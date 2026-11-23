# Development Roadmap

## Vision

Build a modular, transparent, evidence-oriented financial-file analysis toolkit.

The project prioritizes safe file handling, reproducibility, parser accuracy, privacy, and honest reporting.

## Milestone 0 — Repository Foundation

- [x] Repository created
- [x] README published
- [x] MIT License added
- [x] Security policy added
- [x] Contribution guide added
- [x] Code of Conduct added
- [x] Evidence methodology documented
- [x] Architecture documented
- [x] Format targets documented
- [x] GitHub issue templates
- [x] Pull request template
- [x] Automated documentation workflow

## Milestone 1 — Core Utilities

- [ ] File intake interface
- [ ] File size limits
- [ ] File type identification
- [ ] SHA-256 hashing
- [ ] Safe filename handling
- [ ] Structured logging with sensitive-data redaction
- [ ] Error model

## Milestone 2 — Data Parsers

- [ ] Generic text parser
- [ ] JSON parser
- [ ] CSV parser
- [ ] XML parser
- [ ] SWIFT FIN parser
- [ ] ISO 20022 message detection

## Milestone 3 — Analysis

- [ ] Field extraction
- [ ] Reference detection
- [ ] Amount and currency detection
- [ ] Date and timestamp handling
- [ ] BIC detection
- [ ] Structural checks
- [ ] Consistency checks
- [ ] Findings model

## Milestone 4 — Evidence and Reporting

- [ ] Evidence manifest
- [ ] Hash manifest
- [ ] JSON report
- [ ] Human-readable report
- [ ] Report redaction
- [ ] Multi-file comparison
- [ ] Analysis reproducibility metadata

## Milestone 5 — Quality and Security

- [ ] Unit test suite
- [ ] Parser edge-case fixtures
- [ ] Malformed input testing
- [ ] XML security testing
- [ ] Path traversal testing
- [ ] Dependency review
- [ ] Security checklist

## Milestone 6 — Usability

- [ ] Command-line interface
- [ ] Batch analysis
- [ ] Search extracted findings
- [ ] Report export
- [ ] User documentation
- [ ] Optional graphical interface evaluation

## Release Criteria

A release should not be published until:

- Core tests pass.
- Security considerations are reviewed.
- Documentation reflects actual functionality.
- Unsupported formats are clearly identified.
- No sensitive evidence or credentials are included.
- Release notes accurately describe limitations.
