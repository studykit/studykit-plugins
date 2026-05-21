Write operations — read `{{WORKFLOW_POLICY_DIR}}/provider-writes/{{WORKFLOW_ISSUE_PROVIDER}}.md`
first. `--help` shows flag syntax only; it does not cover the
`authoring_resolver.py` prereq, the body-file lifecycle, or freshness-drift
handling. Every issue operation runs through the unified
`workflow issue` dispatcher; pick the subcommand by intent:

- `issue.py new` — create a new issue
- `issue.py comment` — add a comment
- `issue.py update` — change body, title, labels, or state
- `issue.py link` — add / remove / replace links
- `issue.py state | assign | unassign | set-type` — body-less change (close, reopen, assign, unassign, set-type, or a configured state transition)

Common shapes (resolver prereq is required for any body-file flow):

```bash
# Publish a new issue
workflow authoring_resolver.py --type task
# Read the returned paths, draft the body to <body-path>, get user approval.
workflow issue new \
  --type task --title "<title>" --body-file <body-path>

# Update an existing issue body
workflow issue update \
  --type task --issue <issue> --body-file <body-path>

# Add a relationship (also: --blocked-by, --blocking, --child, --related, --remove-*)
workflow issue link <issue> --parent <issue>
```

`issue.py` loads `.workflow/config.yml`, dispatches to the configured
backend, and gates each subcommand's `--help` to the active backend's
option surface; backend-exclusive flags from the other provider are
hidden.
