## github — append a comment

```bash
spec-track issue comment \
  --issue <ref> \
  --body-file <path> \
  [--type <type>] \
  [--state open|closed] \
  [--state-reason completed|not_planned|reopened] \
  [--overwrite] \
```

Required: `--issue`, `--body-file`. `--state` / `--state-reason` apply
an inline state change on the same call. `--overwrite` skips the
freshness check and replaces the provider copy (see the conflict flow
in `../issue-write/github.md`).

See `../issue-write/github.md` for the shared body-bearing write
procedure.
