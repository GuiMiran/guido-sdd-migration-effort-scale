# GUIDO Scale v0.1 — Repository knowledge and reconstruction

Status: proposed for calibration, not an approved scoring or certification policy.
The existing organizational scorecard and the inventory-only CLI remain unchanged.

Assess a named behavior scope at a pinned revision, not an organization or an
entire repository by implication. Publish six diagnostic observations, an optional
reconstruction attestation, and a separate migration estimate to a named target.
No weights, overall grade, automatic attestation or write authority in v0.1.

Use the proposed [calibration protocol](docs/calibration-v0.1.md) for evidence
anchors and independent reviewer comparison. It does not resolve or replace
the legacy organizational scoring policies.

## Diagnostic dimensions

Use OBSERVED for a supported observation (including weaknesses), NOT_ASSESSED
for insufficient evidence and NOT_TESTED for an unrun or invalid reconstruction.

| Dimension | Diagnostic question |
| --- | --- |
| Spec Coverage | Which inventoried obligations are missing from the specs? |
| Spec Quality | Which clauses are ambiguous, contradictory or not testable? |
| Traceability | Which links from obligation to change and executed test are verified at this revision? |
| Invariant Coverage | Which mandatory rules were challenged, and which remain untested? |
| Domain Extraction | Which decisions still require asking the author or guessing? |
| Reconstructability | Which behaviors survived reconstruction without the original code? |

Record the inventory denominator, selection method, evidence IDs and limitations.
For each inventoried obligation record a unique ID, verification basis
(existing implementation or reconstruction), mandatory status and
DEMONSTRATED, FAILED or NOT_EVALUATED, with evidence for measured outcomes.
An incomplete inventory cannot support a completeness claim.
Do not treat a filename, a trace declaration or a self-reported test
result as an attestation.

## Reconstruction protocol

Freeze the scope, permitted inputs, mandatory obligations, reserved independent
tests, model/tool versions, budget, attempt count and acceptance rule before
running. Isolate the builder from original implementation, history and reserved
tests. Run the oracle outside builder authority. Record input/output digests,
test outcomes, failures and deviations. An invalid run is not a behavioral
failure. Attest only when all required attempts and mandatory checks pass,
with a named reviewer and explicit exclusions. The attestation is project-issued,
not accredited certification or proof of general agent capability.

## Review and handoff

Compare only equivalent scopes, rubric revisions and protocols. Prioritize
mandatory failures and unresolved evidence. Each
finding names a next action and a test or artifact that can close it. Record
migration work, dependencies and confidence independently, or NOT_ESTIMATED.
The report is an advisory input for SPECTRA; it cannot grant execution rights.
See [report schema](auditor/report-schema.json), [manual prompt](auditor/prompts/review.md),
[Pipeline calibration](examples/pipeline-calibration.json) and
[GastroFlow pilot](examples/reconstruction-pilot/README.md).
