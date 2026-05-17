---
name: ieee-power-terminology
description: >-
  Normalize terminology, acronyms, units, and journal-scope wording for IEEE PES
  power systems and smart grid manuscripts. Use for TPWRS/TSG papers involving
  OPF, power flow, DER, EV, PMU, AMI, microgrids, active distribution networks,
  demand response, reliability, resilience, and cyber-physical power systems.
---

# IEEE Power Terminology

Use this skill before manuscript polishing, figure captions, keywords, and final
submission checks. The goal is not to homogenize every phrase; it is to remove
ambiguous, local, or nonstandard wording that can distract IEEE reviewers.

## Workflow

1. Identify target journal: TPWRS, TSG, or general IEEE PES.
2. Scan for acronym definitions on first use.
3. Normalize common power-engineering terms conservatively.
4. Check that smart-grid language is tied to microgrids, ADNs, DER/EV
   integration, AMI, distribution PMUs, cyber-physical security, or data
   analytics when targeting TSG.
5. Preserve author-specific notation unless it conflicts with standard usage.
6. Return revised text plus an audit list of replacements.

## Common replacements

| Avoid | Prefer |
|---|---|
| load flow calculation | power flow analysis |
| micro-grid | microgrid |
| charging piles | EV chargers |
| renewable energies | renewable energy resources |
| optimal powerflow | optimal power flow |
| distribution network | distribution system |

## Script

For plain text files inside the repository:

```bash
python -m ieee_skills normalize draft.txt --output draft.normalized.txt
```

If the package is not installed, use `scripts/normalize_terms.py` for a small
standalone fallback.

## When to load references

| File | Open when |
|---|---|
| `references/term-map.md` | Need preferred terms, acronyms, and replacements. |
| `references/journal-scope.md` | Need TPWRS/TSG scope wording or boundary checks. |
