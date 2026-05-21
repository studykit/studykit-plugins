Backend-only extras for Jira issues:

- `issue_drafts.py publish` accepts `--epic-name <name>` (Epic-only; defaults to `--title`), `--subtask-parent <KEY>` to create a native Sub-task, `--issue-type <type>` for the create-time Jira issue type, `--project-key <PROJECT>` to override the project, and `--assignee <user>` (or `--assignee me`).
- `issue_relationships.py` accepts the Epic-Link family `--epic <KEY>`, `--replace-epic <KEY>`, `--remove-epic` alongside the standard relationship flags.
- `issue_writeback.py update` and `issue_comments.py append` accept `--state <verb>` where `<verb>` is keyed in `providers.issues.state_transitions`.
- `issue_fields.py` subcommands include the static verbs `assign <KEY> me`, `unassign <KEY>`, `set-type <KEY> <new-type>`, plus one dynamic `<verb> <KEY> [--comment ...]` subcommand per key in `providers.issues.state_transitions`.

```bash
# Publish a new Epic
"$WORKFLOW" issue_drafts.py publish \
  --type epic --title "<title>" --body-file <body-path>

# Run a configured state transition, assign, unassign, or change the issuetype
"$WORKFLOW" issue_fields.py <verb> <KEY>
"$WORKFLOW" issue_fields.py assign <KEY> me
"$WORKFLOW" issue_fields.py set-type <KEY> bug

# Add a Jira-specific Epic Link relationship
"$WORKFLOW" issue_relationships.py <KEY> --epic <KEY>
```
