# Memory index

- [Async agent status is not a deferral](async_agent_status_not_deferral.md) — "will notify when the background agent finishes" isn't a resolvable fact-punt.
- [Guard state-root untracked dirs](guard_state_root_untracked_dirs.md) — stray `.claude/guard/...` (or `.codex/guard/...`) anywhere is guard's own cache; check `_state_root`/`STATE_DIR_REL` in guard_hook.py before deferring to the user.
- [Root agent-memory-local is tracked](reference_agent_memory_local_root_tracked.md) — `.gitignore` un-ignores root `.claude/agent-memory-local/`; whether to commit files there isn't the user's call.
