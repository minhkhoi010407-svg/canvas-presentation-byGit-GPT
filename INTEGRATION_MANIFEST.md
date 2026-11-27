# Integration manifest and audit record

**Audit date:** 2026-11-27  
**Repository:** [minhkhoi010407-svg/unified-ai-presentation-toolkit](https://github.com/minhkhoi010407-svg/unified-ai-presentation-toolkit)  
**Purpose:** curated source and documentation toolkit; not a completed slide-generation application.

## Source audit and inclusion

The 11 supplied ZIP archives were inspected for repository structure, README, license, package metadata, documentation, examples, scripts, dependencies, and build/test content. GitHub API repository and latest-commit metadata were checked for all 12 sources. OfficeGen's `LICENSE` and `package.json` were fetched from its verified default-branch commit because its ZIP was absent.

**Important revision caveat:** attached ZIPs are branch archives and do not contain their Git commit IDs. `latest_verified_commit` in `SOURCE_REGISTRY.json` records the upstream default-branch tip observed on the audit date; it does not assert that a ZIP matches that commit. Package versions are listed only where observed in the supplied archive or the explicitly pinned OfficeGen metadata.

No complete upstream repository has been copied. Six resources are present as curated source bundles (the five presentation-skill projects and the shadcn agent guide). The other six technical resources are reference-only here: their licenses and source-informed selection guidance are available locally, but upstream implementations/dependency trees are not mirrored. Install those resources from the exact upstream project when developing a consumer application.

| # | Resource | License | Revision/version evidence | Local scope |
|---:|---|---|---|---|
| 1 | [Knowledge Cat PPT Skill](https://github.com/gnipbao/knowledge-cat-ppt-skill) | MIT | `0.10.0` README; upstream tip `889c3dc` | Curated source: skill, all 16 references, schema, sample plan, agent metadata, helper scripts, license |
| 2 | [Codex PPT](https://github.com/qybaihe/codex-ppt) | MIT | `0.4.0` package; upstream tip `2a132f1` | Curated source: skill, five references, selected scripts, one example's source notes, license |
| 3 | [Presentation Skill](https://github.com/siril9/presentation-skill) | MIT | `0.14.0` package; upstream tip `efd899c` | Curated source: skill/design/discovery docs, 11 linked references, selected scripts/metadata, license |
| 4 | [Master Slide Skill](https://github.com/shaikaakif/Master-Slide-Skill) | MIT reported upstream | No version; upstream tip `4ec482a` | Curated source: skill and original license; license has unresolved copyright placeholders |
| 5 | [Presentation Agent Skills](https://github.com/hiamberhuang/presentation-agent-skills) | MIT | No package/release version; upstream tip `9e868af` | Curated source: specialist skills, references, installer, third-party notices, license |
| 6 | [PptxGenJS](https://github.com/gitbrent/PptxGenJS) | MIT | `4.0.1` package; upstream tip `3c9ec1b` | Reference-only: original license, upstream root package metadata, and source-informed adapter recommendation |
| 7 | [OfficeGen](https://github.com/Ziv-Barber/officegen) | MIT | `0.6.5` at exact commit `87dd550` (2021-03-06) | Reference-only: exact upstream license/package metadata and compatibility assessment; no ZIP/source implementation |
| 8 | [Marp](https://github.com/marp-team/marp) | MIT | No single root release version; upstream tip `95263d5` | Reference-only: license, root package metadata, and Markdown authoring/export guidance |
| 9 | [Slidev](https://github.com/slidevjs/slidev) | MIT | Root monorepo metadata `53.2.0`; tip `3de6c46` | Reference-only: license, root package metadata, and Vue/Markdown authoring/export guidance |
| 10 | [Playwright](https://github.com/microsoft/playwright) | Apache-2.0 | No consumer package version inferred; tip `c2ebabaf` | Reference-only: license, NOTICE, root package metadata, and browser-QA scope |
| 11 | [shadcn/ui](https://github.com/shadcn-ui/ui) | MIT | Root tooling metadata `0.0.1`; tip `0e5b2e6` | Curated source: upstream shadcn agent skill and referenced Markdown guides, license, root metadata; no component registry |
| 12 | [Lucide](https://github.com/lucide-icons/lucide) | ISC; MIT for enumerated Feather-derived icons | No single root package version; tip `9cb3934` | Reference-only: original dual-license notice, root metadata, React guide, and icon-use guidance |

Full SHAs, observed archive names, source owners, commit dates, and precise scope are in `SOURCE_REGISTRY.json`. The abbreviated SHAs in this table are for readability only.

## License and dependency findings

- Each included source has its own preserved `LICENSE`/`LICENSE.md`; no aggregate license is declared.
- Master Slide Skill's supplied license text is MIT but has literal `[YEAR] [COPYRIGHT HOLDER]` placeholders. It is not silently repaired.
- Lucide's archive `LICENSE` states ISC and separately identifies Feather-derived icons under MIT; GitHub API metadata returned `NOASSERTION`.
- Playwright is Apache-2.0; its upstream `NOTICE` is preserved.
- No `node_modules`, package lockfiles, browser binaries, dependency caches, secrets, or generated slide binaries are included.
- PptxGenJS is the preferred first candidate for a JS/TS native-PPTX adapter. OfficeGen's verified old package metadata and commit date warrant compatibility/security testing before use; they do not prove incompatibility.
- Marp and Slidev are optional authoring/rendering paths. Neither is assumed to produce editable PPTX directly. Playwright is browser QA, not a PPTX renderer. shadcn/ui and Lucide are application UI/icon resources, not slide engines.
- Runtime requirements and unverified assumptions are detailed in `08-REFERENCE/DEPENDENCY_MATRIX.md`, `COMPATIBILITY_MATRIX.md`, and `KNOWN_LIMITATIONS.md`.

## Repository structure

The repository follows the requested numbered layout: root guide, registry, manifest and license summary; `.github/copilot-instructions.md`; six core references; five skill bundles; two PPTX engine records; two optional framework records; application UI/icon notes; Playwright QA note; unified engine architecture; four example contexts; API/dependency/compatibility/limitation references; and setup/validation tools.

## Validation and final review

- [x] Registry JSON parses and contains exactly 12 unique source IDs and the requested 12 repository URLs.
- [x] Required documents, all 12 source guides/license files, and every inline local Markdown link resolve.
- [x] Source license files are present; Playwright's Apache `NOTICE` is also present.
- [x] Repository validation found no `node_modules`, cache/build-output directories, or likely credential files.
- [x] Documentation distinguishes six curated source bundles from six reference-only resources; no full upstream mirror is claimed.
- [x] No application build, slide render, exported PPTX, or end-to-end integration is claimed.

**Validator result:** `node .\09-TOOLS\validate-repository\validate.mjs` — passed; 12 sources, 180 files, local links resolved. The seven upstream package metadata JSON files and source registry also parsed successfully.

The validator checks repository structure and local links, not upstream correctness or deck rendering. No root build/test suite exists; source scripts are preserved reference material and were not executed. This repository does not implement a production deck generator, so no end-to-end deck export was attempted.

