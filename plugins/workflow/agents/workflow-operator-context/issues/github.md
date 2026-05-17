## configured issue commands

Use only the GitHub issue command family for this project:

```bash
ISSUE_FETCH=github_issue_fetch.py
ISSUE_DRAFTS=github_issue_drafts.py
ISSUE_LIFECYCLE=github_issue_lifecycle.py
ISSUE_WRITEBACK=github_issue_writeback.py
ISSUE_COMMENTS=github_issue_comments.py
ISSUE_RELATIONSHIPS=github_issue_relationships.py
ISSUE_METADATA=github_issue_metadata.py
```

Do not use another issue provider command family in this project.

Resolve authoring paths with `authoring_resolver.py`.
For comment-only requests, resolve authoring paths with the resolver's comment
scope so the caller reads only the Markdown and GitHub issue convention files.
Fetch or refresh issues with `$ISSUE_FETCH`.
Use `$ISSUE_LIFECYCLE close` or `$ISSUE_LIFECYCLE reopen` for supported provider
lifecycle mutations.
Prepare new issues as pending drafts with `$ISSUE_DRAFTS prepare`.
Create provider issues from drafts only after explicit user approval and
`--confirm-provider-create`.
Use `$ISSUE_WRITEBACK`, `$ISSUE_COMMENTS`, `$ISSUE_LIFECYCLE`,
`$ISSUE_RELATIONSHIPS`, and `$ISSUE_METADATA` for provider/cache mutations they
support.
Provider mutation scripts refresh affected cache projections internally.
If a mutation response has `status=blocked` and `reread_required=true`, stop and
tell the main agent to reread the listed cache paths before retrying.
If a requested provider operation is unsupported, return that limitation and
tell the main agent to decide whether to use a raw provider CLI outside the
operator. Do not guess another provider command.
