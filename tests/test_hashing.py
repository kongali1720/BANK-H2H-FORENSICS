import hashlib
import tempfile
import unittest
from pathlib import Path

from bank_h2h_forensics.hashing import sha256_file


class HashingTests(unittest.TestCase):
    def test_hash_matches_standard_sha256(self):
        payload = b"BANK-H2H-FORENSICS-TEST"

        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "sample.bin"
            path.write_bytes(payload)

            expected = hashlib.sha256(payload).hexdigest()
            actual = sha256_file(path)

            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
