# Dependency matrix

The source repositories are not a single dependency stack. Install only what the selected application lane uses, pin versions in that application, and retain its lockfile/SBOM separately.

| Resource | Runtime / package boundary | Additional requirements and cautions |
|---|---|---|
| Knowledge Cat PPT Skill | Agent instructions; selected scripts are Python source | Skills do not install engines. Validate any reused script and its Python requirements independently. |
| Codex PPT | Agent instructions; source metadata shows `pptxgenjs` and Node `>=18.0.0` in its package | Its image-generation workflow needs a compatible image-generation capability; its PDF/image helpers may require Python packages and system tools. |
| Presentation Skill | Agent instructions; archived package lists `pptxgenjs`, `jszip`, React and `sharp` | It has many optional scripts/checks. The archive's package manifest is not a curated toolkit install plan. |
| Master Slide Skill | Text-only agent skill | Renderer/runtime is selected separately. |
| Presentation Agent Skills | Agent instructions; optional image comparison script uses Python ecosystem | The skills do not provide a complete generator runtime. Check each specialist's references. |
| PptxGenJS | Install `pptxgenjs` in the JS/TS application | Package metadata observed at `4.0.1`; repository root `engines` did not declare a Node version in the supplied archive. Verify current install/runtime requirements. |
| OfficeGen | Install `officegen` only in an isolated compatibility spike | Verified `0.6.5` metadata says Node `>=0.10.0`; its dependency list includes `archiver`, `async`, `fast-image-size`, `jszip`, `lodash`, `readable-stream`, `setimmediate`, and `xmlbuilder`. Old metadata is not a modern compatibility guarantee. |
| Marp | Select an actual ecosystem package such as its CLI/core package | The upstream repository spans multiple related projects; repository root package has no single observed release version. Install the selected package(s) and renderer separately. |
| Slidev | Select the required Slidev CLI/framework packages | Root archive metadata says Node `>=22.22.0`, version `53.2.0`; verify current package-specific engine requirements and browser/PDF export dependencies. |
| Playwright | Install a chosen Playwright package with a compatible Node runtime | Browser binaries must be installed and match package expectations. Supplied monorepo root package says Node `>=20`, which is not a statement of every consumer package's support floor. |
| shadcn/ui | Use its CLI or copy selected registry components into a React application | Requires compatible React, styling/configuration, and any primitive/icon dependencies used by selected components. Component source becomes application code; review its license and generated dependencies. |
| Lucide | Install the framework-specific Lucide package or consume approved SVGs | Package varies by framework. Keep ISC attribution for redistributed assets and verify selected package/version. |

## Runtime policy

- Never install a complete upstream monorepo to use one small skill or library.
- Do not check in `node_modules`, browser binaries, caches, generated build output, or application credentials.
- Do not assume the AI host has Node, Python, LibreOffice, Microsoft Office, browsers, fonts, or external network access.
- Detect required tools before starting and return actionable errors for missing executables or fonts.
- Record versions at application build/release time; this registry's versions are source-audit evidence, not evergreen pins.

