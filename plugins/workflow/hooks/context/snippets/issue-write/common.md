Write operations — read `{{WORKFLOW_POLICY_DIR}}/provider-writes/{{WORKFLOW_ISSUE_PROVIDER}}.md`
first. `--help` shows flag syntax only; it does not cover the
`authoring_resolver.py` prereq, the body-file lifecycle, or freshness-drift
handling. Pick the script by intent:

- `issue_drafts.py publish` — create a new issue
- `issue_comments.py append` — add a comment
- `issue_writeback.py update` — change body, title, labels, or state
- `issue_relationships.py` — add / remove / replace links
- `issue_fields.py` — body-less change (close, reopen, assign, unassign, set-type, or a configured state transition)

Common shapes (resolver prereq is required for any body-file flow):

```bash
# Publish a new issue
"$WORKFLOW" authoring_resolver.py --type task
# Read the returned paths, draft the body to <body-path>, get user approval.
"$WORKFLOW" issue_drafts.py publish \
  --type task --title "<title>" --body-file <body-path>

# Update an existing issue body
"$WORKFLOW" issue_writeback.py update \
  --type task --issue <issue> --body-file <body-path>

# Add a relationship (also: --blocked-by, --blocking, --child, --related, --remove-*)
"$WORKFLOW" issue_relationships.py <issue> --parent <issue>
```

Each dispatcher loads `.workflow/config.yml`, dispatches to the configured
backend, and gates its `--help` to the active backend's option surface;
backend-exclusive flags from the other provider are hidden.
