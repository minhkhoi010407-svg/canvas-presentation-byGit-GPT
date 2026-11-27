# Rendering pipeline

## Stage inputs and outputs

| Stage | Input | Output | Invariant |
|---|---|---|---|
| Normalize | Brief, locale, constraints | normalized brief | preserve intent and explicit unknowns |
| Research | brief questions | evidence ledger | claims are traceable and scoped |
| Verify | draft claims + evidence | verified/qualified claims | no unsupported fact promoted |
| Structure | verified claims | narrative outline | logical progression and audience outcome |
| Direct | outline + audience | design contract | one coherent visual system |
| Plan assets | design contract | asset manifest | provenance and rights captured |
| Storyboard | outline, evidence, assets | slide plan | one purpose/takeaway per slide |
| Adapt | slide plan + lane | renderer input | every feature mapped or explicitly rejected |
| Render | renderer input + pinned toolchain | artifact + receipt | errors and environment are visible |
| Review | artifact + receipts | revision findings | content, visual, and editability gates separate |
| Export | QA-passed artifact | delivery package | correct format and caveats disclosed |

## Output lanes

### Editable-first

Use semantic text, shapes, charts, and images through a native PPTX adapter, generally PptxGenJS for a Node application. It offers direct control over generated Office objects, but requires renderer/viewer validation. Choose this lane when the recipient needs to edit slide content and layout.

### Image-first

Use full-page images as the primary output when visual composition is more important than native editability. An image-first PPTX can place each page image on a slide, but on-slide text/illustrations remain rasterized. Inspect generated text and package a PDF/images as appropriate.

### Hybrid

Combine editable titles, labels, key data, and simple shapes with raster or vector assets for complex artwork. Document which objects are editable and which are not. Test representative edits and check text/image alignment after rendering.

### Browser-authored

Use Marp for a simple Markdown presentation or Slidev when Vue/interactive web features are valuable. This is a separate authoring and rendering path; converting its output into editable PPTX is an additional adapter with its own QA contract.

