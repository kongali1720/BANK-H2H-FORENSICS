# Security Design

## Security Objective

BANK-H2H-FORENSICS processes user-provided financial files.

Files may be malformed, deceptive, oversized, sensitive, or intentionally crafted to exploit parsers.

Security controls must be considered part of the core architecture.

## Threat Model

Potential threats include:

- Malicious file contents
- XML entity expansion
- XML external entity attacks
- Oversized input
- Resource exhaustion
- Path traversal
- Unexpected encodings
- Parser crashes
- Unsafe temporary-file behavior
- Sensitive data leakage
- Log injection
- Dependency compromise
- Report manipulation
- Accidental destruction of evidence

## Input Handling

Treat every input file as untrusted.

Never:

- Execute source file content.
- Evaluate financial file data as code.
- Execute macros or embedded scripts.
- Trust file extensions.
- Assume files are safe because they appear to be bank documents.
- Automatically open external URLs embedded in files.
- Automatically fetch remote resources referenced by XML.

## XML Security

XML parsers should be configured securely.

Security expectations include:

- Disable external entity resolution.
- Disable external DTD loading.
- Prevent entity expansion attacks.
- Avoid remote resource retrieval.
- Apply file size and processing limits.
- Reject or safely handle malformed XML.
- Use maintained XML libraries.

Schema validation must not introduce unsafe network retrieval.

## Path Safety

File paths must be validated.

Controls should prevent:

- Directory traversal
- Writing outside approved directories
- Overwriting evidence unexpectedly
- Unsafe symbolic-link handling
- Unsafe temporary-file names
- Arbitrary file deletion

## Resource Limits

Where practical, establish limits for:

- File size
- Processing duration
- Memory usage
- XML nesting depth
- CSV rows
- JSON nesting
- Report size
- Batch file count

Resource exhaustion should fail safely.

## Evidence Protection

Original evidence must not be silently changed.

Recommended controls:

- Read-only handling where practical.
- Separate original and processed directories.
- Hash originals.
- Avoid overwriting.
- Track transformations.
- Secure temporary files.
- Redact sensitive data in reports.
- Restrict access to evidence directories.

## Logging

Logs should not contain:

- Passwords
- API keys
- Tokens
- Private keys
- Full account numbers
- Unnecessary personal data
- Full confidential payment messages

Prefer structured, minimal, redacted logs.

## Network Access

The core parsing process should ideally operate offline.

Network access should not be required to parse source files.

Any future external verification feature must be explicitly separated from file parsing and documented with its source, permissions, limitations, and auditability.

## Dependencies

Dependencies must be reviewed.

Avoid:

- Unmaintained packages
- Unnecessary packages
- Unknown binary downloads
- Unverified installation scripts
- Dependencies that perform unexpected network access

## Secrets

Do not commit:

- .env files
- API credentials
- Passwords
- Private keys
- Banking credentials
- Personal access tokens
- Confidential evidence

## Security Testing

Security testing should include:

- Malformed XML
- XML entity payloads
- Oversized files
- Invalid encodings
- Traversal attempts
- Unexpected file extensions
- Empty files
- Deeply nested structures
- Invalid JSON
- CSV edge cases
- Log injection cases

## Failure Handling

When processing fails:

- Report the error safely.
- Avoid stack traces containing secrets in user-facing reports.
- Preserve original evidence.
- Avoid partially overwriting output.
- Record the failure where appropriate.

## Verification Boundary

Technical file analysis is not banking verification.

Security and analysis outputs must clearly distinguish:

- File integrity
- Structural validity
- Extracted content
- Internal consistency
- External authenticity
- Payment execution
- Settlement
- Beneficiary credit

Only the first four may be established through local file analysis alone, and even those depend on implementation quality and evidence.
