# Memory index

- [Async agent status is not a deferral](async_agent_status_not_deferral.md) — "will notify when the background agent finishes" isn't a resolvable fact-punt.
- [Guard state-root untracked dirs](guard_state_root_untracked_dirs.md) — stray `.claude/guard/...` (or `.codex/guard/...`) anywhere is guard's own cache; check `_state_root`/`STATE_DIR_REL` in guard_hook.py before deferring to the user.
- [Root agent-memory-local is tracked](reference_agent_memory_local_root_tracked.md) — `.gitignore` un-ignores root `.claude/agent-memory-local/`; whether to commit files there isn't the user's call.
- [guard hooks.json count / _cli_project_dir contamination](guard_hooks_json_count_and_cli_project_dir.md) — "9 hooks matches hooks.json?" and "does settings set share bug A's stale-env risk?" are both answerable by static code reading, not live testing.
- [Commit titles carry no issue ref](commit_title_convention_no_issue_ref.md) — titles are `guard: v<version> — <headline>`; "the issue ref is undecided" is a checkable and currently false reason not to commit.
