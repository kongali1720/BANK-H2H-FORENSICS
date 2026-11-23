# Contributing to BANK-H2H-FORENSICS

Thank you for your interest in contributing to BANK-H2H-FORENSICS.

This project aims to provide a transparent, evidence-oriented toolkit for inspecting financial files and analyzing transaction-related data structures.

## Contribution Principles

Contributions should prioritize:

- Accuracy
- Reproducibility
- Evidence integrity
- Security
- Transparency
- Maintainability
- Clear limitations
- Privacy protection
- Defensive file handling

Do not submit code that creates fabricated banking evidence or falsely claims transaction execution, settlement, or beneficiary credit.

## Areas for Contribution

Contributions are welcome in:

- SWIFT FIN parsing
- ISO 20022 XML parsing
- JSON parsing
- CSV analysis
- File identification
- Metadata extraction
- Hashing
- Evidence manifests
- Report generation
- Validation
- Security
- Tests
- Documentation
- User experience
- Accessibility

## Before Starting

1. Check existing issues and pull requests.
2. Describe the proposed change.
3. Identify the intended behavior.
4. Consider backward compatibility.
5. Avoid duplicating existing work.

For significant changes, open an issue or discussion before implementation.

## Development Workflow

1. Fork the repository.
2. Clone your fork.
3. Create a feature branch.
4. Implement your changes.
5. Add or update tests.
6. Run tests and validation.
7. Review your changes.
8. Commit with a descriptive message.
9. Push your branch.
10. Open a Pull Request.

## Branch Naming

Suggested branch names:

- feature/xml-parser
- feature/swift-fin-parser
- fix/path-validation
- docs/evidence-methodology
- security/xml-hardening
- test/hash-validation

## Commit Messages

Use clear and descriptive commit messages.

Examples:

- feat: add ISO 20022 parser
- fix: prevent unsafe XML entity processing
- docs: clarify evidence verification limits
- test: add SHA-256 test cases
- refactor: separate parsing from report generation

## Code Quality

Contributions should:

- Use clear names.
- Keep functions focused.
- Handle errors explicitly.
- Avoid unnecessary complexity.
- Document non-obvious behavior.
- Avoid logging sensitive data.
- Avoid unsafe dynamic execution.
- Avoid destructive file operations.
- Maintain separation between parsing, analysis, and reporting.

## Testing

New functionality should include appropriate tests.

Testing should cover:

- Valid inputs
- Invalid inputs
- Empty files
- Malformed files
- Unexpected encodings
- Large files
- Missing fields
- Duplicate fields
- Edge cases
- Security boundaries
- Failure handling

Use sanitized test fixtures. Never commit confidential financial evidence.

## Documentation

Update documentation when changes affect:

- Supported formats
- Parser behavior
- Output fields
- Security assumptions
- Evidence methodology
- Limitations
- Installation
- Usage
- Configuration

## Pull Request Checklist

- [ ] The change has a clear purpose.
- [ ] Tests were added or updated.
- [ ] Documentation was updated where applicable.
- [ ] No secrets or confidential evidence are included.
- [ ] No real banking information is exposed.
- [ ] Security implications were considered.
- [ ] Transaction claims are evidence-based.
- [ ] Original evidence is not silently modified.
- [ ] The change is consistent with project scope.

## Financial Evidence Integrity

A parser result is a technical observation of file contents.

Contributors must not describe extracted information as independently authenticated banking data unless an independent verification mechanism exists and is documented.

## License

By contributing, you agree that your contributions will be distributed under the project's MIT License, unless a different license is explicitly agreed upon for the contribution.

Thank you for helping improve the project.
