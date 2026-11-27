# QA pipeline

QA is staged and evidence-based. The application should block export claims on failed gates while allowing a user-visible draft when appropriate.

## Content QA

- Compare rendered text and speaker notes to storyboard.
- Check all material factual claims against the evidence ledger.
- Validate numbers, units, time ranges, citations, terms, language, and spelling.
- Check narrative purpose and action title per slide.

## Visual QA

- Produce a contact sheet and inspect every page at presentation size.
- Check clipped/overlapping/off-canvas content, line wraps, contrast, type size, alignment, density, image crops, and chart labels.
- Review first/last slides, dense slides, charts, and a representative complex slide at full size.
- Record renderer and fonts; report the tested view, not universal rendering fidelity.

## Editability and accessibility QA

- State which element types must be editable; inspect representative elements in an Office-compatible viewer and perform a sample edit when the user requested editability.
- Confirm intended reading order, notes, alt text, and non-color cues where supported.
- Label rasterized pages and other non-editable elements honestly.

## Browser QA boundary

Use Playwright for generator UI, HTML slide decks, or browser previews. Capture screenshots and console/network failures as browser evidence. Playwright does not interpret Office Open XML or replace PPTX renderers/editability checks.

Each gate must return structured `pass`, `fail`, or `not_run`, evidence paths/notes, and unresolved findings. Never map `not_run` to `pass`.

