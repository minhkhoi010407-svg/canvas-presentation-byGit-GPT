# Source licenses and attribution

This repository aggregates materials from independent upstream projects. **There is no umbrella license for all repository contents.** Each source retains its own license; do not infer that a file is relicensed because it is present here. Aggregator-authored integration documentation is identified by its placement outside the source-specific directories.

The following source license files are preserved under each corresponding source directory:

| Source | License | Preserved notice |
|---|---|---|
| Knowledge Cat PPT Skill | MIT | `01-PRESENTATION-SKILLS/knowledge-cat-ppt-skill/LICENSE` |
| Codex PPT | MIT | `01-PRESENTATION-SKILLS/codex-ppt/LICENSE` |
| Presentation Skill | MIT | `01-PRESENTATION-SKILLS/presentation-skill/LICENSE` |
| Master Slide Skill | MIT | `01-PRESENTATION-SKILLS/master-slide-skill/LICENSE` |
| Presentation Agent Skills | MIT | `01-PRESENTATION-SKILLS/presentation-agent-skills/LICENSE` |
| PptxGenJS | MIT | `02-PPTX-ENGINES/pptxgenjs/LICENSE` |
| OfficeGen | MIT | `02-PPTX-ENGINES/officegen/LICENSE` |
| Marp | MIT | `03-PRESENTATION-FRAMEWORKS/marp/LICENSE` |
| Slidev | MIT | `03-PRESENTATION-FRAMEWORKS/slidev/LICENSE` |
| Playwright | Apache-2.0 | `05-AUTOMATION-AND-QA/playwright/LICENSE` |
| shadcn/ui | MIT | `04-UI-AND-VISUAL/shadcn-ui/LICENSE.md` |
| Lucide | ISC; MIT applies to the Feather-derived icons listed in its license | `04-UI-AND-VISUAL/lucide/LICENSE` |

## Important exceptions and scope

- **Master Slide Skill:** the archive's `LICENSE` identifies itself as MIT but contains the literal copyright placeholder `[YEAR] [COPYRIGHT HOLDER]`. It is preserved unchanged; this repository does not invent a replacement attribution. Confirm upstream before redistributing beyond this curated copy.
- **OfficeGen:** no source ZIP was attached. Its repository, license, package metadata, and commit were checked at the exact revision in `SOURCE_REGISTRY.json`; this toolkit does not reproduce OfficeGen source files.
- **Lucide:** GitHub's repository metadata returned `NOASSERTION`; the included upstream `LICENSE` states ISC and separately applies MIT terms to its enumerated Feather-derived icons. Follow the specific terms for the asset being redistributed.
- A source license applies to that project's material, not automatically to assets, fonts, plugins, or third-party components that project may reference. Review upstream notices and the licenses for anything copied or installed.
- Dependencies are not vendored. Installing a dependency introduces its own license and transitive notices; generate an application-specific third-party notice inventory at release time.

