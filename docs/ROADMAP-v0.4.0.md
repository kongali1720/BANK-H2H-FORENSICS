# BANK-H2H-FORENSICS v0.4.0 Development Roadmap

## Release Objective

Upgrade BANK-H2H-FORENSICS from v0.3.0 with improved financial-file
structural analysis, evidence handling, reporting, testing, and CLI
capabilities while preserving the existing project identity and README design.

## Development Tracks

### 1. Core Engine
- Review current engine and analysis pipeline.
- Improve validation and error handling.
- Preserve deterministic and evidence-based processing.

### 2. SWIFT Structural Analysis
- Improve SWIFT-like message structure inspection.
- Expand tag and message-type candidate analysis.
- Clearly distinguish structural inspection from authentication or validation.

### 3. Financial File Analysis
- Improve structured JSON, CSV, and XML inspection.
- Investigate additional field-level analysis.
- Evaluate ISO 20022 XML analysis enhancements.

### 4. Evidence and Integrity
- Improve evidence metadata.
- Expand evidence manifest capabilities.
- Enhance integrity and reproducibility workflow.
- Document SHA-256 limitations.

### 5. Reporting
- Improve JSON report structure.
- Expand warnings and limitations.
- Improve report readability and consistency.

### 6. CLI
- Review command-line arguments.
- Improve user-facing output and error messages.
- Preserve compatibility where practical.

### 7. Quality Assurance
- Add tests for edge cases and invalid input.
- Improve parser test coverage.
- Run pytest, Ruff, and package build.
- Review CI workflow.

### 8. Documentation
- Preserve the original README branding, badges, images, Mermaid diagrams,
  and layout.
- Update documentation only to reflect implemented capabilities.
- Add v0.4.0 release notes after implementation is complete.

## Release Gate

The v0.4.0 release is not considered complete until:

- [ ] Implementation tasks are completed and reviewed.
- [ ] Tests pass.
- [ ] Ruff checks pass.
- [ ] Build succeeds.
- [ ] Security and privacy review is completed.
- [ ] Documentation accurately reflects implemented functionality.
- [ ] Release notes are prepared.
- [ ] Version is updated consistently.
- [ ] Git tag and GitHub Release are prepared.

## Scope Disclaimer

This roadmap describes planned development. Planned features must not be
represented as implemented or as proof of real financial transactions,
bank authentication, payment execution, settlement, beneficiary credit,
or funds availability.
