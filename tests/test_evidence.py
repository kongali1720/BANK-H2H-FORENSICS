import hashlib
import tempfile
import unittest
from datetime import datetime
from pathlib import Path

from bank_h2h_forensics.evidence import create_evidence_metadata


class EvidenceTests(unittest.TestCase):
    def test_metadata_contains_valid_sha256(self):
        payload = b"SYNTHETIC-EVIDENCE-TEST"

        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "evidence.txt"
            path.write_bytes(payload)

            metadata = create_evidence_metadata(path, case_id="CASE-001")

            expected_hash = hashlib.sha256(payload).hexdigest()

            self.assertEqual(metadata["case_id"], "CASE-001")
            self.assertEqual(metadata["evidence"]["sha256"], expected_hash)
            self.assertEqual(metadata["evidence"]["size_bytes"], len(payload))
            self.assertEqual(
                metadata["evidence"]["integrity_algorithm"],
                "SHA-256",
            )

    def test_report_id_is_generated(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.txt"
            path.write_text("synthetic", encoding="utf-8")

            first = create_evidence_metadata(path)
            second = create_evidence_metadata(path)

            self.assertTrue(first["report_id"].startswith("RPT-"))
            self.assertNotEqual(first["report_id"], second["report_id"])

    def test_timestamps_are_utc_aware(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.txt"
            path.write_text("synthetic", encoding="utf-8")

            metadata = create_evidence_metadata(path)

            timestamp = datetime.fromisoformat(
                metadata["created_at_utc"]
            )

            self.assertIsNotNone(timestamp.tzinfo)
            self.assertEqual(timestamp.utcoffset().total_seconds(), 0)

    def test_chain_of_custody_initial_event(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.txt"
            payload = b"synthetic custody evidence"
            path.write_bytes(payload)

            metadata = create_evidence_metadata(path)
            event = metadata["chain_of_custody"][0]

            self.assertEqual(event["event_id"], "COC-001")
            self.assertEqual(event["event"], "EVIDENCE_INGESTED")
            self.assertEqual(
                event["integrity_hash"],
                hashlib.sha256(payload).hexdigest(),
            )

    def test_missing_source_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "missing.txt"

            with self.assertRaises(ValueError):
                create_evidence_metadata(path)



    def test_metadata_and_custody_share_timestamp(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sample.txt"
            path.write_text("synthetic", encoding="utf-8")

            metadata = create_evidence_metadata(path)
            event = metadata["chain_of_custody"][0]

            self.assertEqual(
                metadata["created_at_utc"],
                event["timestamp_utc"],
            )

if __name__ == "__main__":
    unittest.main()
