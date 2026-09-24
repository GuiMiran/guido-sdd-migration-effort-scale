"""Deterministic, read-only evidence collection. No network or model calls."""

import argparse
import json
from pathlib import Path
import subprocess
import sys

SKIP = {".git", "node_modules", ".venv", "venv", "dist", "build", "coverage", ".next"}

CHECKS = (
    ("documentation", "project_readme", "Project README", lambda p: p.name.lower() == "readme.md" and p.parent == Path(".")),
    ("documentation", "specifications", "Versioned specifications", lambda p: any(x.lower() in ("spec", "specs", ".spectra", "specifications") for x in p.parts[:-1]) and p.suffix.lower() in (".md", ".yaml", ".yml", ".json")),
    ("governance", "contribution_policy", "Contribution guidance", lambda p: p.name.lower() in ("contributing.md", "code_of_conduct.md")),
    ("governance", "security_policy", "Security policy", lambda p: p.name.lower() == "security.md"),
    ("automation", "ci_workflow", "CI workflow", lambda p: len(p.parts) >= 3 and p.parts[:2] == (".github", "workflows") and p.suffix.lower() in (".yaml", ".yml")),
    ("quality", "tests", "Versioned tests", lambda p: (p.name.lower().startswith("test_") and p.suffix.lower() == ".py") or p.name.lower().endswith((".test.js", ".test.ts", ".test.mjs", ".spec.js", ".spec.ts", ".spec.mjs", "tests.cs", "test.cs"))),
    ("agents", "agent_contract", "Agent instructions or contract", lambda p: (p.parent == Path(".") and p.name.lower() == "agents.md") or (p.name.lower() in ("agent.yaml", "agent.yml") and "agents" in p.parts) or ("agents" in p.parts[:-1] and p.suffix.lower() in (".md", ".yaml", ".yml")) or (p.name.lower() in ("agentes.md", "agents.md") and "dev" in p.parts[:-1])),
    ("traceability", "trace_map", "Explicit trace mapping", lambda p: "trace" in p.name.lower() and p.suffix.lower() in (".json", ".yaml", ".yml", ".md")),
)

RECOMMENDATIONS = {
    "project_readme": "Add a root README explaining purpose and how to run the project.",
    "specifications": "Version functional requirements and acceptance criteria in a specs/ directory.",
    "contribution_policy": "Document the contribution and review process in CONTRIBUTING.md.",
    "security_policy": "Document security reporting in SECURITY.md.",
    "ci_workflow": "Add a CI workflow that checks the repository on pull requests.",
    "tests": "Add automated behavioral tests for the primary contract.",
    "agent_contract": "Define the agent's inputs, outputs, tools and permissions.",
    "trace_map": "Record explicit links between requirements, code, tests and evidence.",
}


def inventory(root):
    found = []
    for directory, dirs, files in __import__("os").walk(root, followlinks=False):
        dirs[:] = sorted(d for d in dirs if d not in SKIP and not (Path(directory) / d).is_symlink())
        for name in sorted(files):
            path = Path(directory) / name
            if not path.is_symlink() and path.is_file():
                found.append(path.relative_to(root))
    return found


def audit(root):
    paths = inventory(root)
    checks = []
    for dimension, check_id, label, predicate in CHECKS:
        evidence = [p.as_posix() for p in paths if predicate(p)]
        checks.append({"id": check_id, "dimension": dimension, "label": label,
                       "status": "observed" if evidence else "no_evidence",
                       "evidence": evidence[:20], "evidence_count": len(evidence),
                       "recommendation": None if evidence else RECOMMENDATIONS[check_id]})
    head = None
    if (root / ".git").exists():
        command = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"],
                                 capture_output=True, text=True, check=False)
        if command.returncode == 0:
            head = command.stdout.strip()
    return {
        "schema_version": "1.0", "agent": "sdd-auditor", "agent_version": "0.1.0",
        "repository": {"path": str(root), "commit": head, "files_inspected": len(paths)},
        "scope": "Repository file presence only; observed does not imply quality or enforcement.",
        "checks": checks,
        "summary": {"observed": sum(c["status"] == "observed" for c in checks),
                    "no_evidence": sum(c["status"] == "no_evidence" for c in checks)},
        "guido_scale": {"organizational_level": None, "migration_effort": None,
                        "reason": "Process, culture, adoption and actual practices require human assessment."},
    }


def markdown(report):
    lines = ["# SDD repository evidence audit", "", f"Repository: `{report['repository']['path']}`",
             f"Commit: `{report['repository']['commit'] or 'unavailable'}`", "",
             f"Observed: {report['summary']['observed']}/8; no evidence: {report['summary']['no_evidence']}/8.",
             "", "| Dimension | Check | Status | Evidence |", "|---|---|---|---|"]
    for c in report["checks"]:
        examples = ", ".join(f"`{p}`" for p in c["evidence"][:3]) or "—"
        lines.append(f"| {c['dimension']} | {c['label']} | {c['status']} | {examples} |")
    lines += ["", "## Next steps", ""]
    lines += [f"- {c['recommendation']}" for c in report["checks"] if c["recommendation"]]
    if not any(c["recommendation"] for c in report["checks"]):
        lines.append("- Review the observed artifacts for substance and enforcement.")
    lines += ["", "## Interpretation", "", report["scope"],
              "Absence means the check found no matching file, not that the practice does not exist.",
              "No organizational GUIDO level or migration effort is assigned by this scan.", ""]
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(prog="guido", description="GUIDO repository evidence auditor")
    sub = parser.add_subparsers(dest="command", required=True)
    cmd = sub.add_parser("audit", help="Audit a local repository without modifying it")
    cmd.add_argument("repository", type=Path)
    cmd.add_argument("--output-dir", type=Path, help="Write audit.json and audit.md outside the repository")
    args = parser.parse_args(argv)
    root = args.repository.expanduser().resolve()
    if not root.is_dir():
        parser.error(f"Repository is not a directory: {root}")
    if args.output_dir:
        out = args.output_dir.expanduser().resolve()
        if out == root or root in out.parents:
            parser.error("Output directory must be outside the audited repository")
        out.mkdir(parents=True, exist_ok=True)
    report = audit(root)
    if args.output_dir:
        (out / "audit.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        (out / "audit.md").write_text(markdown(report), encoding="utf-8")
        print(f"Wrote {out / 'audit.json'} and {out / 'audit.md'}")
    else:
        print(markdown(report))
    return 0


if __name__ == "__main__":
    sys.exit(main())
