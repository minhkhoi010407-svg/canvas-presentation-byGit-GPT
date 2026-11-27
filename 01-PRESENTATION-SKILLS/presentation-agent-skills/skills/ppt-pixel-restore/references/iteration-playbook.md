# 8–10 Pass Iteration Playbook

Keep every pass narrow enough that its effect is visible in the next comparison.

## Pass 1 — source map and protection

Confirm page mapping, canvas, reference crops, protected selectors/objects, and no-change pages. Capture the immutable baseline.

## Pass 2 — macro geometry

Match the outer margins, column widths, large bands, major card rectangles, dominant images, and overall density. Ignore shadows and tiny offsets.

## Pass 3 — information hierarchy

Match reading order, grouping, visual emphasis, label treatment, and whitespace. Preserve protected titles and copy even when the reference differs.

## Pass 4 — typography and wrapping

Match font availability, weight, line height, letter spacing, paragraph width, and line breaks. Repair overlap by changing the editable container before shrinking type. Never reduce protected font sizes to make content fit.

## Pass 5 — diagrams, charts, and assets

Match real asset crops, chart scales, line endpoints, node centers, connector routing, icon scale, and repeated-item spacing. Measure center axes instead of judging by eye alone.

## Pass 6 — color and surface

Match fills, text color, opacity, borders, shadows, radii, and background blocks. Reuse the deck's existing tokens when the user says the palette must remain.

## Pass 7 — collision and overflow repair

Run DOM/object QA. Fix text overlaps, clipped labels, objects leaving the canvas, bad stacking order, and inconsistent repeated spacing. Remove unrequested separators or notes only when the user authorizes it.

## Pass 8 — optical alignment

Correct the final 1–8 px errors: center axes, baselines, card padding, chart labels, repeated numerals, and visual balance. Prefer parent-grid fixes over scattered transforms.

## Pass 9 — narrative and full-deck regression

Use this pass when copy was also revised. Read the titles and subtitles in sequence, then recheck line wrapping, protected text, no-change pages, navigation, assets, and console state across the full deck.

## Pass 10 — delivery parity

Use only when needed. Re-render the approved state, rebuild contact sheets, verify exported PDF/PPTX/HTML, and—only when deployment was requested—compare deployed asset hashes or bytes with the local approved files.

## Round record

For each pass write:

```markdown
### Round 04 — typography and wrapping
- Pages checked: 3, 5, 7
- Largest mismatch before:
- Changes made:
- Protected regression: none | details
- Remaining P0/P1/P2:
- Evidence: path/to/comparison.png
```

Two consecutive passes with no meaningful improvement indicate convergence. Stop instead of perturbing already matched areas.
