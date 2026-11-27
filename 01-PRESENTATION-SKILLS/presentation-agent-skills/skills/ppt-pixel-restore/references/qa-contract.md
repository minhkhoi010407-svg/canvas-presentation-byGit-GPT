# Restoration QA Contract

Use this contract before editing so the reference, user constraints, and measurable result cannot drift apart.

## Precedence

1. Latest explicit user request.
2. User-declared protected elements and no-change pages.
3. Current approved copy and data.
4. Reference image geometry and styling.
5. Existing implementation details.

If two sources conflict, preserve the higher item and record the residual visual difference as intentional.

## Manifest template

```markdown
# Restoration manifest

- Active source:
- Working copy:
- Output target: HTML | PPTX | PNG/PDF
- Canvas: 1280x720 | 1920x1080 | other
- Canonical viewport / device scale:
- Fonts and fallbacks:
- Reference source and revision:
- Publish authorization: no | yes, target ...

| Page | Reference | State | Protected | Editable zones | Notes |
|---:|---|---|---|---|---|
| 01 | ref-01.png | MATCH | title, subtitle, logo | body | |
| 02 | none | NO CHANGE | entire page | none | no image supplied |
```

## Protected snapshot

For HTML, store for every protected selector:

- text content;
- computed font family, size, weight, line height, letter spacing, and color;
- `getBoundingClientRect()` values;
- relevant background and border values;
- image `src`, natural dimensions, and rendered rectangle.

For PPTX, store slide/object identifiers where available, text, geometry, crop, font properties, fill, line, and asset hash. Also keep baseline renders because object equality does not prove identical rendering.

For untouched pages, a whole-slide baseline/final pixel comparison should be exactly zero after normalization.

## Priority rubric

- **P0:** missing page/content, broken asset, unreadable text, runtime failure, or unauthorized change.
- **P1:** wrong structure, major region size, content order, crop, or protected-element regression.
- **P2:** visible overlap, incorrect wrapping, alignment, color, scale, spacing, or chart geometry.
- **P3:** small optical polish that does not change comprehension.

## Comparison evidence

For every changed page retain:

1. reference image;
2. implementation render;
3. side-by-side comparison;
4. overlay;
5. heatmap and metrics JSON;
6. one-line judgment explaining the remaining largest difference.

Use a stable naming scheme such as `page-05-round-04-*`. Never overwrite the baseline.

## Final acceptance checklist

- Page count and ordering match.
- All reference images have a mapped page.
- Missing-reference pages are unchanged.
- Protected text, geometry, styling, and assets match the baseline.
- No unintended text overlap or clipping remains.
- All images load and retain correct aspect ratio.
- Console and syntax errors are zero.
- Navigation and primary interaction work.
- Copy and numeric claims remain source-bounded.
- Final render and public/deployed files, if authorized, match the approved local version.
