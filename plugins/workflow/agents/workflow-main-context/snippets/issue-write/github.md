Write operations — read `{{WORKFLOW_POLICY_DIR}}/provider-writes/github.md`
first. `--help` shows flag syntax only; it does not cover the
`authoring_resolver.py` prereq, the body-file lifecycle, or freshness-drift
handling. Pick the script by intent:

- `github_issue_drafts.py publish` — create a new issue
- `github_issue_comments.py append` — add a comment
- `github_issue_writeback.py update` — change body, title, labels, or state
- `github_issue_relationships.py` — add / remove / replace links
- `github_issue_metadata.py` — metadata-only change
- `github_issue_lifecycle.py close|reopen` — state-only change

Common shapes (resolver prereq is required for any body-file flow):

```bash
# Publish a new issue
"$WORKFLOW" authoring_resolver.py --type task --json
# Read the returned paths, draft the body to <body-path>, get user approval.
"$WORKFLOW" github_issue_drafts.py publish \
  --type task --title "<title>" --body-file <body-path> --json

# Update an existing issue body
"$WORKFLOW" github_issue_writeback.py update \
  --type task --issue <ref> --body-file <body-path> --json

# Add a relationship (also: --blocked-by, --blocking, --child, --related, --remove-*)
"$WORKFLOW" github_issue_relationships.py <ref> --parent <ref> --json

# Close or reopen
"$WORKFLOW" github_issue_lifecycle.py close <ref> --json
```
