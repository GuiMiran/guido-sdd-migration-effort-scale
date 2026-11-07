# GUIDO v0.1 calibration protocol

Status: proposal for human review. This guide operationalizes [SCALE.md](../SCALE.md);
it does not ratify organizational scoring, change the inventory CLI or authorize
execution. The six diagnostic dimensions are not G1–G5 organizational ratings.

## Choose the right instrument

| Question | Instrument | Limit |
| --- | --- | --- |
| What evidence files exist? | `guido audit` | Presence inventory only; no quality score |
| What can be demonstrated for a named behavior at one revision? | `SCALE.md` and `auditor/report-schema.json` | v0.1 diagnostic proposal; no aggregate grade |
| How ready is an organization? | Existing organizational assessment documents | Human assessment; aggregation policy remains unresolved |

The executive scorecard sums five category ratings. The assessment template
contains 25 questions but a maximum of 25 points without an explicit
question-to-pillar aggregation. The skill describes six dimensions and a
bottleneck rule. Do not combine these algorithms, choose one silently, or map
v0.1 observations to a G level. The owner must ratify the organizational policy
in a separate decision.

## Evidence anchors for each diagnostic dimension

| Dimension | Minimum basis for a supported observation | What remains unknown |
| --- | --- | --- |
| Spec Coverage | Independently reviewed, bounded obligation inventory; identify clauses present or absent for every inventoried ID | No completeness claim if the denominator or selection is incomplete |
| Spec Quality | Versioned clauses reviewed for ambiguity, contradictions and testability; cite precise examples and the review method | A well-written sample does not establish whole-repository quality |
| Traceability | Reviewed links from a named obligation to change and executed check, pinned to a revision and receipt | An annotation or passing test alone is not an end-to-end verified chain |
| Invariant Coverage | Reviewed mandatory-rule inventory and challenge outcomes, including untested obligations and negative controls | Coverage outside that inventory is unknown |
| Domain Extraction | Frozen input package and independent decision review distinguishing explicit rules, guesses and unavailable knowledge | Author explanations supplied later are not part of the original package |
| Reconstructability | Frozen protocol, isolated builder, original output digest and independent evaluation record | Unrun, invalid or contaminated trials are NOT_TESTED, not behavioral failures |

`OBSERVED` means supported, not successful: a demonstrated mandatory failure
is still an observation. Use `FAILED` on the corresponding obligation.
`NOT_ASSESSED` identifies an unsupported diagnostic observation; use
`NOT_TESTED` for unrun or invalid reconstruction. Follow the existing JSON schema.
Schema validation checks shape, not whether evidence is authentic or sufficient.

## Run a bounded calibration

1. Freeze scope, source revision, rubric revision and reviewed obligation
   inventory. State exclusions and the selection method. Separate implementation
   verification from reconstruction.
2. Register each evidence item: ID, immutable location, source revision, producer,
   run/time and digest where available. Inspect its contents; a link is not proof.
   Do not include private suites or credentials in a public report.
3. Give the same packet to two reviewers independently. Each returns the
   [existing report format](../auditor/report-schema.json), using the
   [review prompt](../auditor/prompts/review.md). Neither sees the other's report.
4. Compare per-obligation outcomes, unknowns, six dimension statuses and closure
   checks. Record matching decisions over comparable decisions with the
   denominator; do not report an agreement percentage without it.
5. Keep both originals and a separate reconciliation with reviewer identity,
   disagreements, rationale and owner decision. Unresolved disagreement remains
   visible; do not average it into a score.
6. Choose one evidenced gap, its owner and a closure check. Reassess with the same
   scope and protocol after an approved change. If inventory or protocol changes,
   version it and explain why the results are not directly comparable.

Migration is `NOT_ESTIMATED` unless a named target, concrete work, dependencies
and justified confidence are available. Do not derive duration from a GUIDO label.

## Suggested first packet: public synthetic controls

Use the SPECTRA Umbral, rounding and idempotency examples as an instrument check,
not a maturity assessment. Freeze a commit that contains all three examples and
capture a fresh run before assessing it; no such run or reviewer agreement is
claimed by this document.

Inventory: allowed transition persists; forbidden transition is rejected without
changing state; small-amount rounding follows its explicit policy; same-key retry
preserves response and stored record count. Record each separately. Challenge
the assertions with their seeded defects. A passing reference plus caught
mutants validates only those controls. It does not establish tax compliance,
concurrency safety, reconstructability or organizational maturity.

## Owner decisions still required

- Approve or amend v0.1's diagnostic scope and this calibration method.
- Name reviewers and approve a pilot packet, revision and mandatory inventory.
- Select the organizational aggregation policy separately; no change here.
- Approve any reconstruction attestation separately after the required evidence.
