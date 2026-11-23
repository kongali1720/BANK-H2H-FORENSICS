"""JSON report writer."""

import json
from pathlib import Path


def write_json_report(report, output_path):
    destination = Path(output_path)
    destination.parent.mkdir(parents=True, exist_ok=True)

    with open(destination, "w", encoding="utf-8") as file:
        json.dump(report, file, indent=2, ensure_ascii=False)

    return destination
