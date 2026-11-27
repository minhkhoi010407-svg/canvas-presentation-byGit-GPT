# PPTX export pipeline

## Native generation path

1. Validate canonical deck and reject unsupported elements.
2. Map design tokens and geometry to a renderer-specific layout.
3. Add text/shapes/charts/images with stable slide/element IDs in source artifacts.
4. Write `.pptx` to a temporary output; keep renderer logs.
5. Render using a verified Office-compatible renderer in the target environment.
6. Inspect slide count, dimensions, text, representative object editability, and all rendered pages.
7. Re-open the final file after the last edit and generate the delivery receipt.

PptxGenJS is the preferred first adapter candidate for a Node/TypeScript application; verify its current package/API at implementation time. OfficeGen is an alternate candidate with an old observed upstream version; adopt only after a compatibility spike. Do not choose two engines by default.

## Browser framework conversion

Marp/Slidev source does not become editable PPTX merely because it can be rendered to HTML, PDF, or images. A framework-to-PPTX converter must define how text, layout, charts, links, speaker notes, fonts, and assets map; evaluate each converted object for editability and fidelity. When no such adapter is implemented, deliver the format the framework actually produces.

## Required export receipt

Record source revision and package version, runtime/platform, renderer/viewer and version, fonts, output name/size/slide count, warnings/errors, inspection result, and untested environments. Keep this receipt with the artifact.

