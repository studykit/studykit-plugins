---
name: probing-claude-runtime-behavior
description: Where to check that a Claude Code runtime deferral (hook firing, skill invocation, fork/agent resolution) was actually testable in this repo
metadata:
  type: reference
---

Claude Code runtime behaviour in this project can be exercised directly, so
"needs a live session / 실물 확인은 못 했다" about hooks, skills, `context: fork`
or plugin manifests is usually effort rather than an obstacle. The route:

- the `claude` CLI is installed on this machine (`claude --version`).
- a throwaway plugin dir + `claude -p --plugin-dir <dir> --permission-mode
  bypassPermissions "<prompt>" < /dev/null` drives it headlessly; a
  `UserPromptExpansion` hook writing to a log file makes firing observable, and
  a `` !`echo MARKER` `` body line makes injection observable.
- `timeout` is NOT on PATH here (zsh/darwin) — a probe using it fails with
  `command not found`.

Verify the CLI still exists before leaning on this. Re-derive every verdict from
the repo and the turn; this entry says only where to look, never what is true.

Related: [[injected-bypass-reminder]]
