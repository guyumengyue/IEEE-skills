"""Generate example IEEE Transactions-ready figures."""

from __future__ import annotations

from pathlib import Path
import sys

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ieee_skills import box_plot, heatmap, line_plot, save_figure, single_line_diagram
from ieee_skills.styles import IEEEFigureSpec


def main() -> None:
    outdir = Path(__file__).resolve().parents[1] / "examples" / "outputs"
    outdir.mkdir(parents=True, exist_ok=True)

    rng = np.random.default_rng(7)
    load = pd.DataFrame(
        {
            "hour": np.tile(np.arange(24), 3),
            "load_mw": np.concatenate(
                [
                    55 + 10 * np.sin(np.linspace(0, 2 * np.pi, 24)) + rng.normal(0, 1.0, 24),
                    50 + 7 * np.sin(np.linspace(0, 2 * np.pi, 24) + 0.3) + rng.normal(0, 1.0, 24),
                    44 + 5 * np.sin(np.linspace(0, 2 * np.pi, 24) + 0.8) + rng.normal(0, 1.0, 24),
                ]
            ),
            "scenario": np.repeat(["Base", "DER-rich", "DR-enabled"], 24),
        }
    )
    spec = IEEEFigureSpec(columns=1, aspect=0.65)
    ax = line_plot(
        load,
        x="hour",
        y="load_mw",
        hue="scenario",
        columns=spec.columns,
        xlabel="Hour",
        ylabel="Load (MW)",
        title="A. Feeder load under control scenarios",
    )
    save_figure(ax.figure, outdir / "ieee_line_load", formats=spec.formats, dpi=spec.dpi)

    voltage = pd.DataFrame(
        {
            "method": np.repeat(["Base", "Volt-VAR", "OPF"], 60),
            "voltage_pu": np.concatenate(
                [
                    rng.normal(0.965, 0.018, 60),
                    rng.normal(0.982, 0.010, 60),
                    rng.normal(0.992, 0.006, 60),
                ]
            ),
        }
    )
    ax = box_plot(
        voltage,
        x="method",
        y="voltage_pu",
        xlabel="Control mode",
        ylabel="Voltage (p.u.)",
        title="B. Voltage regulation performance",
    )
    save_figure(ax.figure, outdir / "ieee_box_voltage", formats=("pdf", "svg", "png"), dpi=600)

    sensitivity = pd.DataFrame(
        rng.normal(0, 1, (5, 5)),
        index=[f"Bus {i}" for i in range(1, 6)],
        columns=[f"PV {i}" for i in range(1, 6)],
    )
    ax = heatmap(
        sensitivity,
        cbar_label="Sensitivity",
        title="C. Voltage sensitivity matrix",
        annotate=True,
    )
    save_figure(ax.figure, outdir / "ieee_heatmap_sensitivity", formats=("pdf", "svg", "png"), dpi=600)

    buses = pd.DataFrame(
        {
            "bus": [1, 2, 3, 4, 5],
            "label": ["G", "B2", "B3", "PV", "Load"],
            "x": [0, 1.2, 2.4, 2.4, 3.6],
            "y": [0, 0, 0, 0.8, 0],
            "kv": [230, 230, 115, 115, 115],
        }
    )
    branches = pd.DataFrame(
        {
            "from": [1, 2, 3, 3],
            "to": [2, 3, 4, 5],
            "loading": [0.44, 0.72, 0.88, 0.61],
            "status": [True, True, True, True],
        }
    )
    ax = single_line_diagram(buses, branches, title="D. Test feeder one-line diagram")
    save_figure(ax.figure, outdir / "ieee_single_line", formats=("pdf", "svg", "png"), dpi=600)


if __name__ == "__main__":
    main()
