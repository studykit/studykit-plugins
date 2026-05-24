# UI Screen Grouping

After several UI-related use cases are confirmed in the session,
group them by screen so the design surface is visible end-to-end.
This procedure is optional — only run it when the user explicitly
asks for screen grouping or when discovery has produced 3+ UI use
cases the user wants to see together.

The skill never edits a curated knowledge page from this procedure.
Screen narrative belongs to the `context` knowledge page (Screens
section) per
`${CLAUDE_PLUGIN_ROOT}/authoring/common/usecase-issue-authoring.md`'s
knowledge side-effects table; surface it as a `review` item per
`./knowledge-side-effects.md` when grouping reveals a screen that the
context page does not yet name.

## Procedure

For each screen the user names:

1. **Pick a group label** — short kebab-case, e.g.,
   `screen-dashboard`, `screen-meeting-detail`. Use the same label
   across every use case that belongs to the screen.
2. **Apply the label to participating `usecase` issues.** Use the
   provider's labelling form via `workflow issue update` (verb syntax
   at `<runbook>`'s `issue-update` intent). When the backend doesn't
   support custom labels for this issue type, append a comment on
   each participating issue naming the screen group instead — comment
   syntax at `<runbook>`'s `issue-comment` intent.
3. **Record the screen narrative.** When the `context` knowledge
   page does not yet describe this screen, file a `review` item per
   `./knowledge-side-effects.md` targeting `context`. The `review`
   body's `Suggested Fix` should sketch the screen's purpose, the
   use cases that compose it, and the navigation flow between them.

## Mock generation (optional)

For each confirmed screen group, optionally generate an HTML mock so
the user can react to a concrete visual.

1. Confirm with the user that a mock is wanted; mocks are
   throwaway, not deliverables.
2. Dispatch `Agent(subagent_type: "workflow:mock-html-generator")`
   with:
   - The participating `usecase` issue refs (the agent will fetch them
     via `workflow issue fetch`).
   - The screen-group label.
   - Layout requirements (the user's wording verbatim).
   - An absolute output directory under
     `/tmp/workflow-mocks/<screen-slug>/`.
3. After the agent returns the output path, present the mock to the
   user (file path they can open in a browser). Gather feedback.
4. **Reflect mock feedback into use cases** the same way as research:
   either through a follow-up question in the discovery loop or, when
   the change concerns a knowledge surface, a side-effect `review`
   item. Do not edit `usecase` issue bodies in place from mock
   feedback alone — re-confirm with the user first.

## Anti-patterns

- Grouping unrelated use cases under one screen because the user
  mentioned them in the same breath. The grouping rule is shared
  visual surface, not topical proximity.
- Treating a mock as a use case deliverable. Mocks support
  discovery; the durable artifact is the use case issue and any
  `review` items it spawned.
- Letting the screen narrative live only in the session
  conversation. If it matters to the product, it belongs in a
  `review` item targeting `context` — otherwise the screen story is
  lost when the session ends.
