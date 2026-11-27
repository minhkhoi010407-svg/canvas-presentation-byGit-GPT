# Content integrity and provenance

## Claim ledger

Maintain one record per material factual claim:

```json
{
  "claim_id": "claim-001",
  "claim": "A concise, testable statement",
  "source_url": "https://example.org/source",
  "source_title": "Source title",
  "published_or_accessed": "YYYY-MM-DD",
  "support": "Where the evidence appears and how it supports the claim",
  "confidence": "verified | qualified | unresolved",
  "slide_ids": ["slide-03"]
}
```

Replace example values with evidence; do not use this illustration as a factual source. Prefer primary sources for material claims. Record disagreement and uncertainty instead of suppressing them.

## Non-negotiable checks

- Do not invent statistics, quotations, case studies, customer logos, source citations, or experimental results.
- Distinguish user-provided statements, externally verified facts, estimates, and generated interpretation.
- Preserve the source's date, population, units, and context when summarizing data.
- Ensure that each slide's claims can be traced to evidence or are clearly marked as proposed/hypothetical.
- Treat output quality reports as evidence of only the checks actually performed.
- Do not claim a rendering, file-open, browser, or editability check without a recorded run and environment.

