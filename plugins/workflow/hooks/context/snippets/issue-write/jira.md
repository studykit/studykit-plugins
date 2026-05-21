Backend-only extras for Jira issues:

- `issue.py new` accepts `--epic-name <name>` (Epic-only; defaults to `--title`), `--subtask-parent <KEY>` to create a native Sub-task, `--issue-type <type>` for the create-time Jira issue type, `--project-key <PROJECT>` to override the project, and `--assignee <user>` (or `--assignee me`).
- `issue.py link` accepts the Epic-Link family `--epic <KEY>`, `--replace-epic <KEY>`, `--remove-epic` alongside the standard relationship flags.
- `issue.py update` and `issue.py comment` accept `--state <verb>` where `<verb>` is keyed in `providers.issues.state_transitions`.
- `issue.py state <KEY> <verb> [--comment ...]` runs any verb keyed in `providers.issues.state_transitions`; `issue.py assign <KEY> me`, `issue.py unassign <KEY>`, and `issue.py set-type <KEY> <new-type>` cover the static verbs.

```bash
# Publish a new Epic
"$WORKFLOW" issue.py new \
  --type epic --title "<title>" --body-file <body-path>

# Run a configured state transition, assign, unassign, or change the issuetype
"$WORKFLOW" issue.py state <KEY> <verb>
"$WORKFLOW" issue.py assign <KEY> me
"$WORKFLOW" issue.py set-type <KEY> bug

# Add a Jira-specific Epic Link relationship
"$WORKFLOW" issue.py link <KEY> --epic <KEY>
```
