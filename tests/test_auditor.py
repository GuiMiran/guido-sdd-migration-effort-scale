import tempfile
import unittest
from pathlib import Path

from guido_auditor.cli import audit, markdown


class AuditorTests(unittest.TestCase):
    def test_evidence_and_missing_practices_are_distinct(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "README.md").write_text("Project\n")
            (root / "specs").mkdir()
            (root / "specs" / "acceptance.md").write_text("Acceptance\n")
            report = audit(root)
            checks = {c["id"]: c for c in report["checks"]}
            self.assertEqual(checks["specifications"]["evidence"], ["specs/acceptance.md"])
            self.assertEqual(checks["ci_workflow"]["status"], "no_evidence")
            self.assertIsNone(report["guido_scale"]["organizational_level"])
            self.assertIn("not that the practice does not exist", markdown(report))

    def test_nested_vendor_files_do_not_create_false_evidence(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "node_modules" / "tests").mkdir(parents=True)
            (root / "node_modules" / "tests" / "test_vendor.py").write_text("pass\n")
            checks = {c["id"]: c for c in audit(root)["checks"]}
            self.assertEqual(checks["tests"]["status"], "no_evidence")

    def test_test_package_initializer_is_not_a_test(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "tests").mkdir()
            (root / "tests" / "__init__.py").write_text("")
            checks = {c["id"]: c for c in audit(root)["checks"]}
            self.assertEqual(checks["tests"]["status"], "no_evidence")

    def test_uppercase_game_spec_is_not_confused_with_gameplay_agents(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            (root / "Spec" / "game" / "design").mkdir(parents=True)
            (root / "Spec" / "game" / "invariants.yaml").write_text("rules: []\n")
            (root / "Spec" / "game" / "design" / "agents.md").write_text("Game units\n")
            checks = {c["id"]: c for c in audit(root)["checks"]}
            self.assertEqual(checks["specifications"]["status"], "observed")
            self.assertEqual(checks["agent_contract"]["status"], "no_evidence")

            (root / "Spec" / "dev").mkdir()
            (root / "Spec" / "dev" / "agentes.md").write_text("Development roles\n")
            checks = {c["id"]: c for c in audit(root)["checks"]}
            self.assertEqual(checks["agent_contract"]["evidence"], ["Spec/dev/agentes.md"])


if __name__ == "__main__":
    unittest.main()
