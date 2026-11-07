"""Offline structural checks; never authenticate evidence or assign ratings."""
import argparse
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit

from jsonschema import Draft202012Validator

SKIP = {".git", ".venv", ".venv-ci", "node_modules", "__pycache__", "build", "dist"}


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON key: {key}")
        result[key] = value
    return result


def load_json(path):
    def invalid_constant(value):
        raise ValueError(f"Invalid JSON constant: {value}")
    return json.loads(path.read_text(encoding="utf-8"),
                      object_pairs_hook=unique_object, parse_constant=invalid_constant)


def document_errors(root, path):
    # Deliberately bounded: inline Markdown file/image targets only.
    # No HTTP requests, fragment validation, reference links or HTML parsing.
    text = re.sub(r"^```[^\n]*\n.*?^```[^\n]*$", "", path.read_text(encoding="utf-8"),
                  flags=re.MULTILINE | re.DOTALL)
    errors = []
    for raw in re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", text):
        destination = raw.strip().split()[0].strip("<>")
        url = urlsplit(destination)
        if url.scheme or url.netloc or not url.path:
            continue
        target = ((root / unquote(url.path).lstrip("/")) if url.path.startswith("/")
                  else (path.parent / unquote(url.path))).resolve()
        if not target.is_relative_to(root) or not target.exists():
            errors.append(f"{path.relative_to(root)}: missing/unsafe target {destination}")
    return errors


def check_local_refs(value):
    if isinstance(value, dict):
        for key, item in value.items():
            if key in {"$ref", "$dynamicRef"} and (not isinstance(item, str) or not item.startswith("#")):
                raise ValueError("Schema references must be local fragments")
            check_local_refs(item)
    elif isinstance(value, list):
        for item in value:
            check_local_refs(item)


def verify(root):
    root = root.resolve()
    schema = load_json(root / "auditor/report-schema.json")
    check_local_refs(schema)
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)
    errors = []
    json_count = report_count = doc_count = 0
    required_example = root / "examples/pipeline-calibration.json"
    if not required_example.is_file():
        errors.append("Missing required pipeline calibration example")
    for path in sorted(root.rglob("*")):
        if any(part in SKIP for part in path.relative_to(root).parts):
            continue
        if not path.is_file() or path.is_symlink():
            continue
        if path.suffix == ".json":
            json_count += 1
            try:
                data = load_json(path)
                is_report = isinstance(data, dict) and "rubric" in data
                if path == required_example or is_report:
                    report_count += 1
                    for error in validator.iter_errors(data):
                        errors.append(f"{path.relative_to(root)}: {error.message}")
            except (ValueError, OSError) as error:
                errors.append(f"{path.relative_to(root)}: {error}")
        elif path.suffix.lower() == ".md":
            doc_count += 1
            errors.extend(document_errors(root, path))
    return errors, (json_count, report_count, doc_count)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors, counts = verify(args.root)
    for error in errors:
        print(error)
    if errors:
        return 1
    print(f"PASS: {counts[0]} JSON files, {counts[1]} diagnostic reports, {counts[2]} Markdown files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
