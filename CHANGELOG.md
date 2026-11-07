# Changelog

## Unreleased

### Added

- Proposed `GUIDO Verify` GitHub Actions workflow for PRs targeting main, pushes
  to main and manual dispatch; read-only permissions, pinned actions and bounded
  runtime.
- Repository verifier: strict JSON syntax, diagnostic report/schema validation
  and local inline Markdown target checks. Remote schema references are rejected.
- Negative tests for invalid reports, authority escalation, malformed JSON,
  duplicate keys, missing examples and broken/unsafe document targets.
- Local verification instructions and the separate required-check setup.
- English, specification-format-agnostic guide for target repository evaluation,
  separating inventory, qualitative review and isolated reconstruction.
- Didactic README with an evaluation flowchart, instrument selection and
  evidence-to-claim examples; no new scoring policy.

### Boundaries

- No GUIDO score, attestation, CLI output or report-schema change.
- A workflow file does not establish enforced main protection; administrator
  configuration and verification of effective rules remain separate.
