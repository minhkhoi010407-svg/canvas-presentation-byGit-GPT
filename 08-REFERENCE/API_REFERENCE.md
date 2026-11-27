# Capability reference

This is a role/selection reference, not a substitute for the current upstream API documentation.

| Resource | Use it for | Do not use it for |
|---|---|---|
| Knowledge Cat PPT Skill | End-to-end story-first deck workflow and output routing | Runtime rendering |
| Codex PPT | AI-image pages and optional editable reconstruction workflow | Guaranteed editable output from a raster page |
| Presentation Skill | Structured plan/design/render evidence and style systems | Assuming every optional plugin/corpus is present |
| Master Slide Skill | Hackathon and judge-facing narrative discipline | General-purpose rendering |
| Presentation Agent Skills | Specialist storyline, generator, director, restoration, and QA tasks | Five parallel, conflicting primary planners |
| PptxGenJS | Programmatic PPTX generation in a JS/TS application | Browser rendering or fact checking |
| OfficeGen | Alternative Office document generation, subject to current compatibility testing | Assumed current or preferred PPTX engine |
| Marp | Markdown-authored slide decks | Vue-rich interactivity or guaranteed editable PPTX |
| Slidev | Markdown/Vue developer presentations and browser-native interaction | A lightweight standalone PPTX package |
| Playwright | Browser automation, app/web deck screenshots, and browser behavior | Native PPTX parsing/rendering |
| shadcn/ui | Generator product UI in a compatible React app | Slide rendering |
| Lucide | Consistent framework icon components/SVG assets | Full illustration, branding, or data-chart library |

## Adapter-specific verification

Before calling a library from application code, consult its current upstream API docs and use the exact installed version's types. In the adapter test suite verify:

- creation and reopening of a minimal file;
- text, shapes, images, chart data/units, and notes required by the product;
- fonts, image embedding, page dimensions, and renderer compatibility;
- error handling, output cleanup, and stable diagnostics;
- editability of representative elements in the target viewer.

Keep application API documentation separate from source links in `SOURCE_REGISTRY.json`; these sources change independently.

