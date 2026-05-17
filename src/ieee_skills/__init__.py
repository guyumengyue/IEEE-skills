"""IEEE PES Transactions-ready plotting and manuscript utilities."""

from .plots import box_plot, heatmap, line_plot, single_line_diagram
from .references import check_bibtex_style, format_ieee_reference, make_bstctl_entry
from .styles import (
    IEEE_COLUMN_WIDTH_IN,
    IEEE_TEXT_WIDTH_IN,
    IEEEFigureSpec,
    audit_figure,
    figure_size,
    save_figure,
    set_ieee_style,
    style_context,
)
from .terms import find_term_issues, normalize_terms

__all__ = [
    "IEEE_COLUMN_WIDTH_IN",
    "IEEE_TEXT_WIDTH_IN",
    "IEEEFigureSpec",
    "audit_figure",
    "box_plot",
    "check_bibtex_style",
    "figure_size",
    "find_term_issues",
    "format_ieee_reference",
    "heatmap",
    "line_plot",
    "make_bstctl_entry",
    "normalize_terms",
    "save_figure",
    "set_ieee_style",
    "single_line_diagram",
    "style_context",
]
