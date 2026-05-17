"""Terminology normalization for IEEE PES power and smart grid manuscripts."""

from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class TermIssue:
    found: str
    suggestion: str
    reason: str
    start: int
    end: int


REPLACEMENTS = {
    "power flow calculation": ("power flow analysis", "Use the standard analytical term."),
    "load flow calculation": ("power flow analysis", "Use current IEEE-style terminology."),
    "smart grids": ("smart grid", "Use singular adjectival form before a noun."),
    "micro-grid": ("microgrid", "Use the closed compound common in IEEE PES venues."),
    "distribution network": ("distribution system", "Use system when discussing electric power operation."),
    "renewable energies": ("renewable energy resources", "Use resource-focused terminology."),
    "photovoltaics generation": ("photovoltaic generation", "Use adjectival photovoltaic."),
    "charging piles": ("EV chargers", "Use internationally readable EV terminology."),
    "optimal powerflow": ("optimal power flow", "Keep OPF expanded form spaced."),
    "state estimation algorithm": ("state estimator", "Prefer concise technical noun when appropriate."),
}

ACRONYMS = {
    "ADN": "active distribution network",
    "AMI": "advanced metering infrastructure",
    "BESS": "battery energy storage system",
    "DER": "distributed energy resource",
    "DERs": "distributed energy resources",
    "DR": "demand response",
    "DSM": "demand-side management",
    "EV": "electric vehicle",
    "OPF": "optimal power flow",
    "PMU": "phasor measurement unit",
    "RES": "renewable energy source",
    "TSO": "transmission system operator",
    "WAMS": "wide-area measurement system",
    "WACS": "wide-area control system",
}


def find_term_issues(text: str) -> list[TermIssue]:
    """Find terminology that should be normalized before IEEE submission."""

    issues: list[TermIssue] = []
    for raw, (suggestion, reason) in REPLACEMENTS.items():
        pattern = re.compile(rf"\b{re.escape(raw)}\b", re.IGNORECASE)
        for match in pattern.finditer(text):
            issues.append(TermIssue(match.group(0), suggestion, reason, match.start(), match.end()))
    return sorted(issues, key=lambda item: item.start)


def normalize_terms(text: str) -> tuple[str, list[TermIssue]]:
    """Apply conservative terminology replacements and return an audit trail."""

    issues = find_term_issues(text)
    normalized = text
    for issue in reversed(issues):
        normalized = normalized[: issue.start] + issue.suggestion + normalized[issue.end :]
    return normalized, issues


def acronym_expansion(acronym: str) -> str | None:
    """Return the preferred IEEE PES expansion for a common acronym."""

    return ACRONYMS.get(acronym)
