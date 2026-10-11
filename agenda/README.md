# agenda

A Claude Code mod (hooks module) that keeps a pane of what the session is discussing, so the topic
is not lost in a long conversation.

- **지금** — the topic being discussed now, set by the model with `agenda_focus`.
- **안건** — the open items, added with `agenda_add` (`decision: true` marks one the user must
  decide) and removed with `agenda_resolve`.
- `/agenda` opens the pane, `/agenda close` closes it; the status line shows `안건 N · 결정 M`.
- `/agenda band` moves the list to the band right above the prompt, `/agenda pane` back to its own pane; the choice is kept across sessions.
- Each session's items and topic are saved in the plugin's store under the session id, so `claude --resume` brings them back; `/clear` starts an empty agenda. Entries untouched for 30 days are dropped.
- Where the pane itself sits is Claude Code's: docked beside the transcript in the fullscreen layout from 110 columns, else inline above the prompt.

`.claude-plugin/types/` is written by the engine when it loads the mod; `tsconfig.json` extends it
for `tsc -p agenda`. Install it with `/plugin install agenda@studykit-plugins`, or run the working
tree with `claude --plugin-dir <path to agenda>`.
