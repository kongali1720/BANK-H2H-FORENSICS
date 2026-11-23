"""XML inspection parser with external entity processing disabled."""

from xml.etree import ElementTree as ET


def parse_xml(path):
    parser = ET.XMLParser()

    with open(path, "rb") as file:
        root = ET.fromstring(file.read(), parser=parser)

    def local_name(tag):
        return tag.split("}", 1)[-1] if "}" in tag else tag

    elements = []

    for element in root.iter():
        text = (element.text or "").strip()

        if text:
            elements.append({
                "tag": local_name(element.tag),
                "text": text,
            })

    return {
        "format": "XML",
        "valid": True,
        "root": local_name(root.tag),
        "element_count": sum(1 for _ in root.iter()),
        "text_elements": elements,
    }
