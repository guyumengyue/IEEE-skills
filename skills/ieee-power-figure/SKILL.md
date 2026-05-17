---
name: ieee-power-figure
description: >-
  Create, revise, or audit IEEE PES Transactions-ready figures for power systems,
  smart grid, microgrid, DER, EV, OPF, PMU, AMI, reliability, resilience, and
  energy management papers. Use when the user asks for IEEE, TPWRS, TSG,
  Transactions on Power Systems, Transactions on Smart Grid, publication-ready
  plots, one-column or two-column figures, SVG/PDF/TIFF export, grayscale-safe
  line graphs, heatmaps, box plots, or one-line diagrams.
---

# IEEE Power Figure

Produce figures as compact engineering evidence for IEEE double-column papers.
Use the repository package `ieee_skills` when available; otherwise follow the
rules in the references.

## First move

Establish the figure contract before plotting:

1. Journal target: `TPWRS`, `TSG`, or `unspecified IEEE PES`.
2. Claim: the one sentence the figure must support.
3. Panel role: comparison, operation profile, sensitivity, topology, uncertainty,
   resilience, ablation, or case-study evidence.
4. Width: one column (`3.5 in`) or two columns (`7.16 in`).
5. Export: vector first (`PDF` or `SVG`) plus high-resolution raster when needed.
6. Accessibility: do not rely on color alone; use markers, line styles, direct
   labels, or patterns.

If the data, units, scenario definitions, or error-bar meaning are missing,
state the missing item and create a scaffold only when the user wants one.

## Python defaults

Prefer the package helpers:

```python
from ieee_skills import line_plot, box_plot, heatmap, single_line_diagram, save_figure
```

Use these defaults for hand-written matplotlib code:

```python
import matplotlib as mpl

mpl.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "Times", "DejaVu Serif"],
    "mathtext.fontset": "stix",
    "font.size": 8,
    "axes.labelsize": 8,
    "xtick.labelsize": 7,
    "ytick.labelsize": 7,
    "legend.fontsize": 7,
    "pdf.fonttype": 42,
    "ps.fonttype": 42,
    "svg.fonttype": "none",
})
```

## Chart selection

- Time series, load profiles, voltage profiles, and convergence curves:
  line plot with unique markers and line styles.
- Scenario distributions, voltage violations, loss distributions:
  box plot or violin plot with clear median and sample count.
- Sensitivity matrices, locational marginal prices, correlations, attention maps:
  perceptually ordered heatmap, preferably `cividis`, with units in the colorbar.
- Network topology, feeder layout, bus-branch case studies:
  one-line diagram with branch loading encoded by width or grayscale-safe accent.
- Reliability/resilience:
  use event timeline plus quantitative restoration or energy-not-served panel.

## Required QA

Before final delivery:

1. Confirm width is one-column or two-column IEEE size.
2. Confirm all axes include units when physical quantities are plotted.
3. Confirm line graphs are interpretable in grayscale.
4. Confirm exported text remains editable in vector files where possible.
5. Confirm raster export is at least 600 dpi for line art.
6. Confirm captions define scenarios, statistics, error bars, and sample sizes.

## When to load references

| File | Open when |
|---|---|
| `references/ieee-figure-standards.md` | Need exact IEEE graphics dimensions, formats, resolution, or accessibility rules. |
| `references/power-chart-patterns.md` | Need a chart type for TPWRS/TSG power-system evidence. |
| `references/export-qa.md` | Need pre-submission figure audit checks. |
| `references/journal-scope.md` | Need to decide whether the figure narrative fits TPWRS or TSG. |
