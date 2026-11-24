

<p align="center">
<img src="https://github.com/kongali1720/KongWallet-Payment-Gateway-API/blob/main/kop_surat.jpg" width="100%">
</p>

<h1 align="center">🏦 BANK-H2H-FORENSICS</h1>

<h3 align="center">
Financial File Intelligence & Transaction Evidence Analyzer
</h3>

<p align="center">
  <b>Analyze the Evidence. Verify the Data. Never Assume the Transaction.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/PROJECT-FINANCIAL_FORENSICS-0A0A0A?style=for-the-badge&logo=bitcoin&logoColor=white">
  <img src="https://img.shields.io/badge/PYTHON-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/STATUS-ACTIVE_DEVELOPMENT-00C853?style=for-the-badge">
  <img src="https://img.shields.io/badge/SECURITY-EVIDENCE_BASED-0057FF?style=for-the-badge&logo=shield&logoColor=white">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/SWIFT-FIN_MESSAGES-FF6600?style=flat-square">
  <img src="https://img.shields.io/badge/ISO_20022-XML-6A5ACD?style=flat-square">
  <img src="https://img.shields.io/badge/JSON-SUPPORTED-000000?style=flat-square&logo=json">
  <img src="https://img.shields.io/badge/CSV-SUPPORTED-008000?style=flat-square">
  <img src="https://img.shields.io/badge/SHA256-FILE_INTEGRITY-555555?style=flat-square">
  <img src="https://img.shields.io/badge/OPEN_SOURCE-RESEARCH-FFFFFF?style=flat-square&logo=github&logoColor=black">
</p>

---

## 📌 Overview

**BANK-H2H-FORENSICS** is an open-source financial file intelligence and transaction evidence analysis project designed to inspect, identify, parse, fingerprint, and report on banking-related files.

The project focuses on examining real source files and extracting structured information without making unsupported assumptions about transaction authenticity, payment execution, settlement, or beneficiary credit.

It is designed for financial technology research, digital forensic workflows, file inspection, transaction data analysis, and technical investigations.

---

## 🎯 Project Objectives

- Analyze real financial files supplied by the user or authorized source.
- Identify file formats and message structures.
- Parse SWIFT FIN message structures.
- Inspect ISO 20022 XML payment messages.
- Extract transaction identifiers and reference information.
- Extract amounts, currencies, dates, BICs, and selected payment fields.
- Generate SHA-256 file integrity fingerprints.
- Produce structured JSON forensic reports.
- Identify malformed, incomplete, suspicious, or inconsistent file structures.
- Preserve the distinction between file evidence and actual bank transaction status.

---

## 🔍 Core Features

| Feature | Description |
|---|---|
| 📁 File Identification | Detect supported file formats |
| 🏦 SWIFT FIN Parser | Extract fields from FIN message structures |
| 🌐 ISO 20022 XML Parser | Parse XML financial message structures |
| 📄 JSON Analyzer | Inspect structured financial JSON |
| 📊 CSV Analyzer | Analyze tabular transaction records |
| 🔐 SHA-256 Fingerprinting | Generate file integrity hash |
| 🧬 Metadata Extraction | Extract references, identifiers, and timestamps |
| 💰 Amount Extraction | Identify amounts and currency information |
| 🏛️ BIC Extraction | Detect relevant bank identifier fields |
| 🧾 Evidence Reporting | Generate structured forensic output |
| ⚠️ Integrity Checks | Detect parsing issues and structural inconsistencies |
| 📦 Batch Analysis | Planned analysis of multiple files |
| 📝 Report Generation | JSON and future human-readable reports |

---

## 🛡️ Forensic Principles

This project follows an evidence-based approach.

A file containing a payment instruction does not independently prove that:

- The sending bank authenticated the message.
- A transaction was executed.
- Funds were debited.
- Funds were settled.
- The receiving bank accepted the transaction.
- The beneficiary account was credited.
- Funds are available for withdrawal.

### Evidence classification

| Evidence | What it can establish |
|---|---|
| Original file | A file was provided for examination |
| SHA-256 hash | File fingerprint at the time of analysis |
| Parsed message | Structured contents found in the file |
| Transaction reference | Reference value present in the source |
| BIC field | BIC value present in the source |
| Amount & currency | Amount information contained in the file |
| Bank confirmation | Requires independently verified bank evidence |
| Settlement confirmation | Requires reliable external confirmation |
| Beneficiary credit | Requires receiving-bank/account evidence |

