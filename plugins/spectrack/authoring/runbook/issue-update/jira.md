## jira — update an existing issue

```bash
spectrack issue update \
  --issue <KEY> \
  --body-file <path> \
  [--type <task|bug|...>] \
  [--title <title>] \
  [--add-label <label> ...] [--remove-label <label> ...] \
  [--set-labels <label,label,...>] \
  [--state <verb>] \
  [--overwrite] \
```

Required: `--issue`, `--body-file`. At least one of body, title,
labels, or state must change. `--add-label` / `--remove-label` are
repeatable; `--set-labels` takes a single comma-separated list and
replaces the entire label set (mixing it with `--add-label` or
`--remove-label` errors). `--state` is the same free-form verb
described under comment append. `--overwrite` skips the freshness check
and replaces the provider copy (see the conflict flow in
`../issue-write/jira.md`).

To change only part of an existing body, seed the temp `--body-file`
from the cached `issue.md` (the provider-normalized current body) and
edit just the affected sections — do not re-author the whole body.

See `../issue-write/jira.md` for the shared body-bearing write
procedure and `../issue-link/jira.md` for relationship semantics.
