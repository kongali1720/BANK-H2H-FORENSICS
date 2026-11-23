"""Main financial file analysis engine."""

from pathlib import Path
from datetime import datetime, timezone

from .detector import detect_format
from .hashing import sha256_file
from .parsers.json_parser import parse_json
from .parsers.csv_parser import parse_csv
from .parsers.xml_parser import parse_xml
from .parsers.swift_parser import parse_swift

MAX_FILE_SIZE = 25 * 1024 * 1024


def analyze_file(path):
    source = Path(path)

    if not source.exists():
        raise FileNotFoundError(f"File not found: {source}")

    if not source.is_file():
        raise ValueError("Input must be a regular file.")

    size = source.stat().st_size

    if size > MAX_FILE_SIZE:
        raise ValueError("File exceeds the 25 MB analysis limit.")

    detected = detect_format(source)
    parsed = None
    warnings = []

    if detected == "JSON":
        parsed = parse_json(source)
    elif detected == "CSV":
        parsed = parse_csv(source)
    elif detected == "XML":
        parsed = parse_xml(source)
    elif detected == "SWIFT_OR_TEXT":
        parsed = parse_swift(source)
        warnings.append(
            "SWIFT detection is heuristic and does not authenticate a message."
        )
    else:
        warnings.append(
            "Unsupported format. Metadata and SHA-256 only."
        )

    report = {
        "tool": "BANK-H2H-FORENSICS",
        "version": "0.1.0",
        "analysis_timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "source": {
            "filename": source.name,
            "size_bytes": size,
            "detected_format": detected,
            "sha256": sha256_file(source),
        },
        "analysis": {
            "status": "COMPLETED",
            "parser_result": parsed,
            "warnings": warnings,
        },
        "limitations": [
            "File analysis does not authenticate the source institution.",
            "A file hash does not prove the truth of file contents.",
            "Parsing does not prove payment execution or settlement.",
            "Funds availability must be independently confirmed.",
        ],
    }

    return report
