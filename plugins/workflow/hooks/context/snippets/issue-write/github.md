Backend-only extras for GitHub issues:

- `issue.py new` accepts `--assignee <user>` (or `--assignee me`) to set the assignee at create time.
- `issue.py update` accepts `--state open|closed` and `--state-reason completed|not_planned|reopened` for state changes.
- `issue.py state <ref> close|reopen` covers the lifecycle verbs; `issue.py assign <ref> me`, `issue.py unassign <ref>`, and `issue.py set-type <ref> <new-type>` cover the static field verbs.

```bash
# Close, reopen, assign, unassign, or change the workflow-type label
"$WORKFLOW" issue.py state <ref> close
"$WORKFLOW" issue.py assign <ref> me
"$WORKFLOW" issue.py set-type <ref> bug
```
