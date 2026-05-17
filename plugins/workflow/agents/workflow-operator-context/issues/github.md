## configured issue commands

Use only the GitHub issue command family for this project:

```bash
ISSUE_PROVIDER=workflow_github.py
ISSUE_FETCH=github_issue_fetch.py
ISSUE_DRAFTS=github_issue_drafts.py
ISSUE_WRITEBACK=github_issue_writeback.py
ISSUE_COMMENTS=github_issue_comments.py
ISSUE_RELATIONSHIPS=github_issue_relationships.py
ISSUE_METADATA=github_issue_metadata.py
```

Do not use another issue provider command family in this project.

Resolve authoring paths with `authoring_resolver.py`.
Fetch or refresh issues with `$ISSUE_FETCH`.
Use `$ISSUE_PROVIDER close` or `$ISSUE_PROVIDER reopen` for supported provider
lifecycle mutations.
Prepare new issues as pending drafts with `$ISSUE_DRAFTS prepare`.
Create provider issues from drafts only after explicit user approval and
`--confirm-provider-create`.
Use `$ISSUE_WRITEBACK`, `$ISSUE_COMMENTS`, `$ISSUE_RELATIONSHIPS`, and
`$ISSUE_METADATA` for provider/cache mutations they support.
After any provider state mutation, run `$ISSUE_FETCH` with
`--cache-policy refresh` for the affected issues so cache projections match the
provider.
If a requested provider operation is unsupported, return that limitation instead
of guessing another provider command.
