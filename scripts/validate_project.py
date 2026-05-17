"""Validate the IEEE-skills repository after local edits."""

from __future__ import annotations

import importlib
import os
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run(cmd: list[str]) -> None:
    print("+", " ".join(cmd))
    env = os.environ.copy()
    env["PYTHONPATH"] = str(ROOT / "src") + os.pathsep + env.get("PYTHONPATH", "")
    subprocess.run(cmd, cwd=ROOT, check=True, env=env)


def main() -> int:
    sys.path.insert(0, str(ROOT / "src"))
    importlib.import_module("ieee_skills")

    for skill in (ROOT / "skills").glob("ieee-*"):
        run([sys.executable, r"C:\Users\38414\.codex\skills\.system\skill-creator\scripts\quick_validate.py", str(skill)])

    bst = ROOT / "assets" / "bibtex" / "IEEEtran.bst"
    if not bst.exists():
        raise FileNotFoundError("Missing bundled IEEEtran.bst")

    with tempfile.TemporaryDirectory() as td:
        output = Path(td) / "term.txt"
        sample = Path(td) / "sample.txt"
        sample.write_text("The load flow calculation uses smart grids and charging piles.", encoding="utf-8")
        run([sys.executable, "-m", "ieee_skills", "normalize", str(sample), "--output", str(output)])
        if "power flow analysis" not in output.read_text(encoding="utf-8"):
            raise RuntimeError("Terminology normalization did not run as expected.")

    run([sys.executable, "scripts/generate_examples.py"])
    expected = ROOT / "examples" / "outputs" / "ieee_line_load.pdf"
    if not expected.exists():
        raise FileNotFoundError(f"Example output not generated: {expected}")

    print("Validation complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
