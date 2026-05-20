```bash
"$WORKFLOW" github_issue_fetch.py <ref> [<ref> ...] \
  [--cache-policy default|refresh]
```

Default cache policy reuses the cached `issue.md` projection when fresh;
pass `--cache-policy refresh` to force a remote re-read. The script emits a
JSON payload with each issue's cache path, title, state, and `cache_hit` —
open `issue.md` for the body and frontmatter. Never edit `issue.md` in place.
