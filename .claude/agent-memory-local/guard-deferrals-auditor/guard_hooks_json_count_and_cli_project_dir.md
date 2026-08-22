---
name: guard-hooks-json-count-and-cli-project-dir
description: Two guard facts answerable by static reading, that a turn deferred as "untested" or "not verified" instead of resolving from the repo.
metadata:
  type: reference
---

Two recurring guard deferrals that are actually resolvable by reading the repo, not by
running a live host/session:

1. **"Does `Registered N hooks` match hooks.json 1:1?"** — count top-level hook-command
   entries in `plugins/guard/hooks/hooks.json` directly: sum, over each event, the number of
   matcher blocks, and separately the number of inner `"hooks"` array entries per block. As
   of the 0.53.0-era file: `UserPromptSubmit`(1) + `UserPromptExpansion`(5 matchers) +
   `PostToolUse`(1) + `Stop`(1) + `SessionStart`(1) = 9 matcher blocks, each with exactly one
   inner hook command = 9 total. No host log needed to confirm the count is a clean 1:1
   correspondence — only arithmetic on the JSON.

2. **"Does the `_project_dir` stale-`GUARD_PROJECT_DIR` contamination bug (nested `claude`
   session inherits the parent's exported project dir) also affect `settings set`?"** —
   readable from `plugins/guard/scripts/guard_core/paths.py` (`_cli_project_dir`, which reads
   `GUARD_PROJECT_DIR` before `CLAUDE_PROJECT_DIR`, by design, per its own docstring) plus
   `plugins/guard/scripts/guard_core/cmd_settings.py` (imports and uses `_cli_project_dir`).
   The mechanism is identical to bug A's: a nested session's Bash still holds the outer
   session's exported `GUARD_PROJECT_DIR`, so `settings set` run from inside it would resolve
   to the wrong project. This doesn't need a live nested-session test to establish as a
   structural fact — the code path is fully traceable statically. (A turn that leaves this as
   "이번에 시험하지 않았다" without tracing `cmd_settings.py` is deferring a resolvable fact.)

See [[async_agent_status_not_deferral]] for the general boundary: genuine runtime-behavior
claims across *different hosts/configs not present in this repo* (e.g. "does some other
host's Bash env ever contain `CLAUDE_PROJECT_DIR`?") remain legitimately unverified — only
the in-repo structural facts above are resolvable by reading code.
