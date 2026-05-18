## workflow operator bootstrap

Use `$WORKFLOW` to invoke bundled workflow scripts. The launcher and the
`$AUTHORING_RESOLVER` path are persisted by SessionStart, and the launcher
owns Codex session translation; do not derive either from project layout or
inspect runtime-specific session files directly.
