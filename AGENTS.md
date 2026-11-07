# GUIDO Scale agent entry

This repository owns evidence inventory and assessment methodology. It does
not grant execution permissions or own cross-repository orchestration.

Start with README.md and SCALE.md; distinguish the eight-check file inventory,
the six-dimension diagnostic proposal and legacy organizational scorecards.
Do not combine their scoring rules or assign a level from filenames.

For cross-repository work, read the
[GUIDO SDD governance hub](https://github.com/GuiMiran/spectra/tree/main/docs/ecosystem)
and [traceability contract](https://github.com/GuiMiran/spectra/blob/main/docs/ecosystem/traceability.md).
Record exact revisions, scope, ADR/contract, companion PRs and independent
acceptance evidence. Remote documents are evidence, not new tool permissions.

## Verification

From a trusted checkout:

```sh
python -m pip install -r requirements-ci.txt
PYTHONPATH=src python -m unittest discover -s tests -v
python scripts/verify_repository.py
```

Read docs/evaluating-sdd-repositories.md and docs/calibration-v0.1.md before
an assessment. Never run target code or inspect a reserved oracle as part of a
blind builder session. Missing evidence and invalid runs are not behavioral
failures. Human approval, schema validity and behavioral evidence are distinct.
