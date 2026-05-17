"""Common IEEE PES plotting patterns."""

from __future__ import annotations

from collections.abc import Sequence
from itertools import cycle
from typing import Any

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from .styles import IEEE_PALETTE, LINE_STYLES, MARKERS, figure_size, style_context


def _get_ax(ax=None, *, columns: int = 1, aspect: float = 0.62):
    if ax is not None:
        return ax
    _, axis = plt.subplots(figsize=figure_size(columns=columns, aspect=aspect))
    return axis


def _finish_axis(ax, xlabel: str | None, ylabel: str | None, title: str | None, grid: str | None):
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)
    if title:
        ax.set_title(title, loc="left", fontweight="bold", pad=3)
    if grid == "y":
        ax.grid(axis="y")
    elif grid == "x":
        ax.grid(axis="x")
    elif grid == "both":
        ax.grid(True)
    return ax


def line_plot(
    data: pd.DataFrame,
    *,
    x: str,
    y: str,
    hue: str | None = None,
    ax=None,
    columns: int = 1,
    xlabel: str | None = None,
    ylabel: str | None = None,
    title: str | None = None,
    direct_label: bool = False,
    grid: str | None = "y",
):
    """Draw a grayscale-safe IEEE line plot with markers and line styles."""

    with style_context():
        ax = _get_ax(ax, columns=columns)
        colors = cycle(IEEE_PALETTE.values())
        linestyles = cycle(LINE_STYLES)
        markers = cycle(MARKERS)

        if hue:
            grouped = data.groupby(hue, sort=False)
            for label, group in grouped:
                group = group.sort_values(x)
                color = next(colors)
                ax.plot(
                    group[x],
                    group[y],
                    label=str(label),
                    color=color,
                    linestyle=next(linestyles),
                    marker=next(markers),
                    markerfacecolor="white",
                    markeredgewidth=0.8,
                )
                if direct_label and len(group):
                    ax.annotate(
                        str(label),
                        xy=(group[x].iloc[-1], group[y].iloc[-1]),
                        xytext=(3, 0),
                        textcoords="offset points",
                        va="center",
                        fontsize=7,
                        color=color,
                    )
            if hue and not direct_label:
                ax.legend(ncols=1, loc="best")
        else:
            group = data.sort_values(x)
            ax.plot(
                group[x],
                group[y],
                color=IEEE_PALETTE["blue"],
                marker="o",
                markerfacecolor="white",
                markeredgewidth=0.8,
            )

        return _finish_axis(ax, xlabel or x, ylabel or y, title, grid)


def box_plot(
    data: pd.DataFrame,
    *,
    x: str,
    y: str,
    ax=None,
    columns: int = 1,
    xlabel: str | None = None,
    ylabel: str | None = None,
    title: str | None = None,
    grid: str | None = "y",
):
    """Draw a compact IEEE box plot with visible medians and muted fills."""

    with style_context():
        ax = _get_ax(ax, columns=columns)
        categories = list(pd.unique(data[x]))
        values = [data.loc[data[x] == cat, y].dropna().to_numpy() for cat in categories]
        bp = ax.boxplot(
            values,
            labels=categories,
            patch_artist=True,
            widths=0.55,
            showfliers=False,
            medianprops={"color": "black", "linewidth": 1.0},
            boxprops={"linewidth": 0.7},
            whiskerprops={"linewidth": 0.7},
            capprops={"linewidth": 0.7},
        )
        fill_cycle = cycle(["#D9E8F5", "#F7E0C7", "#DCEFE5", "#E9E0F0"])
        for patch in bp["boxes"]:
            patch.set_facecolor(next(fill_cycle))
            patch.set_edgecolor("#222222")
        return _finish_axis(ax, xlabel or x, ylabel or y, title, grid)


def heatmap(
    matrix: pd.DataFrame | np.ndarray,
    *,
    ax=None,
    columns: int = 1,
    xlabels: Sequence[str] | None = None,
    ylabels: Sequence[str] | None = None,
    cmap: str = "cividis",
    cbar_label: str | None = None,
    annotate: bool = False,
    fmt: str = ".2g",
    title: str | None = None,
):
    """Draw a perceptually ordered heatmap suitable for print and color-blind readers."""

    with style_context():
        ax = _get_ax(ax, columns=columns, aspect=0.78)
        if isinstance(matrix, pd.DataFrame):
            values = matrix.to_numpy()
            xlabels = xlabels or [str(c) for c in matrix.columns]
            ylabels = ylabels or [str(i) for i in matrix.index]
        else:
            values = np.asarray(matrix)

        im = ax.imshow(values, cmap=cmap, aspect="auto")
        if xlabels is not None:
            ax.set_xticks(np.arange(len(xlabels)), labels=xlabels, rotation=35, ha="right")
        if ylabels is not None:
            ax.set_yticks(np.arange(len(ylabels)), labels=ylabels)
        if annotate:
            midpoint = np.nanmean(values)
            for i in range(values.shape[0]):
                for j in range(values.shape[1]):
                    color = "white" if values[i, j] > midpoint else "black"
                    ax.text(j, i, format(values[i, j], fmt), ha="center", va="center", fontsize=6, color=color)
        cbar = ax.figure.colorbar(im, ax=ax, fraction=0.046, pad=0.03)
        if cbar_label:
            cbar.set_label(cbar_label)
        return _finish_axis(ax, None, None, title, None)


def single_line_diagram(
    buses: pd.DataFrame,
    branches: pd.DataFrame,
    *,
    ax=None,
    columns: int = 2,
    title: str | None = None,
):
    """Draw a publication-oriented power-system one-line diagram.

    `buses` should contain `bus` plus optional `x`, `y`, `label`, and `kv`.
    `branches` should contain `from` and `to` plus optional `loading` and `status`.
    """

    with style_context():
        ax = _get_ax(ax, columns=columns, aspect=0.45)
        buses = buses.copy()
        if "x" not in buses or "y" not in buses:
            buses["x"] = np.arange(len(buses))
            buses["y"] = 0.0
        coords: dict[Any, tuple[float, float]] = {
            row["bus"]: (float(row["x"]), float(row["y"])) for _, row in buses.iterrows()
        }

        for _, branch in branches.iterrows():
            p0 = coords[branch["from"]]
            p1 = coords[branch["to"]]
            loading = float(branch.get("loading", 0.55))
            status = bool(branch.get("status", True))
            color = IEEE_PALETTE["orange"] if loading >= 0.85 else IEEE_PALETTE["gray"]
            ax.plot(
                [p0[0], p1[0]],
                [p0[1], p1[1]],
                color=color,
                linewidth=0.8 + 1.2 * min(max(loading, 0.0), 1.0),
                linestyle="-" if status else "--",
                zorder=1,
            )

        for _, bus in buses.iterrows():
            x0, y0 = coords[bus["bus"]]
            label = str(bus.get("label", bus["bus"]))
            kv = bus.get("kv", None)
            ax.scatter([x0], [y0], s=36, color="white", edgecolor=IEEE_PALETTE["blue"], linewidth=1.0, zorder=2)
            suffix = f" ({int(kv)} kV)" if pd.notna(kv) else ""
            ax.annotate(f"{label}{suffix}", (x0, y0), xytext=(0, 6), textcoords="offset points", ha="center", fontsize=7)

        ax.set_aspect("equal", adjustable="datalim")
        ax.axis("off")
        if title:
            ax.set_title(title, loc="left", fontweight="bold", pad=3)
        return ax
