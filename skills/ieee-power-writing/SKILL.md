---
name: ieee-power-writing
description: >-
  Draft, restructure, or polish IEEE PES Transactions manuscript text for IEEE
  Transactions on Power Systems and IEEE Transactions on Smart Grid. Use for
  abstracts, introductions, methods, results, conclusions, titles, keywords,
  response-aware revisions, scope checks, contribution framing, and Chinese to
  English academic writing in power systems, smart grid, microgrid, DER, EV,
  OPF, PMU, AMI, reliability, and resilience papers.
---

# IEEE Power Writing

Write in a concise IEEE engineering style: claim first, method explicit,
evidence nearby, and limitations bounded. Do not invent results, baselines,
statistics, datasets, references, or mechanisms.

## Intake

Identify:

1. Target journal: TPWRS, TSG, or another IEEE PES venue.
2. Section type: title, abstract, introduction, method, results, discussion,
   conclusion, keywords, or full outline.
3. Contribution: what is new and why it matters to power engineering.
4. Evidence: figures, tables, simulations, hardware tests, field data, or
   theoretical results.
5. Boundary: assumptions, network type, operating condition, and deployment limit.

If the target journal is unclear, infer only from topic:

- TPWRS: analysis, dynamics, operations, planning, reliability, resilience,
  economics, and education.
- TSG: microgrids, active distribution networks, DER/EV integration, AMI,
  distribution PMU applications, cyber-physical security, transactive energy,
  and data analytics for microgrids or ADNs.

When the topic is boundary-sensitive, state the risk instead of forcing a match.

## Abstract rules

Use one paragraph, approximately 150-200 words. Keep it self-contained and avoid
citations, footnotes, displayed equations, tabular material, and unexplained
abbreviations. A robust pattern is:

`problem -> gap -> method -> key quantitative result -> implication -> boundary`

## Section defaults

- Introduction: operational problem -> prior limitation -> unresolved gap ->
  contribution -> evidence preview.
- Method: model assumptions -> notation -> formulation or architecture ->
  solution method -> reproducibility-critical settings.
- Results: case system -> evaluation protocol -> main comparison -> diagnostic
  or ablation -> robustness or scalability -> practical interpretation.
- Conclusion: demonstrated result -> engineering implication -> limitation ->
  future extension.

## Style guardrails

- Prefer exact engineering nouns over broad adjectives.
- Use SI units and define per-unit bases when relevant.
- Use "power flow analysis" rather than "load flow calculation" unless quoting.
- Do not call a transmission-only market or WAMS topic a smart-grid contribution
  without a clear TSG scope rationale.
- Keep contribution claims proportional to evidence.
- For Chinese drafts, translate intent and argument, not word order.

## Output

Return:

1. Revised text or draft.
2. Short claim-evidence map for major claims.
3. Scope note if TPWRS/TSG fit is material.
4. Missing inputs only when they affect submission readiness.

## When to load references

| File | Open when |
|---|---|
| `references/manuscript-structure.md` | Drafting or restructuring sections. |
| `references/tps-vs-tsg.md` | Deciding TPWRS versus TSG fit. |
| `references/abstract-keywords.md` | Writing abstract or keywords. |
| `references/style-guardrails.md` | Polishing tone, terminology, units, and claims. |
