import json
import tempfile
import unittest
from pathlib import Path

from bank_h2h_forensics.analyzer import analyze_file


class AnalyzerTests(unittest.TestCase):
    def test_json_analysis(self):
        payload = {"example": "synthetic", "amount": "10.00"}

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.json"
            path.write_text(json.dumps(payload), encoding="utf-8")

            report = analyze_file(path)

            self.assertEqual(report["source"]["detected_format"], "JSON")
            self.assertEqual(report["analysis"]["status"], "COMPLETED")
            self.assertEqual(report["analysis"]["parser_result"]["data"], payload)

    def test_unknown_file_still_hashes(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.unknown"
            path.write_bytes(b"synthetic unknown content")

            report = analyze_file(path)

            self.assertEqual(report["source"]["detected_format"], "UNKNOWN")
            self.assertTrue(report["source"]["sha256"])
            self.assertTrue(report["analysis"]["warnings"])


if __name__ == "__main__":
    unittest.main()
