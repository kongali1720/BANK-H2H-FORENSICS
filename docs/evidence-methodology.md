# Evidence Methodology

## Purpose

This document defines the project's baseline methodology for handling and analyzing financial files.

It is a software analysis methodology, not a substitute for formal forensic procedures, institutional policies, legal requirements, or professional forensic standards.

## 1. Scope

The analyzer may inspect:

- Financial message files
- Payment-related XML
- SWIFT FIN text
- JSON records
- CSV transaction tables
- Plain-text financial data
- Other supported structured files

The analyzer is not a bank authentication service.

## 2. Evidence Categories

### Original Evidence

The original source file submitted for examination.

### Derived Evidence

Information produced by processing the original source, including:

- Parsed fields
- Normalized data
- Calculated hashes
- Validation results
- Analysis reports

### External Evidence

Information obtained independently of the source file, such as confirmation obtained through an authorized institutional channel.

External evidence should be documented separately.

## 3. Preservation

Where practical:

- Preserve original files.
- Avoid editing source evidence.
- Use copies for processing.
- Separate originals from derived artifacts.
- Record filenames and file sizes.
- Calculate file fingerprints.
- Document processing steps.
- Record errors and limitations.

## 4. File Fingerprinting

The system may calculate SHA-256 hashes.

A hash can be used to:

- Compare files
- Detect content changes
- Identify exact file copies
- Support evidence tracking

A hash cannot independently establish:

- Who created the file
- Whether the source was a bank
- Whether a document is authorized
- Whether the contents are truthful
- Whether a transaction was executed
- Whether funds were settled
- Whether a beneficiary received funds

## 5. Analysis Record

Each analysis record should contain, where available:

- Analysis identifier
- Original filename
- File size
- Detected format
- SHA-256 hash
- Analysis timestamp
- Tool version
- Parser name
- Parser status
- Extracted fields
- Validation findings
- Warnings
- Errors
- Limitations

## 6. Observations and Findings

A finding should be reproducible and connected to the input evidence.

Preferred finding structure:

- Finding ID
- Category
- Severity
- Description
- Evidence location
- Observed value
- Expected condition
- Rule applied
- Confidence or limitation
- Recommended review

The system should avoid unsupported accusations or conclusions.

## 7. Field Extraction

Extracted fields must be labeled as extracted values.

Examples:

- Message reference
- Transaction reference
- Amount
- Currency
- Date
- Timestamp
- BIC
- Sender field
- Receiver field
- Message type
- Related reference

Field extraction does not independently verify the real-world meaning or validity of the values.

## 8. Validation

Validation may evaluate:

- Required field presence
- Format
- Data types
- XML structure
- Schema compatibility when supported
- Date parsing
- Currency formatting
- Numeric consistency
- Duplicate identifiers
- Cross-field consistency

Validation results should be descriptive and explain the rule applied.

## 9. Evidence Limitations

The existence of a message or transaction-related file does not establish that:

- The file originated from a bank.
- The file was transmitted.
- The message was accepted.
- The payment was authorized.
- The payment was executed.
- Funds were settled.
- Funds are available.
- A beneficiary account was credited.

Those conclusions require independent and appropriate evidence.

## 10. Sensitive Data

Reports should minimize exposure of sensitive financial information.

Where appropriate, redact:

- Account numbers
- IBANs
- Customer names
- Addresses
- Phone numbers
- Email addresses
- Identification numbers
- Credentials
- Tokens

Redaction must be clearly identified. A redacted report should not be confused with the original source.

## 11. Reproducibility

A reproducible examination should retain:

- Original evidence
- File fingerprint
- Tool version
- Analysis configuration
- Parser version
- Processing timestamps
- Output report
- Relevant validation rules

## 12. Chain-of-Custody Considerations

This project may support basic evidence tracking but does not automatically implement a legally complete chain-of-custody process.

Users requiring formal forensic procedures must follow applicable institutional, legal, regulatory, and professional requirements.
