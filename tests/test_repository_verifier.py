import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("verify_repository", ROOT / "scripts/verify_repository.py")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class VerificationTests(unittest.TestCase):
    def test_remote_schema_references_are_never_retrieved(self):
        for ref in ["https://example.invalid/schema", "file:///tmp/schema.json", "other.json"]:
            with self.assertRaisesRegex(ValueError, "local fragments"):
                MODULE.check_local_refs({"allOf": [{"$ref": ref}]})
        MODULE.check_local_refs({"$ref": "#/$defs/text"})

    def fixture(self, root):
        (root / "auditor").mkdir()
        (root / "examples").mkdir()
        (root / "auditor/report-schema.json").write_text(
            (ROOT / "auditor/report-schema.json").read_text())
        data = json.loads((ROOT / "examples/pipeline-calibration.json").read_text())
        (root / "examples/pipeline-calibration.json").write_text(json.dumps(data))
        return data

    def test_reference_and_missing_example(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.fixture(root)
            self.assertEqual(MODULE.verify(root)[0], [])
            (root / "examples/pipeline-calibration.json").unlink()
            self.assertIn("Missing required", MODULE.verify(root)[0][0])

    def test_schema_rejects_execution_authority_missing_fields_and_bad_status(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            original = self.fixture(root)
            for mutation in ["authority", "missing", "status", "unknown_rubric"]:
                data = copy.deepcopy(original)
                if mutation == "authority":
                    data["executionAuthorized"] = True
                elif mutation == "missing":
                    del data["dimensions"]
                elif mutation == "status":
                    data["dimensions"]["specCoverage"]["status"] = "PASS"
                else:
                    data["rubric"] = "unknown"
                (root / "examples/pipeline-calibration.json").write_text(json.dumps(data))
                self.assertTrue(MODULE.verify(root)[0], mutation)

    def test_every_json_is_parsed_strictly(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.fixture(root)
            for content in ['{"a":1,"a":2}', '{"a":NaN}', '{']:
                (root / "examples/bad.json").write_text(content)
                self.assertTrue(MODULE.verify(root)[0])

    def test_relative_root_links_and_missing_targets(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.fixture(root)
            doc = root / "README.md"
            doc.write_text("[ok](examples/pipeline-calibration.json) [root](/examples/) "
                           "[web](https://example.invalid/) [anchor](#heading)")
            self.assertEqual(MODULE.verify(root)[0], [])
            doc.write_text("[missing](gone.md) [escape](../outside.md)")
            self.assertEqual(len(MODULE.verify(root)[0]), 2)

    def test_new_report_is_schema_checked_and_fences_are_ignored(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            data = self.fixture(root)
            data["executionAuthorized"] = True
            (root / "examples/new.json").write_text(json.dumps(data))
            self.assertTrue(MODULE.verify(root)[0])
            (root / "examples/new.json").unlink()
            (root / "README.md").write_text("```md\n[x](absent.md)\n```\n")
            self.assertEqual(MODULE.verify(root)[0], [])
