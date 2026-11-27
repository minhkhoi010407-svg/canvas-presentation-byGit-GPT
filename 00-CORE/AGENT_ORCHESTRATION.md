# Agent orchestration

Use a small, explicit role graph rather than invoking every included skill on every deck.

| Role | Input | Output | Preferred guidance |
|---|---|---|---|
| Brief analyst | Request, constraints | brief, audience shift, intended outcome | Knowledge Cat |
| Researcher | Brief and claim list | source ledger, evidence, uncertainty | project-owned research policy |
| Story architect | Verified facts | narrative spine, slide outline | Knowledge Cat; consulting-deck-expert when applicable |
| Art director | Story and audience | design contract, visual references | slide-visual-director or Presentation Skill |
| Asset planner | Design contract | asset inventory and rights notes | slide-visual-director |
| Slide author | Approved storyboard | canonical slide model | selected engine/framework skill |
| Restoration specialist | Reference deck/screenshots | measured reconstruction plan | ppt-pixel-restore |
| QA reviewer | Rendered output and reports | issue list, pass/fail, revisions | presentation-qa; Playwright for browser surfaces |

## Conflict resolution

1. User-specified requirements and safety/factual obligations are hard constraints.
2. Runtime feasibility and output format decide whether a skill's workflow is applicable.
3. Pick one primary skill; add a specialist only for a bounded stage.
4. Define explicit project-owned design and content contracts.
5. If guidance conflicts, document the choice and why; do not merge image-first and editable-first defaults implicitly.

Keep delegation artifacts typed: brief, evidence ledger, outline, art direction, asset plan, storyboard, render receipt, and QA report. Do not let downstream agents treat unverified model output as evidence.

