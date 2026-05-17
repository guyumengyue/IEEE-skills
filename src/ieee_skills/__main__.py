"""Small command-line helpers for IEEE-skills."""

from __future__ import annotations

import argparse
from pathlib import Path

from .terms import normalize_terms


def main() -> int:
    parser = argparse.ArgumentParser(prog="python -m ieee_skills")
    sub = parser.add_subparsers(dest="cmd", required=True)
    norm = sub.add_parser("normalize", help="Normalize IEEE PES terminology in a text file.")
    norm.add_argument("input")
    norm.add_argument("--output")

    args = parser.parse_args()
    if args.cmd == "normalize":
        path = Path(args.input)
        text = path.read_text(encoding="utf-8")
        normalized, issues = normalize_terms(text)
        if args.output:
            Path(args.output).write_text(normalized, encoding="utf-8")
        else:
            print(normalized)
        if issues:
            print("\nIssues:")
            for issue in issues:
                print(f"- {issue.found} -> {issue.suggestion}: {issue.reason}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
