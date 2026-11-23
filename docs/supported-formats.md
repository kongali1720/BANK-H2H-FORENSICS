# Supported Formats

## Status

This document describes the intended format coverage and analysis targets.

Listing a format here does not mean a complete parser or validation engine has already been implemented.

Actual support must be confirmed against the implemented version of the software.

## SWIFT FIN

### MT103

Customer credit transfer message commonly associated with cross-border customer payments.

Potential fields for extraction may include:

- :20: Transaction reference
- :23B: Bank operation code
- :32A: Value date, currency, amount
- :50a: Ordering customer
- :52a: Ordering institution
- :56a: Intermediary institution
- :57a: Account-with institution
- :59: Beneficiary
- :70: Remittance information
- :71A: Details of charges
- :72: Sender-to-receiver information

Field interpretation depends on message structure, usage rules, and applicable specifications.

### MT202

Financial institution transfer message.

Potential analysis areas:

- Transaction references
- Related references
- Amount and currency
- Institution identifiers
- Ordering and beneficiary institution fields
- Structured message fields

### MT202 COV

Cover payment message structure.

Potential analysis areas include the cover-payment fields and related customer transfer information when present in the source.

### MT199

Free-format message.

Analysis may include:

- Message references
- Related references
- Text content
- Sender and receiver fields
- Structural observations

### MT192 / MT292

Cancellation-related message types. Parser behavior must be based on the actual message specification and available fields.

## ISO 20022 XML

Target message families may include:

- pacs.008
- pacs.009
- pacs.002
- pacs.004
- pain.001
- pain.002
- camt.053
- camt.054

XML analysis may include:

- Namespace identification
- Root element detection
- Message identification
- Transaction references
- Amount and currency
- Date and timestamp
- Institution identifiers
- Account identifiers
- Status and reason fields
- Structural validation

Schema validation should be implemented only when the correct schema and version are available.

## JSON

Potential analysis:

- JSON syntax
- Key and value extraction
- Nested objects
- Arrays
- Identifier detection
- Numeric fields
- Timestamp candidates
- Structural inconsistencies

## CSV

Potential analysis:

- Header identification
- Row and column counts
- Data type observations
- Numeric values
- Currency fields
- Duplicate rows
- Missing values
- Identifier columns

CSV headers and data are treated as untrusted content.

## Plain Text

Potential analysis:

- Encoding detection where available
- Line and character counts
- Pattern identification
- Reference candidates
- Timestamp candidates
- Structural observations

## Unknown Files

Unknown file types should be handled conservatively.

The analyzer should:

- Identify basic file properties.
- Avoid executing the file.
- Avoid unsafe parsing.
- Provide an unsupported-format message.
- Preserve the original file.
- Record relevant errors.

## Implementation Status

Parser availability, limitations, test coverage, and supported message versions should be maintained as implementation progresses.
