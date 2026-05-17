"""Smoke-test IEEE figure generation from this repository."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from ieee_skills import line_plot, save_figure


def main() -> int:
    data = pd.DataFrame(
        {
            "hour": [0, 6, 12, 18, 24] * 2,
            "mw": [40, 48, 55, 63, 44, 37, 43, 49, 54, 40],
            "case": ["Base"] * 5 + ["Control"] * 5,
        }
    )
    ax = line_plot(data, x="hour", y="mw", hue="case", xlabel="Hour", ylabel="Load (MW)")
    save_figure(ax.figure, Path("examples/outputs/skill_smoke"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
