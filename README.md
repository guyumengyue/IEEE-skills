# IEEE-skills

IEEE-skills is a source-grounded skill and plotting library for manuscripts
targeting IEEE Transactions on Power Systems (TPWRS) and IEEE Transactions on
Smart Grid (TSG). It is inspired by the modular idea of
[nature-skills](https://github.com/Yuan1z0825/nature-skills): each skill is a
self-contained instruction bundle, and reusable scripts turn journal rules into
repeatable outputs.

This repository is a creative IEEE PES adaptation, not a rename of the Nature
project. The visual language is denser, more conservative, and tuned for
two-column engineering papers: one-column and two-column graphics, grayscale-safe
line styles, Times-compatible typography, vector-first export, and explicit
power-system terminology checks.

## What is included

| Component | Purpose |
|---|---|
| `skills/ieee-power-figure` | Codex/agent workflow for IEEE-ready power and smart-grid figures. |
| `skills/ieee-power-writing` | Manuscript section drafting and revision for TPWRS/TSG. |
| `skills/ieee-power-citation` | IEEE numeric citation and BibTeX hygiene workflow. |
| `skills/ieee-power-terminology` | Power systems and smart grid terminology normalization. |
| `src/ieee_skills` | Python plotting, export, reference, and terminology utilities. |
| `assets/latex/ieee-pes-template.tex` | Minimal IEEEtran manuscript scaffold. |
| `assets/bibtex/IEEEtran.bst` | Bundled unmodified IEEEtran BibTeX style under LPPL. |

## IEEE source basis

The implemented defaults are grounded in current official IEEE/PES pages checked
on 2026-05-17:

- IEEE PES author information says Transactions papers are limited to 10 pages
  at submission; accepted papers submitted on or after 2024-01-01 incur
  overlength charges beyond 12 published pages; abstracts should be about
  150-200 words, self-contained, and avoid abbreviations, footnotes, references,
  displayed equations, and tables.
- IEEE PES preparation guidance points authors to Part 4 of the Author's Kit for
  equations, units, figures, tables, references, abbreviations, acronyms, and
  biographies, and encourages LaTeX for math-heavy papers.
- IEEE Author Center graphics guidance recommends vector formats where possible,
  accepts PS, EPS, PDF, PNG, and TIFF, requires embedded fonts, and gives standard
  graphic widths of 3.5 in for one column and 7.16 in for two columns.
- IEEE Author Center accessibility guidance says line graphs should remain
  interpretable in grayscale and should use both color and shape, with thick
  lines, unique data symbols, and direct labels when helpful.
- TPWRS scope emphasizes power system analysis, computing and economics, dynamic
  performance, operations, planning and implementation, and power engineering
  education.
- TSG scope emphasizes microgrids, active distribution networks, DER and EV grid
  integration, AMI, distribution PMU applications, cyber-physical security,
  transactive energy, and data analytics for microgrids and ADNs. It explicitly
  marks several transmission-system-only topics as out of scope.

Official links:

- [IEEE PES Author Information](https://ieee-pes.org/publications/authors-kit/information-for-authors-of-ieee-power-energy-society-transactions-papers/)
- [IEEE PES Preparation and Submission](https://ieee-pes.org/publications/authors-kit/preparation-and-submission-of-transactions-papers/)
- [IEEE Transactions on Power Systems](https://ieee-pes.org/publications/transactions-on-power-systems/)
- [IEEE Transactions on Smart Grid](https://ieee-pes.org/publications/transactions-on-smart-grid/)
- [IEEE Author Center: Create Graphics](https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/create-graphics-for-your-article/)
- [IEEE Author Center: Resolution and Size](https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/create-graphics-for-your-article/resolution-and-size/)
- [IEEE Author Center: File Formatting](https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/create-graphics-for-your-article/file-formatting/)
- [IEEE Article Templates](https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/authoring-tools-and-templates/tools-for-ieee-authors/ieee-article-templates/)
- [IEEE Editorial Style Manual page](https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/create-the-text-of-your-article/ieee-editorial-style-manual/)

## Install

```bash
git clone https://github.com/guyumengyue/IEEE-skills.git
cd IEEE-skills
python -m pip install -e .
```

Install the skills into Codex:

```powershell
mkdir $env:USERPROFILE\.codex\skills -Force
Copy-Item -Recurse .\skills\ieee-* $env:USERPROFILE\.codex\skills\
```

Restart Codex after copying skills.

## Quick plotting example

```python
import pandas as pd
from ieee_skills import line_plot, save_figure

df = pd.DataFrame({
    "hour": [0, 6, 12, 18, 24] * 2,
    "load_mw": [42, 50, 58, 66, 45, 39, 46, 52, 57, 41],
    "case": ["Base"] * 5 + ["DR-enabled"] * 5,
})

ax = line_plot(df, x="hour", y="load_mw", hue="case",
               xlabel="Hour", ylabel="Load (MW)")
save_figure(ax.figure, "figures/feeder_load")
```

This writes vector-first `PDF` and `SVG` plus high-resolution `PNG` and `TIFF`
fallbacks. Default dimensions follow IEEE one-column graphics unless a
two-column figure is requested.

## Validation

```bash
python scripts/validate_project.py
```

The validator checks skill metadata, imports the Python package, runs terminology
normalization, and generates example figures in `examples/outputs/`.

## Mapping from nature-skills to IEEE-skills

| Nature-skills idea | IEEE-skills adaptation |
|---|---|
| Figure contract before plotting | Claim, panel role, IEEE width, export format, grayscale readability. |
| Nature-style visual polish | Dense two-column engineering plots with conservative typography and line weights. |
| Modular `SKILL.md` plus references | Four IEEE PES skills with scoped references and scripts. |
| Citation support | IEEE numeric citation hygiene, IEEEtran BibTeX, DOI and abbreviation checks. |
| Writing/polishing | TPWRS/TSG abstract, introduction, method, result, conclusion, and scope checks. |
| Data/source grounding | Journal-scope mapping for TPWRS versus TSG and official IEEE/PES source basis. |

## Journal-specific stance

Use TPWRS defaults for transmission and distribution analysis, dynamic
performance, operations, planning, reliability, resilience, economics, and
education. Use TSG defaults for active distribution networks, microgrids, DER/EV
integration, AMI, distribution PMU applications, cyber-physical security,
transactive energy, and data analytics tied to smart-grid operation.

When a topic sits near the boundary, the skills require an explicit scope note
instead of silently forcing a journal match.
