# Instructions for AI coding agents

- Treat this repository as an integration toolkit, not as a completed presentation-generator application.
- Read `MASTER_GUIDE.md`, `SOURCE_REGISTRY.json`, and the applicable files in `00-CORE/` before making architectural claims.
- Keep original source material, author attribution, license files, and source URLs intact. Make aggregator-authored analysis outside upstream source files.
- Do not infer that a source archive matches a later upstream commit. Do not invent versions, compatibility, tests, or integrations.
- Select one primary skill and one output lane for each task. Resolve conflicting instructions explicitly; do not combine all skill prompts wholesale.
- Keep research and claims traceable. Mark unknown or unverified facts instead of filling gaps.
- Install only dependencies needed by the selected lane. Never add `node_modules`, browser binaries, build outputs, caches, secrets, or generated decks to this reference repository.
- Treat UI libraries, icons, presentation authoring frameworks, native PPTX engines, and browser QA as distinct roles.
- Before claiming a presentation or adapter works, validate it in an available target renderer/viewer and report the exact checks performed and any limitations.
- Update `SOURCE_REGISTRY.json`, `LICENSES.md`, and `INTEGRATION_MANIFEST.md` when adding, removing, or changing source material.

