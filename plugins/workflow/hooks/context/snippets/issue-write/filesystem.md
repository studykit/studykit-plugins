Filesystem-backed issues have no provider-write scripts. Resolve the
authoring paths with `authoring_resolver.py` (see
`{{WORKFLOW_POLICY_DIR}}/authoring.md`) and edit the returned files
directly in the working tree. Do not call `github_issue_*.py` or
`jira_issue_*.py` for this project.

Most common shape — resolve then edit:

```bash
workflow authoring_resolver.py --type task
# Edit the returned files directly; commit through normal git.
```
