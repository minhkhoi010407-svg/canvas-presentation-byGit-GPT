# Engine-neutral architecture

The application owns the canonical artifact model; upstream skills and renderers are inputs/adapters, not the integration contract.

## Suggested artifact flow

```text
Brief
  -> EvidenceLedger
  -> NarrativeOutline
  -> DesignContract + AssetManifest
  -> Storyboard
  -> CanonicalDeck
  -> RendererAdapter
  -> RenderedArtifact + RenderReceipt
  -> QAReport
  -> DeliveryPackage
```

Keep stable IDs across stages (`claim_id`, `slide_id`, `asset_id`) so evidence and QA findings can refer back to the originating brief and slide.

## Canonical slide model

Represent content semantically before mapping to a renderer:

- deck metadata: title, audience, locale, aspect ratio, output lane;
- slide: stable ID, purpose, takeaway/action title, evidence references, speaker notes;
- elements: type, text/data, geometry intent, style tokens, alt text, asset reference;
- chart: data with units/source, category and measure fields, axis/scale decisions;
- asset: origin, rights, attribution, path or URI, alt text, placement;
- constraints: editable requirement, font policy, safe margins, maximum density;
- renderer features: explicitly supported, degraded, or rejected by each adapter.

Store user-facing facts and sources separately from rendered presentation text so revisions do not lose provenance.

## Adapter contract

Each adapter should declare:

1. supported element types and layout features;
2. output formats and file naming;
3. required runtime, package version, and external executables;
4. supported fonts/assets and offline behavior;
5. rendering method and target viewers;
6. known fidelity, editability, accessibility, and export limitations;
7. diagnostics and structured render receipt.

Adapters must report unsupported fields. They must not silently convert a chart into an unlabeled picture, discard notes, or imply editability after rasterization.

