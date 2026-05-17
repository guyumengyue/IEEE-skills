"""Standalone terminology normalizer for IEEE PES manuscripts."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

REPLACEMENTS = {
    "power flow calculation": "power flow analysis",
    "load flow calculation": "power flow analysis",
    "smart grids": "smart grid",
    "micro-grid": "microgrid",
    "distribution network": "distribution system",
    "renewable energies": "renewable energy resources",
    "photovoltaics generation": "photovoltaic generation",
    "charging piles": "EV chargers",
    "optimal powerflow": "optimal power flow",
}


def normalize(text: str) -> tuple[str, list[tuple[str, str]]]:
    changes: list[tuple[str, str]] = []
    for raw, replacement in REPLACEMENTS.items():
        pattern = re.compile(rf"\b{re.escape(raw)}\b", re.IGNORECASE)
        if pattern.search(text):
            changes.append((raw, replacement))
            text = pattern.sub(replacement, text)
    return text, changes


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    parser.add_argument("--output")
    args = parser.parse_args()

    source = Path(args.input)
    text, changes = normalize(source.read_text(encoding="utf-8"))
    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
    else:
        print(text)
    if changes:
        print("\nChanges:")
        for old, new in changes:
            print(f"- {old} -> {new}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
