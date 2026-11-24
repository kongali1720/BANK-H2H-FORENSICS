"""File format detection."""

from pathlib import Path


def detect_format(path):
    suffix = Path(path).suffix.lower()

    if suffix == ".json":
        return "JSON"

    if suffix == ".csv":
        return "CSV"

    if suffix in (".xml",):
        return "XML"

    if suffix in (".txt", ".fin", ".swift"):
        return "SWIFT_OR_TEXT"

    return "UNKNOWN"
