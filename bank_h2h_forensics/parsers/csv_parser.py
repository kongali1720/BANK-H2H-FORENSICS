"""CSV inspection parser."""

import csv

from ..validation import InputValidationError


def parse_csv(path):
    try:
        with open(path, encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)
            headers = reader.fieldnames

            if not headers:
                raise InputValidationError("CSV is empty or missing a header row.")

            if any(not header.strip() for header in headers):
                raise InputValidationError("CSV contains an empty column name.")

            if len(headers) != len(set(headers)):
                raise InputValidationError("CSV contains duplicate column names.")

            rows = list(reader)

    except UnicodeDecodeError as exc:
        raise InputValidationError("CSV input is not valid UTF-8 text.") from exc

    return {
        "format": "CSV",
        "valid": True,
        "columns": headers,
        "row_count": len(rows),
        "data": rows,
    }
