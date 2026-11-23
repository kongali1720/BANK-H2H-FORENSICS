"""JSON inspection parser."""

import json


def parse_json(path):
    with open(path, "r", encoding="utf-8-sig") as file:
        data = json.load(file)

    return {
        "format": "JSON",
        "valid": True,
        "root_type": type(data).__name__,
        "data": data,
    }
