import json

from bank_h2h_forensics.cli import main


def test_cli_invalid_json_returns_error(tmp_path, monkeypatch, capsys):
    path = tmp_path / "invalid.json"
    path.write_text("{broken", encoding="utf-8")

    monkeypatch.setattr(
        "sys.argv",
        ["bank-h2h-forensics", str(path)]
    )

    exit_code = main()
    captured = capsys.readouterr()

    assert exit_code == 1
    assert "[ERROR]" in captured.err
    assert "Invalid JSON" in captured.err
    assert captured.out == ""


def test_cli_valid_json_returns_success(tmp_path, monkeypatch, capsys):
    path = tmp_path / "valid.json"
    path.write_text(
        json.dumps({"status": "test"}),
        encoding="utf-8"
    )

    monkeypatch.setattr(
        "sys.argv",
        ["bank-h2h-forensics", str(path)]
    )

    exit_code = main()
    captured = capsys.readouterr()

    assert exit_code == 0
    assert captured.err == ""
    assert '"status": "COMPLETED"' in captured.out
