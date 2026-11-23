"""JSON inspection parser."""

import json

from ..validation import InputValidationError


def parse_json(path):
    try:
        with open(path, "r", encoding="utf-8-sig") as file:
            data = json.load(file)
    except json.JSONDecodeError as exc:
        raise InputValidationError(
            f"Invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}"
        ) from exc
    except UnicodeDecodeError as exc:
        raise InputValidationError("JSON input is not valid UTF-8 text.") from exc

    return {
        "format": "JSON",
        "valid": True,
        "root_type": type(data).__name__,
        "data": data,
    }
