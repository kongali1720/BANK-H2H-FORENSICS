"""Basic SWIFT FIN structural inspection."""

import re

FIN_TAG_PATTERN = re.compile(r"(?m)^:(\d{2}[A-Z]?):")


def parse_swift(path):
    with open(path, encoding="utf-8-sig", errors="replace") as file:
        content = file.read()

    tags = FIN_TAG_PATTERN.findall(content)

    message_types = re.findall(r"\{2:[A-Z0-9]{4}", content)

    normalized_types = [match.replace("{2:", "") for match in message_types]

    return {
        "format": "SWIFT_FIN_TEXT",
        "valid": bool(content.strip()),
        "character_count": len(content),
        "tag_count": len(tags),
        "tags": tags,
        "message_type_candidates": normalized_types,
        "warning": (
            "Structural text inspection only. "
            "This does not authenticate a SWIFT message or confirm a transaction."
        ),
    }
