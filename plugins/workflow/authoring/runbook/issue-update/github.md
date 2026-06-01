## github — update an existing issue

```bash
workflow issue update \
  --issue <ref> \
  --body-file <path> \
  [--type <type>] \
  [--title <title>] \
  [--add-label <label> ...] [--remove-label <label> ...] \
  [--set-labels <label,label,...>] \
  [--state open|closed] \
  [--state-reason completed|not_planned|reopened] \
  [--parent <ref> | --replace-parent <ref> | --remove-parent] \
  [--blocked-by <ref> ...] [--remove-blocked-by <ref> ...] \
  [--blocking <ref> ...]  [--remove-blocking <ref> ...] \
  [--child <ref> ...]     [--remove-child <ref> ...] \
  [--overwrite] \
```

Required: `--issue`, `--body-file`. `--add-label` / `--remove-label`
are repeatable; `--set-labels` takes a single comma-separated list and
replaces the entire label set (mixing it with `--add-label` or
`--remove-label` errors). Relationship flags apply after the update
succeeds. `--overwrite` skips the freshness check and replaces the
provider copy (see the conflict flow in `../issue-write/github.md`).

See `../issue-write/github.md` for the shared body-bearing write
procedure and `../issue-link/github.md` for relationship semantics.
