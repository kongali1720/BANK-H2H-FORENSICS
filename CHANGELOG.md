# Changelog

All notable changes to BANK-H2H-FORENSICS are documented here.

## [0.3.0] - 2026-11-24

### Added
- Structured forensic report metadata.
- Unique report identifier (Report ID).
- Optional Case ID support.
- UTC report timestamp.
- Evidence metadata including filename and file size.
- SHA-256 evidence integrity fingerprint.
- Initial evidence intake chain-of-custody event.
- Timestamp consistency between report creation and initial custody event.
- CLI `--case-id` option.
- Expanded evidence metadata unit tests.

### Improved
- Evidence fingerprint is computed once and reused in report metadata.
- Structured evidence intake reporting integrated into the analysis pipeline.

### Security and Limitations
- SHA-256 provides a fingerprint for file integrity comparison.
- File hashing does not authenticate the source institution.
- Parsing does not establish payment execution, settlement, or funds availability.
- Initial custody metadata is not a tamper-proof or digitally signed custody system.
- Bank-origin and transaction verification remain independently unverified.

### Validation
- 17 automated tests passed.
- 8 release candidate validation checks passed.
