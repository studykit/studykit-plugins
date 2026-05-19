Write operations — read `{{WORKFLOW_POLICY_DIR}}/provider-writes/jira.md`
first. `--help` shows flag syntax only; it does not cover the
`authoring_resolver.py` prereq, the body-file lifecycle, or freshness-drift
handling. Pick the script by intent:

- `jira_issue_drafts.py publish` — create a new issue (Epics use `--epic-name`; Sub-tasks use `--subtask-parent`)
- `jira_issue_comments.py append` — add a comment
- `jira_issue_writeback.py update` — change body, title, labels, or state
- `jira_issue_relationships.py` — add / remove / replace links, parent, or Epic Link
- `jira_issue_fields.py {close|reopen|assign|unassign|set-type}` — body-less change

Common shapes (resolver prereq is required for any body-file flow):

```bash
# Publish a new issue
"$WORKFLOW" authoring_resolver.py --type task --json
# Read the returned paths, draft the body to <body-path>, get user approval.
"$WORKFLOW" jira_issue_drafts.py publish \
  --type task --title "<title>" --body-file <body-path> --json

# Publish a new Epic (--epic-name optional; defaults to --title)
"$WORKFLOW" jira_issue_drafts.py publish \
  --type epic --title "<title>" --body-file <body-path> --json

# Update an existing issue body (add --state closed|open for a state change too)
"$WORKFLOW" jira_issue_writeback.py update \
  --type task --issue <KEY> --body-file <body-path> --json

# Add a relationship (also: --epic, --blocked-by, --blocking, --child, --related, --remove-*)
"$WORKFLOW" jira_issue_relationships.py <KEY> --parent <KEY> --json

# Close, reopen, assign, unassign, or change the issuetype
"$WORKFLOW" jira_issue_fields.py close <KEY> --json
"$WORKFLOW" jira_issue_fields.py assign <KEY> me --json
"$WORKFLOW" jira_issue_fields.py set-type <KEY> bug --json
```
