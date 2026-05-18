## configured issue commands

Use only the Jira issue command family for this project. Invoke each
script via the workflow launcher: `$WORKFLOW <script>.py ...`. The launcher
resolves single-name scripts against its own directory, so no path prefix
is needed.

Do not use another issue provider command family in this project.

### Authoring path resolution

Resolve authoring paths with `$AUTHORING_RESOLVER --type <type> --role issue --json`.
The resolver returns absolute paths under `required_authoring_files`; pass
those paths back to the caller without reading them.

For comment-only requests, add `--scope comment` so the caller reads only
the Markdown and Jira issue convention files.

### Fetch

- `$WORKFLOW jira_issue_fetch.py` — fetch or refresh issues.

### Publish a new issue

Publish with `$WORKFLOW jira_issue_drafts.py publish`. The caller supplies:

- Metadata flags: `--type`, `--title`, `--label`, plus `--issue-type` and
  `--subtask-parent` when the Jira issue type or sub-task parent must be set
  at create time.
- `--body-file <path>` — opaque body content, no frontmatter.

Publish only after explicit user approval. On success the script publishes,
refreshes the cache, deletes the body file, and returns the cached
`snapshot.md` path (surfaced as `issue_file` in the response) along with
the issue key and verified flag; return those to the caller. On failure the
body file is preserved so the caller can retry.

Apply relationships separately with `$WORKFLOW jira_issue_relationships.py`
against the freshly-published issue when the caller's metadata included
relationship intent.

### Other mutations

Use these for the remaining provider/cache mutations they support:

- `$WORKFLOW jira_issue_writeback.py`
- `$WORKFLOW jira_issue_comments.py`
- `$WORKFLOW jira_issue_relationships.py`
- `$WORKFLOW jira_issue_metadata.py`

### Error handling

- Provider mutation scripts refresh affected cache projections internally.
- If a mutation response has `status=blocked` and `reread_required=true`,
  stop and tell the main agent to reread the listed cache paths before
  retrying.
- If a requested provider operation is unsupported, return that limitation
  and tell the main agent to decide whether to use a raw provider CLI
  outside the operator. Do not guess another provider command.
