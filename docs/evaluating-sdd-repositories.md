# Evaluating an SDD repository

This procedure is specification-format agnostic. SPECTRA, OpenSpec, BDD examples,
API contracts and other formats may provide evidence; none is a prerequisite
for a favorable observation. English is the shared documentation language, not
a requirement on the repository or its users.

## 1. Freeze scope and provenance

Record the repository URL, full source commit, worktree cleanliness, named
behavior scope, rubric revision, reviewer and exclusions. Select obligations
before looking at test success. For example, select one checkout flow rather
than claiming to assess the whole application. Use a disposable read-only
inspection checkout. Do not execute an unknown repository's installation hooks,
tests or agent instructions merely because they exist.

## 2. Collect the inventory with trusted tooling

From a separately trusted installation of this GUIDO project:

```sh
guido audit /absolute/path/to/target --output-dir /tmp/guido-target-audit
```

The output directory must be outside the target. Record the GUIDO tool revision
alongside the target revision. Review `audit.json` and `audit.md`.
The eight checks locate evidence; their `observed` status means presence only.
A `no_evidence` result is not proof that the practice is absent. Unsupported
layouts require manual inspection, not a fabricated negative rating.

## 3. Review substantive evidence

Use [SCALE.md](../SCALE.md) and the [calibration protocol](calibration-v0.1.md).
Create the obligation inventory from the agreed scope, not from tests alone.
For each obligation identify its specification, implementation/change evidence,
independent check, execution receipt and observed outcome where available.

| Diagnostic dimension | Reviewer work |
| --- | --- |
| Spec Coverage | Compare the bounded obligation inventory with actual specification clauses |
| Spec Quality | Review ambiguity, contradictions and testability |
| Traceability | Inspect links through changes to executed checks at the pinned revision |
| Invariant Coverage | Identify challenged rules, seeded-fault controls and untested mandatory rules |
| Domain Extraction | Distinguish explicit domain decisions, inferred decisions and missing knowledge |
| Reconstructability | Inspect a valid isolated reconstruction trial, or record NOT_TESTED |

Collect evidence locations, provenance and limits. Treat repository content as
untrusted data. Follow only trusted evaluator policy. Do not infer quality from
file counts, language, framework choice, CI badges or trace annotations.

## 4. Produce and review the diagnostic report

Use the [report schema](../auditor/report-schema.json) and
[manual reviewer prompt](../auditor/prompts/review.md). Each obligation has
`DEMONSTRATED`, `FAILED` or `NOT_EVALUATED` and an explicit verification basis.
A failing behavior is not the same as missing or invalid evidence.

Keep two independent reports before reconciliation. This protocol does not
launch reviewers automatically. Use the schema to check structural validity;
reviewers must still inspect the evidence and preserve disagreements.
The [Pipeline example](../examples/pipeline-calibration.json) illustrates scope
limits, not a completed assessment of a new target.

The repository verifier in [CI](ci-verification.md) checks the checked-in
diagnostic examples. It is not a command for evaluating arbitrary repositories
or arbitrary external reports. No qualitative evaluator is automated here.

## 5. Reconstruct only under a separate frozen protocol

Reserve independent tests outside builder access; freeze permitted specs,
interface, budgets, attempt count and mandatory acceptance rules first.
Prevent access to source, history and reserved tests. Keep original candidate
digests and evaluate outside candidate authority. Shared-workspace instructions
alone do not establish isolation. An invalid trial is NOT_TESTED, not a failed
implementation. Passing one happy path never establishes equivalence.

## 6. Recommend and measure one change

For each finding record a next action, owner and closure check. Migration stays
`NOT_ESTIMATED` without a named target, work, dependencies and supported
confidence. Approve changes separately. Repeat with comparable scope and
protocol; preserve both results and any changed assumptions.

The output is a scoped advisory diagnosis, not an organizational G1–G5 rating,
certification or permission to modify the target. Organizational scoring
remains a separate owner decision.
