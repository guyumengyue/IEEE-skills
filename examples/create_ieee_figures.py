"""Minimal example for IEEE-skills plotting helpers."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from ieee_skills import line_plot, save_figure


data = pd.DataFrame(
    {
        "hour": [0, 6, 12, 18, 24] * 2,
        "load_mw": [42, 50, 58, 66, 45, 39, 46, 52, 57, 41],
        "case": ["Base"] * 5 + ["DR-enabled"] * 5,
    }
)

ax = line_plot(
    data,
    x="hour",
    y="load_mw",
    hue="case",
    xlabel="Hour",
    ylabel="Load (MW)",
    title="Feeder loading profile",
)
save_figure(ax.figure, Path("examples/outputs/minimal_line"))
