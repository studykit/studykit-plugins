---
name: guard-state-root-untracked-dirs
description: Any "<project_dir>/.claude/guard/..." or ".codex/guard/..." untracked directory is guard's own state cache, not a mystery — resolvable via guard_hook.py.
metadata:
  type: project
---

`plugins/guard/scripts/guard_hook.py` defines `STATE_DIR_REL` as `.claude/guard`
(Claude) or `.codex/guard` (Codex) at `_state_root()` (guard_hook.py ~line 166-307).
Any untracked directory matching `<some_dir>/.claude/guard/{turns,extracts,state}/...`
found anywhere in the repo (not just the top-level `.claude/`) is guard writing its
own turn records / transcript extracts / session state under whatever `project_dir`
it was invoked with — e.g. `plugins/guard/.claude/guard/extracts/<session>/turn-*.md`
means guard_hook.py ran with `project_dir = plugins/guard` at some point (a test run,
a nested invocation, etc.), not a third-party artifact.

**Why:** an assistant turn claimed ignorance of such a directory and pushed the user
to investigate it themselves, when `_state_root`/`STATE_DIR_REL` in the same repo
names exactly what it is and why it appeared where it did.

**How to apply:** when a response defers "what created this `.claude/guard/...`
(or `.codex/guard/...`) directory" to the user, check `guard_hook.py`'s
`_state_root`/`STATE_DIR_REL`/`_turn_record_file` first — it is very likely
resolvable without asking the user.
