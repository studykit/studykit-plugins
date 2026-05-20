```bash
"$WORKFLOW" jira_issue_fetch.py <KEY> [<KEY> ...] \
  [--cache-policy default|refresh] [--json]
```

Default cache policy reuses the cached `issue.md` projection when fresh;
pass `--cache-policy refresh` to force a remote re-read. Without `--json`
the output lists each issue's cache path plus any sibling `comment-*.md`
files — read `issue.md` for the issue body and frontmatter (title,
state, labels, `remote_links`, `relationships`) and each `comment-*.md`
file for one cached comment. Add `--json` only when you need to branch on
`state`, `cache_hit`, or title without opening the cache file. Never edit
`issue.md` or `comment-*.md` in place.
