"""XML inspection parser with external entity processing disabled."""

from xml.etree import ElementTree as ET

from ..validation import InputValidationError


def parse_xml(path):
    try:
        with open(path, "rb") as file:
            root = ET.fromstring(file.read())
    except ET.ParseError as exc:
        raise InputValidationError(f"Invalid XML: {exc}") from exc
    except OSError as exc:
        raise InputValidationError(f"Unable to read XML file: {exc}") from exc

    def local_name(tag):
        return tag.split("}", 1)[-1] if "}" in tag else tag

    elements = []

    for element in root.iter():
        text = (element.text or "").strip()

        if text:
            elements.append(
                {
                    "tag": local_name(element.tag),
                    "text": text,
                }
            )

    return {
        "format": "XML",
        "valid": True,
        "root": local_name(root.tag),
        "element_count": sum(1 for _ in root.iter()),
        "text_elements": elements,
    }
