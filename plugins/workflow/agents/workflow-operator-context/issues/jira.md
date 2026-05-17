## configured issue commands

Use only the Jira issue command family for this project:

```bash
ISSUE_FETCH=jira_issue_fetch.py
ISSUE_DRAFTS=jira_issue_drafts.py
ISSUE_WRITEBACK=jira_issue_writeback.py
ISSUE_COMMENTS=jira_issue_comments.py
ISSUE_RELATIONSHIPS=jira_issue_relationships.py
ISSUE_METADATA=jira_issue_metadata.py
```

Do not use another issue provider command family in this project.

Resolve authoring paths with `authoring_resolver.py`.
Fetch or refresh issues with `$ISSUE_FETCH`.
Prepare new issues as pending drafts with `$ISSUE_DRAFTS prepare`.
Create provider issues from drafts only after explicit user approval and
`--confirm-provider-create`.
Use `$ISSUE_WRITEBACK`, `$ISSUE_COMMENTS`, `$ISSUE_RELATIONSHIPS`, and
`$ISSUE_METADATA` for provider/cache mutations they support.
Provider mutation scripts refresh affected cache projections internally.
If a mutation response has `status=blocked` and `reread_required=true`, stop and
tell the main agent to reread the listed cache paths before retrying.
If a requested provider operation is unsupported, return that limitation and
tell the main agent to decide whether to use a raw provider CLI outside the
operator. Do not guess another provider command.
