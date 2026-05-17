---
name: ieee-power-citation
description: >-
  Audit, format, or repair IEEE numeric citations, BibTeX files, reference
  lists, DOI metadata, IEEE journal abbreviations, and IEEEtran bibliography
  setup for IEEE Transactions on Power Systems and IEEE Transactions on Smart
  Grid manuscripts. Use when the user asks for IEEE references, IEEEtran.bst,
  BibTeX, bibliography style, citation order, DOI checks, or reference hygiene.
---

# IEEE Power Citation

Use official IEEE numeric citation practice. Prefer `IEEEtran.bst` with BibTeX
or the official IEEE reference tools when available. This skill bundles the
unmodified `IEEEtran.bst` in `assets/IEEEtran.bst` for convenience.

## Workflow

1. Identify manuscript format: LaTeX/BibTeX, Word, plain reference list, or mixed.
2. Confirm citation style: numbered IEEE bracket citations, ordered by first use.
3. Check each bibliographic record for title, author, venue, year, pages or
   article number, DOI, and official journal abbreviation.
4. Do not fabricate DOI, issue, volume, pages, article number, or publisher data.
5. Flag references that are only weak background support for the cited claim.
6. Return corrected BibTeX or a concise issue list.

## LaTeX setup

Use:

```latex
\usepackage{cite}
\bibliographystyle{IEEEtran}
\bibliography{references}
```

If a local TeX distribution lacks the style file, copy `assets/IEEEtran.bst`
beside the manuscript or install the IEEEtran package through TeX Live/MiKTeX.

## BibTeX checks

Use the repository helper when available:

```python
from ieee_skills import check_bibtex_style
issues = check_bibtex_style(open("references.bib", encoding="utf-8").read())
```

## Reference principles

- Use official IEEE journal and magazine abbreviations when possible.
- Prefer DOI over URL for formally published papers.
- Preserve capitalization in acronyms and proper nouns using braces in BibTeX
  only when needed.
- Avoid citing arXiv/preprints as the final source when an IEEE Xplore version
  exists.
- For standards, include standard number, title, publisher or standards body,
  location if known, and year.

## When to load references

| File | Open when |
|---|---|
| `references/ieee-reference-style.md` | Need IEEE citation order, reference fields, or LaTeX/BibTeX setup. |
| `references/pes-reference-checklist.md` | Auditing power systems and smart grid reference quality. |
