```bash
"$WORKFLOW" jira_issue_fetch.py <KEY> [<KEY> ...] \
  [--cache-policy default|refresh]
```

Default cache policy reuses the cached `issue.md` projection when fresh;
pass `--cache-policy refresh` to force a remote re-read. The script emits a
JSON payload with each issue's cache path, title, state, `cache_hit`, and
any sibling `comment-*.md` paths — read `issue.md` for the issue body and
frontmatter (title, state, labels, `remote_links`, `relationships`) and each
`comment-*.md` file for one cached comment. Never edit `issue.md` or
`comment-*.md` in place.
