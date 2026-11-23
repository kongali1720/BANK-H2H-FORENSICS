# Security Policy

## Project

BANK-H2H-FORENSICS is an independent financial-file intelligence and transaction-evidence analysis project.

The software is intended to inspect files, extract data, calculate cryptographic fingerprints, identify structural anomalies, and produce analysis reports.

It is not a banking system, payment processor, transaction execution engine, settlement system, or bank authentication service.

## Supported Security Reporting

Please report security vulnerabilities affecting:

- File parsing and parser robustness
- XML entity processing
- Malicious or malformed input handling
- Path traversal
- Arbitrary file access
- Unsafe file writes
- Evidence integrity
- Hash calculation
- Sensitive data exposure
- Report generation
- Dependency vulnerabilities
- Command injection
- Denial-of-service conditions
- Incorrect security assumptions or validation bypasses

## Reporting a Vulnerability

Please do not disclose sensitive vulnerabilities through public issues before the problem has been assessed.

When reporting a security concern, include:

1. A clear description of the vulnerability.
2. Affected files, functions, or components.
3. Steps to reproduce the issue.
4. Expected behavior.
5. Actual behavior.
6. Potential impact.
7. A minimal proof of concept, if safe.
8. Suggested mitigation, if known.

Never include real banking credentials, account passwords, private keys, customer data, confidential payment records, or unredacted financial evidence in a vulnerability report.

## Scope

Security reports should focus on the software and repository components maintained by this project.

This project does not authorize:

- Testing against banks or financial institutions without permission.
- Unauthorized access to financial systems.
- Interception of payment traffic.
- Credential harvesting.
- Exploitation of third-party infrastructure.
- Manipulation of banking records.
- Attempting to initiate, redirect, or alter real payments.

## File Processing Security

Financial files must be treated as untrusted input.

Implementations should:

- Validate input sizes.
- Avoid unsafe XML entity expansion.
- Prevent path traversal.
- Avoid executing source files.
- Avoid interpreting file content as shell commands.
- Limit memory and processing time.
- Use safe temporary-file handling.
- Preserve original files when evidence preservation is requested.
- Avoid writing outside designated directories.
- Redact sensitive information from logs and reports.
- Avoid network access during file parsing unless explicitly required and authorized.

## Evidence Integrity

Original files should be treated as read-only evidence.

When practical:

- Preserve original filenames and timestamps as recorded.
- Calculate SHA-256 fingerprints.
- Record analysis timestamps separately from source metadata.
- Document any transformation.
- Store processed output separately from original evidence.
- Never silently replace original evidence.
- Clearly label analysis-generated files.

A SHA-256 fingerprint demonstrates that two files have matching contents when their hashes match. It does not prove who created a file, whether a bank issued it, whether it is authentic, or whether a transaction occurred.

## Authentication and Transaction Claims

A file parser must not claim that a payment has been authenticated, executed, settled, or credited solely because a file contains fields suggesting those states.

Independent confirmation requires appropriate evidence from authoritative sources.

## Dependencies

Dependencies should be reviewed and updated when vulnerabilities are identified.

Contributors should:

- Use maintained dependencies.
- Avoid unnecessary dependencies.
- Pin or constrain versions where appropriate.
- Review dependency changes.
- Run tests after updates.
- Avoid including secrets in configuration files.

## Security Updates

Security-related changes should be documented in the project history and release notes when releases are established.

## Responsible Use

Use the project only for lawful analysis, authorized investigations, software testing, education, research, and evidence examination.

