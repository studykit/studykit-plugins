## jira — update an existing issue

```bash
workflow issue update \
  --issue <KEY> \
  --body-file <path> \
  [--type <task|bug|...>] \
  [--title <title>] \
  [--add-label <label> ...] [--remove-label <label> ...] \
  [--set-labels <label,label,...>] \
  [--state <verb>] \
```

Required: `--issue`, `--body-file`. At least one of body, title,
labels, or state must change. `--add-label` / `--remove-label` are
repeatable; `--set-labels` takes a single comma-separated list and
replaces the entire label set (mixing it with `--add-label` or
`--remove-label` errors). `--state` is the same free-form verb
described under comment append.

See `../issue-write/jira.md` for the shared body-bearing write
procedure and `../issue-link/jira.md` for relationship semantics.
