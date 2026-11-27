# Master Guide: Unified AI Presentation Toolkit

## 1. Project purpose

This repository is a curated integration reference for building an AI presentation-generation application. It combines presentation-agent guidance with selected PPTX engines, authored-source frameworks, application UI resources, iconography, and browser QA. It is **not** a finished generator, a unified runtime, or a claim that the upstream projects interoperate natively.

Treat source code, examples, and claims as belonging to their upstream authors. The aggregator supplies routing, contracts, trade-off analysis, and examples; it does not relicense upstream work. Source provenance and inclusion scope are recorded in `SOURCE_REGISTRY.json` and `INTEGRATION_MANIFEST.md`.

## 2. Repository map

- `00-CORE/`: platform-neutral architecture, orchestration, workflow, design, factual integrity, and quality policy.
- `01-PRESENTATION-SKILLS/`: five agent skills. Use their source `SKILL.md` and referenced material as task-specific guidance, not as five simultaneous system prompts.
- `02-PPTX-ENGINES/`: native editable PowerPoint generation candidates.
- `03-PRESENTATION-FRAMEWORKS/`: Markdown/HTML/Vue authoring pipelines for browser presentations and optional conversions.
- `04-UI-AND-VISUAL/`: web-application components and icon resources; these do not generate slide files.
- `05-AUTOMATION-AND-QA/`: browser automation and screenshot QA; this does not natively render or validate PPTX packages.
- `06-UNIFIED-ENGINE/`: engine-neutral orchestration contracts, output lanes, asset pipeline, export and QA stages.
- `07-EXAMPLES/`: illustrative input and intermediate artifacts, not test fixtures that prove a production pipeline.
- `08-REFERENCE/`: capability, dependency, compatibility, and limitation matrices.
- `09-TOOLS/`: local repository validation and setup notes.

## 3. The 12 resources and their roles

### Presentation intelligence

1. **Knowledge Cat PPT Skill** — story-first planning, output-lane routing, design systems, and verification guidance. Its schema and sample plan are preserved with selected references. It is the recommended primary orchestration skill for a general deck task.
2. **Codex PPT** — image-first slide creation and an image-approved, per-slide editable reconstruction workflow. Its output defaults and environment assumptions differ from native-first production.
3. **Presentation Skill** — structured deck artifacts, design contracts, style selection, renderer-aware planning, and quality evidence. Its source is selectively curated; do not assume every upstream plugin, renderer, or corpus is included.
4. **Master Slide Skill** — a compact, judge-focused hackathon deck workflow with explicit reminders not to promise a PPTX that the environment cannot render or verify.
5. **Presentation Agent Skills** — specialist skills for consulting storylines, PPTX generation, visual direction, pixel restoration, and presentation QA. Route to one specialist when its task is needed.

### Production

6. **PptxGenJS** — primary candidate for programmatic native PowerPoint objects from JavaScript/TypeScript. Install the upstream package in the application; this repository does not bundle it.
7. **OfficeGen** — alternative Node.js Office document generation library, assessed as a reference/legacy-compatible option rather than the default. The verified upstream release is old; run current compatibility and feature checks before adoption.

### Authoring frameworks

8. **Marp** — Markdown-first slide authoring and rendering ecosystem. Good for text-centric, reproducible presentations; not a universal substitute for precise native-object authoring.
9. **Slidev** — Markdown + Vue developer presentation framework with interactive and browser-native capabilities. Use when Vue/web presentation features justify its larger application runtime.

### Application UI, visuals, and QA

10. **Playwright** — browser automation, screenshots, and web application testing. It can inspect a browser-rendered deck or application, but does not itself render Office Open XML PPTX.
11. **shadcn/ui** — customizable React application interface components and registry tooling. It belongs in the generator's product UI, not in the slide-rendering engine.
12. **Lucide** — icon set and framework packages. Use supported icon packages or SVG assets under their license; avoid treating icons as a complete illustration system.

See the source-specific folders and registry for exact provenance, licenses, version evidence, commit metadata, and curation status.

## 4. Recommended integration architecture

Use an application-owned orchestration layer with stable, engine-neutral artifacts:

