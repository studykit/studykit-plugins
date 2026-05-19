```bash
"$WORKFLOW" jira_issue_fetch.py <KEY> [<KEY> ...] \
  [--cache-policy default|refresh] [--json]
```

Default cache policy reuses the cached `snapshot.md` projection when fresh;
pass `--cache-policy refresh` to force a remote re-read. Without `--json`
the output lists each issue's cache path — read `snapshot.md` for body and
frontmatter (title, state). Add `--json` only when you need to branch on
`state`, `cache_hit`, or title without opening the cache file. Never edit
`snapshot.md` in place.
