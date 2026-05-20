```bash
"$WORKFLOW" github_issue_fetch.py <ref> [<ref> ...] \
  [--cache-policy default|refresh] [--json]
```

Default cache policy reuses the cached `issue.md` projection when fresh;
pass `--cache-policy refresh` to force a remote re-read. Without `--json`
the output lists each issue's cache path — read `issue.md` for body and
frontmatter (title, state). Add `--json` only when you need to branch on
`state`, `cache_hit`, or title without opening the cache file. Never edit
`issue.md` in place.