> **Important:** Parsing a financial message is not equivalent to authenticating the message or confirming a financial transaction.

---

## 🏗️ System Architecture

```mermaid
flowchart TD
    A["Original Financial File"] --> B["Evidence Intake"]
    B --> C["File Identification"]
    C --> D["SHA-256 Fingerprinting"]
    D --> E{"Format Detection"}

    E -->|SWIFT FIN| F["FIN Parser"]
    E -->|ISO 20022 XML| G["XML Parser"]
    E -->|JSON| H["JSON Parser"]
    E -->|CSV| I["CSV Parser"]
    E -->|Other| J["Generic File Inspection"]

    F --> K["Structured Data Extraction"]
    G --> K
    H --> K
    I --> K
    J --> K

    K --> L["Field Analysis"]
    L --> M["Consistency Checks"]
    M --> N["Evidence Classification"]
    N --> O["Forensic Report"]

    O --> P["JSON Output"]
    O --> Q["Human Readable Report"]
```

---

## 🔄 Analysis Workflow

```mermaid
flowchart TD
    A["START"] --> B["Select Source File"]
    B --> C["Read File Safely"]
    C --> D["Calculate SHA-256"]
    D --> E["Detect File Format"]
    E --> F["Parse Supported Structure"]
    F --> G["Extract Available Fields"]
    G --> H["Analyze Structural Integrity"]
    H --> I["Record Findings"]
    I --> J["Generate Report"]
    J --> K["Save Output"]
    K --> L["END"]

    F -->|Unsupported Format| M["Generic Inspection"]
    M --> I
```

---

## 📂 Supported Formats

### SWIFT FIN

Planned and ongoing parser support for common FIN message structures, including:

- MT103 — Customer Credit Transfer
- MT202 — General Financial Institution Transfer
- MT202 COV — Cover Payment
- MT199 — Free Format Message
- MT192 / MT292 — Cancellation-related message types
- Other FIN message types as parser coverage expands

The analyzer extracts available message fields and reports parser limitations.

### ISO 20022

XML-based payment and financial messages, with support development targeting structures such as:

- `pacs.008`
- `pacs.009`
- `pacs.002`
- `pacs.004`
- `pain.001`
- `pain.002`
- `camt.053`
- `camt.054`

Actual parser support depends on implemented schemas and message structures.

### Other formats

- JSON
- CSV
- TXT
- XML
- Unknown / unrecognized files

---

## 🧾 Evidence Processing

```mermaid
flowchart LR
    A["Source File"] --> B["Read-Only Analysis"]
    B --> C["Hash Calculation"]
    C --> D["Parser"]
    D --> E["Extracted Evidence"]

    E --> F["Message Fields"]
    E --> G["References"]
    E --> H["Financial Values"]
    E --> I["Metadata"]

    F --> J["Report"]
    G --> J
    H --> J
    I --> J

    J --> K["Integrity Fingerprint"]
    J --> L["Analysis Findings"]
    J --> M["Verification Limitations"]
```

---

## 🗂️ Project Structure

```text
BANK-H2H-FORENSICS/
│
├── app/
│   ├── analyzer.py
│   ├── parsers/
│   │   ├── swift_fin.py
│   │   ├── iso20022.py
│   │   ├── json_parser.py
│   │   └── csv_parser.py
│   └── utils/
│       ├── hashing.py
│       ├── file_detection.py
│       └── reporting.py
│
├── evidence/
│   ├── original/
│   ├── processed/
│   └── reports/
│
├── output/
│
├── tests/
│
├── docs/
│   ├── architecture.md
│   ├── evidence-methodology.md
│   ├── supported-formats.md
│   └── security.md
│
├── README.md
├── LICENSE
├── requirements.txt
└── .gitignore
```

---

## 🔐 File Integrity

Each analyzed file can be fingerprinted using SHA-256.

Example:

```text
File:
transaction.xml

SHA-256:
[64-character cryptographic fingerprint]

Analysis:
Completed

Format:
XML

Evidence Status:
NOT INDEPENDENTLY VERIFIED
```

A hash can help identify whether two files have identical byte contents. A hash alone does not prove who created the file, whether a bank transmitted it, or whether the transaction represented by it occurred.

---

## 📊 Planned Report Structure

