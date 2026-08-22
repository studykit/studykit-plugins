# Memory index

- [guard_hook.py comment style](guard-hook-py-style.md) — this file's comments are almost entirely rationale/hazard-grade prose; near-zero redundant-comment findings expected.
- [guard dead constant](guard-hook-py-dead-constant.md) — RESOLVED: `_CLI_MUTATING_VERBS` no longer exists as of 2026-08-22.
- guard trace.log sweep — RESOLVED as of 2026-08-22: `cmd_session_start` now unlinks `_trace_file(project_dir)` past the age cutoff; the old "never swept" defect memory was deleted.
