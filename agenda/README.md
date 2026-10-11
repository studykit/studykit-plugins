# agenda

A Claude Code mod (hooks module) that keeps a pane of what the session is discussing, so the topic
is not lost in a long conversation.

- **지금** — the topic being discussed now, set by the model with `agenda_focus`.
- **안건** — the open items, added with `agenda_add` (`decision: true` marks one the user must
  decide) and removed with `agenda_resolve`.
- `/agenda` opens the pane, `/agenda close` closes it; the status line shows `안건 N · 결정 M`.

`.claude-plugin/types/` is written by the engine when it loads the mod; `tsconfig.json` extends it
for `tsc -p agenda`. Install it with `/plugin install agenda@studykit-plugins`, or run the working
tree with `claude --plugin-dir <path to agenda>`.