```json
{
  "project": "BANK-H2H-FORENSICS",
  "analysis_status": "COMPLETED",
  "file_name": "source_file.xml",
  "file_format": "XML",
  "sha256": "calculated-file-hash",
  "extracted_data": {
    "message_id": null,
    "transaction_reference": null,
    "amount": null,
    "currency": null,
    "bic": null
  },
  "verification": {
    "source_authenticity": "NOT_VERIFIED",
    "bank_execution": "NOT_VERIFIED",
    "settlement": "NOT_VERIFIED",
    "beneficiary_credit": "NOT_VERIFIED"
  },
  "limitations": [
    "File parsing does not independently verify bank origin.",
    "File contents do not independently establish settlement or beneficiary credit."
  ]
}
```

---

## ⚙️ Technology Stack

<p align="center">
  <img src="https://img.shields.io/badge/Python-Analysis_Engine-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/XML-lxml-00599C?style=for-the-badge">
  <img src="https://img.shields.io/badge/JSON-Data_Processing-000000?style=for-the-badge&logo=json">
  <img src="https://img.shields.io/badge/SHA256-Cryptographic_Hashing-555555?style=for-the-badge">
  <img src="https://img.shields.io/badge/Git-GitHub-F05032?style=for-the-badge&logo=git&logoColor=white">
</p>

- **Python** — analysis engine
- **lxml** — XML processing
- **JSON** — structured reporting
- **CSV** — tabular financial data analysis
- **SHA-256** — file integrity fingerprinting
- **Git & GitHub** — source control and development

---

## 🚀 Development Roadmap

### Phase 1 — Foundation

- [x] Repository initialization
- [x] Project structure
- [x] Forensic methodology
- [x] Evidence-first architecture
- [ ] Python environment setup
- [ ] File intake module
- [ ] SHA-256 hashing module

### Phase 2 — Core Parsers

- [ ] XML parser
- [ ] ISO 20022 field extraction
- [ ] SWIFT FIN parser
- [ ] JSON parser
- [ ] CSV parser
- [ ] Format detection engine

### Phase 3 — Analysis Engine

- [ ] Field consistency checks
- [ ] Message structure checks
- [ ] Reference extraction
- [ ] Amount and currency extraction
- [ ] BIC identification
- [ ] Timestamp extraction
- [ ] Warning classification

### Phase 4 — Reporting

- [ ] JSON forensic reports
- [ ] Human-readable reports
- [ ] Evidence index
- [ ] Hash manifest
- [ ] Batch report support

### Phase 5 — Advanced Features

- [ ] ISO 20022 schema validation
- [ ] Advanced FIN field parsing
- [ ] Multi-file comparison
- [ ] Transaction reference cross-comparison
- [ ] Evidence timeline
- [ ] Report export enhancements
- [ ] CLI interface improvements

---

## 🧪 Testing Philosophy

Testing should use:

- Publicly available documentation
- Authorized source files
- User-provided real files
- Clearly labeled synthetic test fixtures
- Invalid and malformed files for parser testing

Synthetic fixtures are used only for software testing and must never be presented as genuine banking evidence.

---

## ⚠️ Disclaimer

BANK-H2H-FORENSICS is an independent technical research and file-analysis project.

This project is not affiliated with, endorsed by, or officially connected to SWIFT, any bank, financial institution, payment network, clearing system, or regulatory authority.

The software analyzes file contents and technical structures. It cannot independently verify bank credentials, message authenticity, transaction execution, settlement, account balances, or beneficiary credit unless appropriate independent verification mechanisms are implemented and used.

All analysis should be conducted on files the user is authorized to access.

---

## 🤝 Contributing

Contributions, parser improvements, documentation, test cases, security reviews, and technical discussions are welcome.

1. Fork the repository.
2. Create a feature branch.
3. Implement and test your changes.
4. Submit a Pull Request.
5. Include documentation and test coverage when appropriate.

---

## 📜 License

This project is intended to be distributed under the **MIT License**.

See `LICENSE` for details.

---

## ☕ Support the Project

If this project has helped your research, learning, or security operations, consider supporting its continued development.

<div align="center">

<a href="https://www.paypal.com/paypalme/bungtempong99">
<img src="https://img.shields.io/badge/☕-Support_Development-FFDD00?style=for-the-badge&logo=buymeacoffee&logoColor=000000">
</a>

</div>

---

<p align="center">
  <b>Built for evidence-based financial file analysis.</b>
  <br>
  <i>Analyze the evidence. Verify the data. Never assume the transaction.</i>
</p>
