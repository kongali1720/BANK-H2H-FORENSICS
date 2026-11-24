"""Structured evidence metadata and chain-of-custody utilities."""

import uuid
from datetime import datetime, timezone
from pathlib import Path

from .hashing import sha256_file


def utc_timestamp():
    """Return an ISO-8601 UTC timestamp."""
    return datetime.now(timezone.utc).isoformat()


def create_evidence_metadata(path, case_id=None):
    """Build metadata for a source evidence file."""
    source = Path(path)

    if not source.exists() or not source.is_file():
        raise ValueError("Evidence source must be an existing regular file.")

    stat = source.stat()
    fingerprint = sha256_file(source)
    recorded_at = utc_timestamp()

    return {
        "report_id": f"RPT-{uuid.uuid4().hex.upper()}",
        "case_id": case_id,
        "created_at_utc": recorded_at,
        "evidence": {
            "filename": source.name,
            "size_bytes": stat.st_size,
            "sha256": fingerprint,
            "integrity_algorithm": "SHA-256",
        },
        "chain_of_custody": [
            {
                "event_id": "COC-001",
                "event": "EVIDENCE_INGESTED",
                "timestamp_utc": recorded_at,
                "description": "Evidence metadata recorded at analysis intake.",
                "integrity_hash": fingerprint,
            }
        ],
    }
