# Compatibility matrix

Compatibility is an application-level result, not a property inferred from two GitHub repository names. `Unknown` means this toolkit has not implemented or tested an integration.

| Pair / path | Expected relationship | Status here | Validate in consuming application |
|---|---|---|---|
| Skills -> canonical brief/storyboard | Convert guidance into explicit artifacts | Guidance only | Schema mapping, precedence, failure behavior |
| PptxGenJS -> native PPTX | Direct generation candidate | Not implemented/tested | Office-compatible rendering, editability, fonts, charts, package validity |
| OfficeGen -> native PPTX | Alternative generator | Not implemented/tested; old observed release | Modern Node install, dependency security, target viewers, feature parity |
| Marp -> Markdown deck | Native authored-source workflow | Not implemented/tested | CLI version, theme, PDF/browser export toolchain |
| Slidev -> Vue/Markdown deck | Native authored-source workflow | Not implemented/tested | Node floor, Vue/Vite compatibility, browser and export tools |
| Marp/Slidev -> editable PPTX | Requires a distinct conversion adapter | No adapter supplied | Element-by-element conversion, notes, charts, editability/fidelity |
| Playwright -> web deck/app | Browser-driven QA | Guidance only | Browser binaries, fonts, headless/CI display environment |
| Playwright -> native PPTX | No direct rendering relationship | Unsupported assumption | Use a separate Office-compatible PPTX renderer/viewer |
| shadcn/ui -> generator web UI | Product UI components in compatible React stack | Guidance only | React/Tailwind/config versions, component-level dependencies |
| Lucide -> UI/deck assets | Icons in supported framework/package | Guidance only | Package variant, sizing, stroke rendering, license notices |
| AI Studio -> any runtime/exporter | Host-dependent execution | Unknown | Probe runtime, network, storage, binaries, quotas, and export access |

No end-to-end integration, build, rendering, or cross-viewer validation is claimed by this repository.

