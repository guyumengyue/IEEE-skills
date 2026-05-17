# IEEE Reference Style

## Core style

- Use numbered citations in square brackets.
- Order references by first citation in the manuscript.
- Use `cite` plus `IEEEtran.bst` for LaTeX/BibTeX manuscripts.
- Do not use author-year citation style.
- Do not fabricate DOI, pages, volume, issue, article number, or publisher data.

## BibTeX

Recommended LaTeX setup:

```latex
\usepackage{cite}
\bibliographystyle{IEEEtran}
\bibliography{references}
```

For IEEEtran controls:

```bibtex
@IEEEtranBSTCTL{IEEEexample:BSTcontrol,
  CTLuse_article_number = "yes",
  CTLuse_paper = "yes",
  CTLmax_names_forced_etal = "6",
  CTLnames_show_etal = "1"
}
```

## Field checks

- Article: author, title, journal, year, volume, number, pages or article number,
  and DOI when available.
- Conference: author, title, conference name, location if available, year, pages,
  and DOI when available.
- Standard: organization, standard number, title, publisher/body, and year.
- Dataset or code: creator, title, repository, version, year, and persistent
  identifier when available.
