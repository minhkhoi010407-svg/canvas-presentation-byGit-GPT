# Skill router

Use the smallest number of skill instructions that covers the task. Skills supply operating guidance; an application should translate selected guidance into typed artifacts and guards rather than injecting every source wholesale.

| User/task signal | Primary guidance | Add only when useful | Avoid |
|---|---|---|---|
| General deck from a topic, report, or notes | Knowledge Cat PPT Skill | Presentation Skill for structured artifacts; `presentation-qa` for review | Concurrently using every skill as an equal planner |
| User explicitly wants image-first pages or image-accurate rendering | Codex PPT image mode | slide-visual-director for visual planning | Claiming editable PPTX from page images |
| User wants editable PPTX | Knowledge Cat native lane or Presentation Skill | Codex PPT reconstruction only when image target is approved; `pptx-generator` for bounded generation | Treating raster images as editable slide elements |
| Existing deck or screenshot reconstruction | Knowledge Cat template replication or `ppt-pixel-restore` | `presentation-qa` | Guessing dimensions or declaring pixel fidelity without visual comparison |
| Consulting, board, strategy, or business case | `consulting-deck-expert` | Knowledge Cat for end-to-end gates | Fabricated market data or generic template output |
| Hackathon/demo-day judging deck | Master Slide Skill | Knowledge Cat for research/QA | Unsupported claims and fictional traction |
| Web-native talk or developer presentation | Slidev | Playwright for browser QA | Adding PPTX conversion without a tested adapter |
| Markdown-led simple linear deck | Marp | Browser/CLI QA for the selected export | Assuming Markdown export is a native editable PPTX |
| Product UI for a generator | Application-owned UI with shadcn/ui | Lucide icons | Treating either as a slide engine |
| Browser UI or HTML deck testing | Playwright | Any selected browser framework | Treating Playwright as a PPTX renderer |

## Routing protocol

1. Identify deliverable: native editable PPTX, image-first PDF/pages, browser-native deck, or review-only.
2. Identify constraints: editability, fidelity, runtime, privacy/offline, accessibility, source-citation needs.
3. Select exactly one primary workflow skill; name bounded specialist roles where needed.
4. Declare the engine and renderer before asset/layout work.
5. Record a short decision in the run artifact and check that all chosen skills assume the same output mode.
6. If no compatible renderer is available, stop at a truthful storyboard/prototype or ask for an environment change; do not pretend export succeeded.

