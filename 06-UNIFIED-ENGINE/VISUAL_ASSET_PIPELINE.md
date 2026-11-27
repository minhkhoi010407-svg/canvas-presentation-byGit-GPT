# Visual asset pipeline

## Asset record

For each nontrivial visual, persist:

```json
{
  "asset_id": "asset-001",
  "kind": "user | original | generated | external | icon",
  "source": "URL, user-provided filename, or generation tool/model",
  "creator": "Known creator or null",
  "license_or_permission": "Verified terms or unresolved",
  "attribution": "Required credit or none verified",
  "alt_text": "Meaningful description",
  "intended_slides": ["slide-03"],
  "path": "assets/asset-001.png"
}
```

The values above are schema examples, not claims about a real asset.

## Selection and delivery

1. Plan visuals to support evidence and story before searching/generating.
2. Prefer user-provided or appropriately licensed assets. Record uncertainty and do not assume public availability means reusable.
3. Keep original, generated, external, and icon sources distinguishable.
4. Check image dimensions, crop, transparency, contrast, safe area, and text legibility at presentation size.
5. Keep attribution close to the asset or in a source appendix when required.
6. Track fonts and embed/package only when permitted; document substitutions.
7. Use Lucide icons as a consistent icon vocabulary, not as substitute for custom diagrams or data visualization. Preserve the applicable terms in its `LICENSE`: ISC generally and MIT for the enumerated Feather-derived icons.

