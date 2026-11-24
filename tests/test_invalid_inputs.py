import pytest

from bank_h2h_forensics.analyzer import analyze_file
from bank_h2h_forensics.parsers.csv_parser import parse_csv
from bank_h2h_forensics.validation import InputValidationError


def test_malformed_json_rejected(tmp_path):
    path = tmp_path / "malformed.json"
    path.write_text("{invalid json", encoding="utf-8")

    with pytest.raises(InputValidationError, match="Invalid JSON"):
        analyze_file(path)


def test_empty_json_rejected(tmp_path):
    path = tmp_path / "empty.json"
    path.write_text("", encoding="utf-8")

    with pytest.raises(InputValidationError, match="Invalid JSON"):
        analyze_file(path)


def test_malformed_xml_rejected(tmp_path):
    path = tmp_path / "malformed.xml"
    path.write_text("<root><broken></root>", encoding="utf-8")

    with pytest.raises(InputValidationError, match="Invalid XML"):
        analyze_file(path)


def test_empty_csv_rejected(tmp_path):
    path = tmp_path / "empty.csv"
    path.write_text("", encoding="utf-8")

    with pytest.raises(InputValidationError, match="missing a header"):
        parse_csv(path)


def test_csv_empty_header_rejected(tmp_path):
    path = tmp_path / "empty_header.csv"
    path.write_text("id,,amount\n1,foo,10\n", encoding="utf-8")

    with pytest.raises(InputValidationError, match="empty column"):
        parse_csv(path)


def test_csv_duplicate_header_rejected(tmp_path):
    path = tmp_path / "duplicate.csv"
    path.write_text("id,id,amount\n1,2,10\n", encoding="utf-8")

    with pytest.raises(InputValidationError, match="duplicate"):
        parse_csv(path)


def test_file_over_25mb_rejected(tmp_path):
    from bank_h2h_forensics.analyzer import MAX_FILE_SIZE

    path = tmp_path / "oversized.unknown"
    with path.open("wb") as file:
        file.truncate(MAX_FILE_SIZE + 1)

    with pytest.raises(ValueError, match="25 MB analysis limit"):
        analyze_file(path)


def test_file_exactly_25mb_accepted(tmp_path):
    from bank_h2h_forensics.analyzer import MAX_FILE_SIZE

    path = tmp_path / "limit.unknown"
    with path.open("wb") as file:
        file.truncate(MAX_FILE_SIZE)

    report = analyze_file(path)

    assert report["source"]["size_bytes"] == MAX_FILE_SIZE
    assert report["source"]["detected_format"] == "UNKNOWN"
    assert report["source"]["sha256"]
    assert report["analysis"]["status"] == "COMPLETED"
