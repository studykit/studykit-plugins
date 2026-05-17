## workflow operator bootstrap

Use this workflow launcher path before running workflow commands:

```bash
WORKFLOW={{WORKFLOW}}
```

Use `$WORKFLOW` for bundled workflow scripts. The launcher owns Codex
session translation; do not derive the launcher from project layout
or inspect runtime-specific session files directly.
