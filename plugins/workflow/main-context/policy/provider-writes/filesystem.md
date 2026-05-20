## filesystem issue writes

The configured issue provider is `filesystem`. Workflow issues are local
Markdown artifacts edited directly at the paths the authoring resolver
returns. There is no provider-backed publish, comment, update, or
relationship script.

## Flow

1. Resolve the authoring paths with `"$WORKFLOW" authoring_resolver.py
   --type <type> --role issue --json` (see `../authoring.md`).
2. Read and edit the returned files directly in the working tree.
3. Commit the changes through normal version control.

There is no body-file temp flow and no cache freshness check on the
filesystem path. Do not call `github_issue_*.py` or `jira_issue_*.py`
scripts on this project.
