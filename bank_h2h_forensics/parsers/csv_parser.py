"""CSV inspection parser."""

import csv


def parse_csv(path):
    with open(path, "r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    return {
        "format": "CSV",
        "valid": True,
        "columns": reader.fieldnames or [],
        "row_count": len(rows),
        "data": rows,
    }
