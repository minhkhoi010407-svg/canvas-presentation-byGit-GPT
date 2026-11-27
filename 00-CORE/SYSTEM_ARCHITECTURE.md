# System architecture

## Layers

| Layer | Responsibility | Owns |
|---|---|---|
| Intake | Clarify audience, outcome, scope, format, language, constraints | normalized brief |
| Evidence | Research, source traceability, claim verification | source ledger and verified facts |
| Story | Narrative structure and slide-level takeaways | outline and storyboard |
| Design | Art direction, visual grammar, accessible tokens | design contract and asset plan |
| Orchestration | Apply gates, route one primary skill, select output lane | stage state and decisions |
| Adapter | Map canonical slide model to one renderer | PPTX, PDF, HTML, or image output |
| QA | Inspect content, renders, editability, and artifact integrity | reports and evidence |
| Delivery | Package requested outputs and caveats | user deliverables and provenance |

Keep the canonical brief, outline, asset records, and storyboard independent of renderer-specific code. An adapter may reject unsupported features; it must not silently flatten or omit them.

## Boundaries

- **PptxGenJS / OfficeGen:** native Office package generation APIs.
- **Marp / Slidev:** authored-source presentation toolchains.
- **Playwright:** browser automation and browser-visible evidence.
- **shadcn/ui:** application interface components.
- **Lucide:** icon assets/components.
- **Skills:** human/agent operating procedures and examples.

No source is a universal engine. Adapters, converters, and runtime dependencies are application work and must be implemented/tested by the consuming project.

