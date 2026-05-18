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
For comment-only requests, resolve authoring paths with the resolver's comment
scope so the caller reads only the Markdown and Jira issue convention files.
Fetch or refresh issues with `$ISSUE_FETCH`.
Publish new provider issues with `$ISSUE_DRAFTS publish`. The caller supplies
the metadata (`--type`, `--title`, `--label`, plus `--issue-type` and
`--subtask-parent` when the Jira issue type or sub-task parent must be set at
create time) and an opaque body file path (`--body-file`); the file must not
contain frontmatter. Publish only after explicit user approval. On success
the script publishes, refreshes the cache, deletes the body file, and returns
the cached `snapshot.md` path (surfaced as `issue_file` in the response)
along with the issue key and verified flag; return those to the caller. On
failure the body file is preserved so the caller can retry.
Apply relationships separately with `$ISSUE_RELATIONSHIPS` against the
freshly-published issue when the caller's metadata included relationship
intent.
Use `$ISSUE_WRITEBACK`, `$ISSUE_COMMENTS`, `$ISSUE_RELATIONSHIPS`, and
`$ISSUE_METADATA` for provider/cache mutations they support.
Provider mutation scripts refresh affected cache projections internally.
If a mutation response has `status=blocked` and `reread_required=true`, stop and
tell the main agent to reread the listed cache paths before retrying.
If a requested provider operation is unsupported, return that limitation and
tell the main agent to decide whether to use a raw provider CLI outside the
operator. Do not guess another provider command.