1. **Intake and research** produce a brief, audience, intended decision/learning outcome, citation requirements, and research notes.
2. **Verification** records each factual claim, its source, date/context, and uncertainty. Unsupported claims remain marked or are removed.
3. **Story architecture** creates a narrative spine and action-title outline.
4. **Art direction** selects a coherent visual system: typography, colors, layout grammar, chart style, image treatment, and accessibility rules.
5. **Asset planning** separates original visuals, user-supplied assets, licensed external assets, and generated assets, with source and usage metadata.
6. **Storyboard** maps each slide to one purpose, evidence, text, visual, and intended layout.
7. **Rendering adapter** transforms the storyboard into the chosen output lane. Adapters are isolated behind a canonical slide model; do not make skills call engines ad hoc.
8. **Rendering and QA** create inspectable output, collect screenshots/render reports, and run independent visual, content, and editability checks.
9. **Export** packages the requested output and its relevant source files, citations, and QA receipt.

The canonical model and stage contracts are described in `06-UNIFIED-ENGINE/ENGINE_ARCHITECTURE.md` and `06-UNIFIED-ENGINE/RENDERING_PIPELINE.md`.

## 5. Dependency and compatibility analysis

The skills are instructions and examples, not runtime libraries. PptxGenJS and OfficeGen are separate PPTX APIs; they are not drop-in compatible. Marp and Slidev have their own CLI/build/runtime paths. Playwright requires a Node runtime and browser binaries for execution. shadcn/ui components require a compatible React/Tailwind project and may require project-specific setup. Lucide imports vary by framework and package.

Choose dependencies only after selecting the output lane. Pin actual versions in the application repository and test the selected combination there. The upstream monorepo versions shown in the registry are provenance observations, not recommended dependency pins. Check `08-REFERENCE/DEPENDENCY_MATRIX.md` and `COMPATIBILITY_MATRIX.md`.

Do not assume Google AI Studio provides Node, Python, LibreOffice, Office, browser binaries, GPU/image-generation APIs, network access, or persistent writable storage. Probe the actual environment and fail clearly when a required renderer or converter is missing.

## 6. Skill selection and routing

Follow `06-UNIFIED-ENGINE/SKILL_ROUTER.md`. In summary:

- Start with one primary story/production skill, usually Knowledge Cat for a general deck.
- Add Codex PPT only when image-first output or screenshot-guided editable reconstruction is explicitly appropriate.
- Use Presentation Skill for structured artifacts, renderer selection, style contracts, and evidence-oriented QA.
- Use a specialist from Presentation Agent Skills only for its bounded job.
- Use Master Slide Skill for hackathon/judging contexts.
- Resolve overlapping directions through the user's requirements first, factual integrity and feasibility second, a single selected primary skill third, and an explicit project design system fourth. Do not average incompatible output assumptions.

## 7. Production workflow

The required sequence and input/output contract is in `00-CORE/PRESENTATION_WORKFLOW.md`. Never jump directly from a vague topic to visual generation. A minimum usable handoff includes:

- brief and audience/outcome;
- traceable research and factual review;
- narrative outline with one slide-level takeaway per page;
- art direction and asset plan;
- slide storyboard with content/evidence references;
- selected render adapter and output lane;
- render evidence plus content, visual, and editability QA;
- final export and provenance/limitations note.

## 8. PPTX generation strategy

Prefer **PptxGenJS** as the default native-editable PPTX candidate when the application is JavaScript/TypeScript-based and user-editable shapes, text, charts, and layout matter. Create a narrow adapter and test its generated output in the target viewers. Use native charts or shapes only where their fidelity and editability meet requirements.

Consider **OfficeGen** only if a verified feature or compatibility need warrants it. Its repository is MIT-licensed but its package metadata reports version `0.6.5`, Node `>=0.10.0`, and a last commit dated 2021-03-06. That does not prove it is incompatible, but it does require a current Node/Office-compatibility spike before it is selected. Do not use it as the primary recommendation solely because it can generate `.pptx`.

