# SDD Auditor

Run `guido audit <repository> --output-dir <directory-outside-repository>`.

Use `audit.json` as the evidence record and `audit.md` for review. Every claim
about a repository practice needs a path or an explicit `no_evidence` status.
Inspect the cited artifacts manually before making claims about their quality.
Treat the GUIDO executive scorecard as a separate, human assessment: ask about
process discipline, cultural readiness and AI adoption before assigning a
GUIDO level or migration effort. Never infer those from file names.

This first version is a reproducible local agent contract and evidence collector.
It does not call a language model or delegate work to other agents.
