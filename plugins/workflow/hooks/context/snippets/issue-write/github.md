Backend-only extras for GitHub issues:

- `issue_drafts.py publish` accepts `--assignee <user>` (or `--assignee me`) to set the assignee at create time.
- `issue_writeback.py update` accepts `--state open|closed` and `--state-reason completed|not_planned|reopened` for state changes.
- `issue_fields.py` subcommands include the static verbs `close <ref>`, `reopen <ref>`, `assign <ref> me`, `unassign <ref>`, and `set-type <ref> <new-type>`.

```bash
# Close, reopen, assign, unassign, or change the workflow-type label
"$WORKFLOW" issue_fields.py close <ref>
"$WORKFLOW" issue_fields.py assign <ref> me
"$WORKFLOW" issue_fields.py set-type <ref> bug
```
