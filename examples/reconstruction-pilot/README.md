# GastroFlow candidate: concurrent reservations

Protocol draft only. No repo revision, suite result, rating or attestation has
been assigned. Confirm the actual domain and semantics with the owner before
using this candidate. Do not assume this behavior exists in GastroFlow today.

1. Freeze the reservation contract, revision and acceptance IDs: one eligible
   reservation wins for the same resource and slot; the other receives the
   specified conflict response; persisted state contains one confirmation.
2. Write an independent reserved test that synchronizes requests and checks
   both responses and persisted state. Verify the test rejects a deliberately
   unsafe implementation; pin the suite digest and test environment.
3. Freeze builder inputs, model, tool permissions, budget and attempts before
   the run. Supply specs and approved starter artifacts only. Block original
   source, Git history and oracle access.
4. Evaluate outside the builder environment. Preserve per-obligation outcomes,
   hashes and deviations. A failing mandatory concurrency check blocks the
   attestation even if other checks pass.
5. If an ambiguity is supported by evidence, amend only the implicated rule and
   repeat under the same protocol. Record other plausible causes; a single
   before/after pair does not establish causation.

Calibration criterion: two reviewers independently identify the same mandatory
failure and a comparable closure check, or record why they disagree.

Illustrative result only: create and cancel were demonstrated; concurrent
exclusion failed; retry behavior was not evaluated. If the contract only said
“avoid duplicates”, review whether it omitted the losing request's outcome.
Clarify the rule and repeat with the same reserved suite, model and budget.
Do not issue a reconstruction attestation while mandatory exclusion fails.
