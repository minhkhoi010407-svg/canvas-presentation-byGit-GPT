# Unified AI Presentation Toolkit

A curated, source-attributed resource repository for AI agents and engineers building presentation-generation workflows. It is an integration and reference toolkit, **not** a finished slide-generation application.

Start with [`MASTER_GUIDE.md`](MASTER_GUIDE.md) for the architecture and implementation path, then use [`INTEGRATION_MANIFEST.md`](INTEGRATION_MANIFEST.md) for the evidence-based source inventory and validation results.

## What is here

- Five presentation-agent skill sources, preserved selectively with their original licenses.
- Seven production, framework, interface, icon, and QA resources, with their roles and dependencies separated.
- A reusable presentation pipeline, skill router, output-selection rules, quality gates, and example briefs/storyboards.
- A machine-readable [`SOURCE_REGISTRY.json`](SOURCE_REGISTRY.json) and source-specific notices in [`LICENSES.md`](LICENSES.md).

## Resource map

| Area | Contents |
|---|---|
| `00-CORE/` | Architecture, agent coordination, workflow, design, integrity, quality |
| `01-PRESENTATION-SKILLS/` | Knowledge Cat, Codex PPT, Presentation Skill, Master Slide Skill, Presentation Agent Skills |
| `02-PPTX-ENGINES/` | PptxGenJS and OfficeGen; neither is bundled as an installable dependency |
| `03-PRESENTATION-FRAMEWORKS/` | Marp and Slidev as optional authored-source pipelines |
| `04-UI-AND-VISUAL/` | shadcn/ui for application UI and Lucide for icons |
| `05-AUTOMATION-AND-QA/` | Playwright for browser-visible app/deck QA, not native PPTX rendering |
| `06-UNIFIED-ENGINE/` | Engine-neutral orchestration contracts and pipeline design |
| `07-EXAMPLES/` | Brief, story, and QA examples; not pre-rendered or fact-verified decks |
| `08-REFERENCE/` | API routing, dependencies, compatibility, limitations |
| `09-TOOLS/` | Repository validation and setup guidance |

## Use

1. Read `MASTER_GUIDE.md`, `06-UNIFIED-ENGINE/SKILL_ROUTER.md`, and `08-REFERENCE/DEPENDENCY_MATRIX.md`.
2. Select a production lane from the user's editability and delivery needs; do not install every resource.
3. Install and pin the selected runtime dependencies in the application that will generate the deck.
4. Follow the content-integrity and QA gates before claiming a deliverable is complete.

The upstream projects retain their own licenses and copyright. This aggregate intentionally does not declare one license for all contents; see `LICENSES.md`.

