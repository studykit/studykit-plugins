## jira — publish a new issue

```bash
spectrack issue new \
  --type <task|bug|spike|epic|review|usecase|research> \
  --title <title> \
  --body-file <path> \
  [--label <label> ...] \
  [--issue-type <jira-issue-type>] \
  [--subtask-parent <PARENT-KEY>] \
  [--epic-name <X>] \
  [--assignee <user>] \
  [--parent <KEY>] [--epic <KEY>] [--blocked-by <KEY> ...] [--blocking <KEY> ...] \
  [--child <KEY> ...] [--related <KEY-or-URL> ...] \
```

Required: `--type`, `--title`, `--body-file`. `--issue-type` overrides
the Jira issue type at create time. `--subtask-parent` publishes a
native Sub-task (see table below). Relationship flags are add-only on
publish and apply after the create succeeds.

`--assignee me` resolves the current Jira user via
`/rest/api/<v>/myself`; clear assignees later with `spectrack issue
unassign <KEY>`.

`--epic-name` overrides the Epic Name customfield and is valid only
with `--type epic` (defaults to `--title`). `--epic <KEY>` adds an
Epic Link after publish; rejected when `--type epic`. Epic create
requires `providers.issues.epic_fields.name` to be configured.

### Native Sub-task vs parent issue-link

`--subtask-parent` and `--parent` produce structurally different
issues. Pick by what the new issue should *be*:

| Flag                       | When the create happens | Effect on the new issue                                                          | Config requirement                                       |
|----------------------------|-------------------------|----------------------------------------------------------------------------------|----------------------------------------------------------|
| `--subtask-parent <KEY>`   | At create time          | Forces `issuetype=Sub-task` and sets Jira's native Sub-task parent to `<KEY>`.   | None beyond standard issue-create config.                |
| `--parent <KEY>`           | Post-create             | Adds an issue link to `<KEY>`. Issuetype is unchanged.                           | `providers.issues.relationship_mappings.parent` must be configured; publish fails after create otherwise. |

When unsure, inspect a sibling under the same parent: if existing
siblings are Sub-tasks, use `--subtask-parent`; otherwise `--parent`.

See `../issue-write/jira.md` for the shared body-bearing write
procedure.
