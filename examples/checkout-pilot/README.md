# GastroFlow checkout — reconstruction trial preparation

**Status:** Source inputs pinned; independent oracle and isolated execution
pending. No reconstruction result or attestation. This is a different case
from the illustrative reservations pilot.

## Prepare

- A trusted packager reads the nine Markdown blobs listed in
  [input-manifest.json](input-manifest.json) at the pinned GastroFlow commit
  and verifies Git blob SHA-1 using the original bytes. Deliver only those
  files and an agreed harness interface. Keep this manifest, repo URL, Git
  metadata, source, existing tests and trace files out of the builder input.
  Historical references in the specs are not permission to retrieve them.
- An independent verifier authors the oracle from the frozen contract. Check
  AC-001 in full: sufficient payment, change, ticket and fiscal breakdown,
  record creation, service closure, table release and event. Check AC-002:
  insufficient payment rejected without completing a ticket or closing the
  service. Check INV-001 and INV-002 explicitly. The exercise tests specified
  behavior; it does not attest legal compliance or external fiscal integration.
- Keep concrete oracle fixtures outside the public repository and builder
  access. Before execution, verify the oracle rejects a deliberately wrong
  implementation. Record the suite digest and versioned runner interface,
  the model and budget, exact isolation controls and number of attempts.
  None is claimed frozen by the input manifest.

## Execute and record

Run in a fresh builder environment with no network, original checkout, history
or oracle access. The builder returns its implementation and decision log.
For each decision record the spec clause (if any), the chosen behavior and
whether it was explicit, inferred or unsupported. Do not patch gaps mid-run.

Run the oracle independently, outside builder authority. Record per-obligation
outcomes and digests with the existing GUIDO report schema. An invalid run is
not an obligation failure. Missing or failed mandatory evidence prevents an
attestation. If a rule is implicated, change only that rule in a second input
bundle and rerun with the same protocol; report variability and alternative
causes. No global score.
