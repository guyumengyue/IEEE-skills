"""Matplotlib defaults for IEEE PES Transactions figures."""

from __future__ import annotations

from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import matplotlib as mpl
import matplotlib.pyplot as plt

IEEE_COLUMN_WIDTH_IN = 3.5
IEEE_TEXT_WIDTH_IN = 7.16
IEEE_MIN_RASTER_DPI = 600

IEEE_BLUE = "#0057A8"
IEEE_PALETTE = {
    "blue": "#0057A8",
    "orange": "#D55E00",
    "green": "#009E73",
    "sky": "#56B4E9",
    "purple": "#7B3294",
    "vermillion": "#CC3311",
    "gray": "#5F6368",
    "black": "#111111",
}

LINE_STYLES = ["-", "--", "-.", ":"]
MARKERS = ["o", "s", "^", "D", "v", "P", "X", "*"]


@dataclass(frozen=True)
class IEEEFigureSpec:
    """Export contract for an IEEE journal figure."""

    columns: int = 1
    aspect: float = 0.62
    height: float | None = None
    dpi: int = IEEE_MIN_RASTER_DPI
    formats: tuple[str, ...] = ("pdf", "svg", "png", "tiff")

    @property
    def width(self) -> float:
        return IEEE_COLUMN_WIDTH_IN if self.columns == 1 else IEEE_TEXT_WIDTH_IN

    @property
    def size(self) -> tuple[float, float]:
        return figure_size(self.columns, self.aspect, self.height)


def figure_size(columns: int = 1, aspect: float = 0.62, height: float | None = None) -> tuple[float, float]:
    """Return IEEE one-column or two-column figure size in inches."""

    if columns not in (1, 2):
        raise ValueError("columns must be 1 or 2")
    width = IEEE_COLUMN_WIDTH_IN if columns == 1 else IEEE_TEXT_WIDTH_IN
    return width, height if height is not None else width * aspect


def rc_params(base_font_size: float = 8.0) -> dict[str, object]:
    """Return rcParams tuned for compact IEEE double-column pages."""

    return {
        "font.family": "serif",
        "font.serif": ["Times New Roman", "Times", "DejaVu Serif"],
        "mathtext.fontset": "stix",
        "font.size": base_font_size,
        "axes.labelsize": base_font_size,
        "axes.titlesize": base_font_size,
        "axes.linewidth": 0.6,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "xtick.labelsize": base_font_size - 1,
        "ytick.labelsize": base_font_size - 1,
        "xtick.major.width": 0.6,
        "ytick.major.width": 0.6,
        "xtick.major.size": 3,
        "ytick.major.size": 3,
        "legend.fontsize": base_font_size - 1,
        "legend.frameon": False,
        "legend.handlelength": 1.8,
        "lines.linewidth": 1.25,
        "lines.markersize": 4,
        "patch.linewidth": 0.6,
        "grid.linewidth": 0.35,
        "grid.alpha": 0.35,
        "figure.dpi": 300,
        "savefig.dpi": IEEE_MIN_RASTER_DPI,
        "savefig.bbox": "tight",
        "savefig.pad_inches": 0.02,
        "pdf.fonttype": 42,
        "ps.fonttype": 42,
        "svg.fonttype": "none",
        "axes.prop_cycle": mpl.cycler(
            color=[
                IEEE_PALETTE["blue"],
                IEEE_PALETTE["orange"],
                IEEE_PALETTE["green"],
                IEEE_PALETTE["purple"],
                IEEE_PALETTE["sky"],
                IEEE_PALETTE["gray"],
            ]
        ),
    }


def set_ieee_style(base_font_size: float = 8.0) -> None:
    """Apply IEEE plotting defaults globally."""

    mpl.rcParams.update(rc_params(base_font_size=base_font_size))


@contextmanager
def style_context(base_font_size: float = 8.0):
    """Temporarily apply IEEE plotting defaults."""

    with mpl.rc_context(rc=rc_params(base_font_size=base_font_size)):
        yield


def save_figure(
    fig: mpl.figure.Figure,
    path: str | Path,
    *,
    formats: Iterable[str] = ("pdf", "svg", "png", "tiff"),
    dpi: int = IEEE_MIN_RASTER_DPI,
    transparent: bool = False,
) -> list[Path]:
    """Save vector-first IEEE graphics plus high-resolution raster fallbacks."""

    base = Path(path)
    base.parent.mkdir(parents=True, exist_ok=True)
    if base.suffix:
        base = base.with_suffix("")

    outputs: list[Path] = []
    for fmt in formats:
        suffix = fmt.lower().lstrip(".")
        out = base.with_suffix(f".{suffix}")
        kwargs = {"bbox_inches": "tight", "transparent": transparent}
        if suffix in {"png", "tif", "tiff", "jpg", "jpeg"}:
            kwargs["dpi"] = dpi
        fig.savefig(out, **kwargs)
        outputs.append(out)
    return outputs


def audit_figure(fig: mpl.figure.Figure, *, intended_columns: int = 1) -> list[str]:
    """Return human-readable checks for IEEE figure readiness."""

    messages: list[str] = []
    width, height = fig.get_size_inches()
    target_width = IEEE_COLUMN_WIDTH_IN if intended_columns == 1 else IEEE_TEXT_WIDTH_IN
    if abs(width - target_width) > 0.15:
        messages.append(
            f"Figure width is {width:.2f} in; expected about {target_width:.2f} in "
            f"for {intended_columns}-column IEEE graphics."
        )
    if height <= 0 or width <= 0:
        messages.append("Figure size is invalid.")

    for ax in fig.axes:
        if ax.get_xlabel() and ax.xaxis.label.get_fontsize() < 7:
            messages.append("X-axis label font size is below 7 pt.")
        if ax.get_ylabel() and ax.yaxis.label.get_fontsize() < 7:
            messages.append("Y-axis label font size is below 7 pt.")
        for label in ax.get_xticklabels() + ax.get_yticklabels():
            if label.get_text() and label.get_fontsize() < 6:
                messages.append("Tick label font size is below 6 pt.")
                break
    return messages
