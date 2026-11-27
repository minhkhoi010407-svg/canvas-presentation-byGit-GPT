# Multi-page Deck Restoration Example

This is the concrete run that the skill was distilled from. It is a visual QA example, not approval of any business claim or publication.

## Scope and protection

- The active artifact was a 15-page fixed-canvas HTML deck.
- Thirteen reference images mapped to pages 1–5 and 7–14.
- Pages 6 and 15 had no reference image and therefore remained unchanged.
- Protected surfaces were the current main title and subtitle treatment, upper-left page label, upper-right logo, page number, existing font sizes and dimensions, and current background palette.
- No extra concluding sentence or reference-only summary band was added.

## Ten-round restoration sequence

1. Pages 1–5: team cards, technical evolution, a brand case, industry-data grid, and whitespace.
2. Page 7: frequency staircase, three quantity bands, and the result strip.
3. Page 8: changed a generic four-curve concept into a vertical evidence-card structure while preserving the red/pink palette.
4. Page 9: before/after attribution columns, unknown-attribution node, and bottom judgment band.
5. Page 10: system stack, KPI feedback loop, and month/week/day cadence.
6. Page 11: three-layer architecture, execution path, and feedback loop.
7. Page 12: demo-AI versus real-business-AI paths, central judgment, and value band.
8. Page 13: transfer conveyor, enterprise growth system, four retained assets, and delivery area.
9. Page 14: 12-week table row height, vertical rhythm, and core-logic band.
10. Full-deck micro-alignment, icon strokes, attribution widths, pixel re-measurement, and protected-item regression.

## Quantitative evidence

- Reference and implementation pages were normalized to 1920×1080.
- Pixels with grayscale difference above 40 counted toward the difference ratio.
- Mean difference ratio across the 13 referenced pages moved from 10.52% to 9.84%.
- The global score was not the acceptance criterion: page 5 retained a larger intentional difference because its protected title/subtitle and absent conclusion band were preserved.
- Protected-element comparison reported no change.
- Pages 6 and 15 reported exactly zero changed pixels.
- Page count remained 15; JavaScript syntax passed; browser runtime errors and broken images were zero.

## Feedback round 11 example

A later annotated review of page 5 requested clearer section labels, smaller and less crowded metrics, removal of vertical separators, centering of a funnel, and removal of left-side notes.

The fix used existing color tokens, reduced the four metric values to 28 px, increased their gap to 18 px, removed divider borders and separator glyphs, and placed both funnel shapes and values on the same grid. Browser measurements confirmed five center offsets of 0 px and metric borders of 0 px. Next/previous navigation and the browser console were rechecked afterward.

## Main lessons

- Protected content outranks visual similarity.
- A no-image page must be proven unchanged, not merely left out of the report.
- Structural layout fixes produce more reliable results than accumulating transforms.
- Overlap and center alignment should be measured in the DOM or object model, then confirmed visually.
- A combined reference/implementation image is stronger evidence than two separate screenshots.
- Deployment is a separate authorized step; after release, verify access state and compare deployed files with the approved local build.