For image-first or screenshot-reconstruction work, treat the source images as the visual reference, not as proof of editable text or accessible structure. If editable output is required, QA text, object boundaries, reading order, and modification of representative elements. Set expectations about image fidelity versus editability before generation.

Marp/Slidev exports may produce PDF or other presentation formats through their own toolchains; do not promise editable native PPTX without an explicit, tested conversion path. See `06-UNIFIED-ENGINE/PPTX_EXPORT_PIPELINE.md`.

## 9. Visual asset management

Use `06-UNIFIED-ENGINE/VISUAL_ASSET_PIPELINE.md`. Track each asset's ID, origin, source URL or user-provided origin, creator/tool where known, license/permission, attribution requirements, alt text, intended use, and local path. Avoid embedding unverified brand marks or copyrighted reference artwork. Use Lucide for interface/simple diagrams only when it fits the visual system; preserve the applicable license notice—ISC generally, and MIT for the Feather-derived icons listed in its `LICENSE`. Keep generated and external imagery distinct from editable native slide content.

## 10. Quality assurance

Require four independent gates:

- **Content:** claims, numbers, dates, quotations, source citations, spelling, and narrative consistency.
- **Visual:** rendered slide/contact-sheet inspection, clipping/overlap, text size, contrast, alignment, density, and consistency.
- **Editability/accessibility:** expected object types, editable text, reading order, alternative text where supported, and practical modification.
- **Artifact:** output opens in the target viewer, slide count/page size is correct, fonts/assets are packaged or documented, and export reports no silent errors.

Playwright may automate browser-based previews, app UI, or web decks. It is not a native PPTX renderer or a substitute for opening/rendering PPTX with a compatible Office renderer. A screenshot is evidence only for the captured rendering, not universal cross-viewer fidelity. See `06-UNIFIED-ENGINE/QA_PIPELINE.md`.

## 11. Limitations and unsupported assumptions

- This repository does not contain a complete production application, unified executable engine, dependency lockfile, verified sample deck, or an end-to-end rendering service.
- Curated source bundles are not necessarily byte-for-byte copies of current upstream branches. ZIP archives do not embed commit IDs; registry commit observations identify upstream tips checked on 2026-11-27, not necessarily the exact archive revision.
- The upstream projects have independent release cycles, licenses, runtimes, support policies, and design assumptions.
- "Editable PPTX" is not a binary property: generated text and shapes may be editable while illustrations are raster images. State exactly what is editable.
- Rendering depends on fonts, Office-compatible software, browser/runtime versions, and available browser binaries.
- AI-generated images can contain visual or textual defects; AI fact summaries can be wrong. Inspect outputs and trace claims.
- External assets, fonts, charts, and brand materials may have additional licensing constraints beyond these repositories.

## 12. Integration instructions

1. Import this repository as reference material; start with this guide and the source registry.
2. Choose one supported output lane and one primary skill, then record the choice in the application design.
3. Probe runtime and filesystem capabilities; install only the selected, pinned dependencies.
4. Define the application-owned brief/storyboard and slide-model schema before implementing adapters.
5. Implement one adapter and one minimal deck path; keep source notes, renderer output, and QA receipts.
6. Validate through the target renderer/viewer and document platform limits. Do not report unrun checks as passed.
7. Review upstream licenses and versions whenever copying code/assets or upgrading dependencies.

## 13. Recommended implementation sequence

1. Build brief, evidence, outline, storyboard, asset, and slide-model schemas.
2. Implement intake, provenance-aware research, and content-verification workflow.
3. Add design-system selection and deterministic storyboard review.
4. Implement a PptxGenJS adapter for a limited, tested subset of native text/shapes/images/charts.
5. Add render-to-image and contact-sheet QA in an environment with a verified PPTX renderer.
6. Add the product UI with shadcn/ui and Lucide only if a web UI is in scope.
7. Add optional Marp or Slidev adapters for their distinct authored-source use cases.
8. Add browser QA with Playwright for the application/web-deck paths.
9. Add image-first/reconstruction lane only after explicitly testing its image and editability contracts.
10. Re-evaluate dependencies, upstream activity, compatibility, and licensing before release.

