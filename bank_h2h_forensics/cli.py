"""Command-line interface."""

import argparse
import json
import sys

from .analyzer import analyze_file
from .reporter import write_json_report


def main():
    parser = argparse.ArgumentParser(
        prog="bank-h2h-forensics",
        description="Financial file inspection and evidence analysis toolkit",
    )

    parser.add_argument(
        "file",
        help="Path to a JSON, CSV, XML, or SWIFT-like text file",
    )

    parser.add_argument(
        "--output",
        "-o",
        help="Optional JSON report output path",
    )

    args = parser.parse_args()

    try:
        report = analyze_file(args.file)

        if args.output:
            destination = write_json_report(report, args.output)
            print(f"[+] Report saved: {destination}")

        print(json.dumps(report, indent=2, ensure_ascii=False))

    except Exception as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
