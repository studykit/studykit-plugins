## github — publish a new issue

```bash
workflow issue new \
  --type <task|bug|spike|epic|review|usecase|research> \
  --title <title> \
  --body-file <path> \
  [--label <label> ...] \
  [--state open|closed] \
  [--state-reason completed|not_planned|reopened] \
  [--assignee <user>] \
  [--parent <ref>] [--blocked-by <ref> ...] [--blocking <ref> ...] \
  [--child <ref> ...] \
```

Required: `--type`, `--title`, `--body-file`. `--state` defaults to
`open`. Relationship flags are add-only on publish and apply after the
create succeeds. `--assignee me` resolves the current GitHub login via
`gh api user`; clear assignees later with `workflow issue unassign
<ref>`.

See `../issue-write/github.md` for the shared body-bearing write
procedure.
