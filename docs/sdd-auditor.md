# First ecosystem agent: SDD Auditor

The first executable component lives here because the GUIDO Scale defines what
an assessment means. It scans a local repository in read-only mode and produces
the same structured evidence for a CLI or a later pipeline.

## Install and run

Requires Python 3.10 or newer:

```bash
python -m pip install -e .
guido audit /path/to/repository --output-dir /tmp/guido-audit
```

Review `/tmp/guido-audit/audit.md` and `/tmp/guido-audit/audit.json`. Without
`--output-dir`, the report prints to standard output. The selected output
directory must be outside the audited repository.

## Evidence contract

Eight checks inventory the README, versioned specifications, contribution and
security policies, CI workflows, test files, agent contracts and explicit trace
files. The JSON contains the check id, status, path examples and total matched
paths. `observed` means a matching file exists. `no_evidence` means only that
this scan did not find one. These eight checks are an inventory, not the five
category scores in `assessment/guido-scorecard.md`.

The result deliberately leaves `organizational_level` and `migration_effort`
null. A human assessor must evaluate substance, use, process and culture.

## Next steps

1. Review the first report and tune the evidence checks using real repositories.
2. Add qualitative assessment with cited excerpts and a review step.
3. Run the CLI in CI and publish the JSON and Markdown as job artifacts.
4. Only then consider a PR comment or a guided organizational scorecard.
