# Repository verification

`GUIDO Verify` runs on every pull request targeting main, every push to main
and manual dispatch. Its stable job name is `GUIDO verification`.
It uses a read-only token, no persisted checkout credentials, pinned action
commits and a ten-minute timeout. It does not issue ratings or attestations.

Reproduce the same checks locally with Python 3.10 or later:

```sh
python -m pip install -r requirements-ci.txt
PYTHONPATH=src python -m unittest discover -s tests -v
python scripts/verify_repository.py
```

The verifier strictly parses repository JSON (including rejecting duplicate
keys and non-finite constants), checks the diagnostic schema itself, validates
the mandatory Pipeline calibration and additional JSON objects carrying a
`rubric` field against that schema. Other JSON files receive syntax checks,
not schema certification. It checks inline Markdown file/image destinations
inside the repository; it does not check web URLs, anchors, HTML or reference
links. Structural success does not authenticate evidence.

## Required-check setup

Adding the workflow is not the same as enforcing branch protection. Once this
PR's check has run, a repository administrator must preserve any existing
main rules and add `GUIDO verification` as a required status check, requiring
pull requests and an up-to-date branch. Check the effective rules and an
unprivileged blocked-merge case before claiming enforcement. A passing run
alone does not establish this configuration; do not overwrite other rules.
