"""IEEE-style reference helpers."""

from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class ReferenceIssue:
    label: str
    message: str


def format_ieee_reference(
    *,
    authors: str,
    title: str,
    venue: str,
    year: int | str,
    volume: str | None = None,
    number: str | None = None,
    pages: str | None = None,
    doi: str | None = None,
) -> str:
    """Format a common journal article reference in compact IEEE style."""

    parts = [f"{authors}, \"{title},\" {venue}"]
    if volume:
        parts.append(f"vol. {volume}")
    if number:
        parts.append(f"no. {number}")
    if pages:
        parts.append(f"pp. {pages}")
    parts.append(str(year))
    ref = ", ".join(parts) + "."
    if doi:
        ref += f" doi: {doi}."
    return ref


def check_bibtex_style(bibtex: str) -> list[ReferenceIssue]:
    """Run lightweight BibTeX checks for IEEE Transactions submissions."""

    issues: list[ReferenceIssue] = []
    entries = re.findall(r"@\w+\s*\{\s*([^,\s]+)", bibtex)
    if not entries:
        issues.append(ReferenceIssue("bibtex-empty", "No BibTeX entries were detected."))
        return issues

    for key in entries:
        entry_match = re.search(rf"@\w+\s*\{{\s*{re.escape(key)}\s*,(.*?)(?=\n@|\Z)", bibtex, re.S)
        body = entry_match.group(1) if entry_match else ""
        lower = body.lower()
        if "doi" not in lower and "url" in lower:
            issues.append(ReferenceIssue(key, "Prefer DOI when available; do not rely on URL alone."))
        if "title" in lower and re.search(r"title\s*=\s*\{[A-Z][^{}]*[A-Z]{2,}", body):
            issues.append(ReferenceIssue(key, "Check title capitalization; IEEEtran.bst applies sentence casing rules."))
        if "journal" in lower and "ieee trans" in lower and "." not in body:
            issues.append(ReferenceIssue(key, "Use official IEEE journal abbreviations where possible."))
    return issues


def make_bstctl_entry(key: str = "IEEEexample:BSTcontrol", *, et_al_threshold: int = 6) -> str:
    """Return an IEEEtranBSTCTL entry for IEEEtran.bst."""

    return (
        f"@IEEEtranBSTCTL{{{key},\n"
        f"  CTLuse_article_number = \"yes\",\n"
        f"  CTLuse_paper = \"yes\",\n"
        f"  CTLmax_names_forced_etal = \"{et_al_threshold}\",\n"
        f"  CTLnames_show_etal = \"1\"\n"
        f"}}\n"
    )
