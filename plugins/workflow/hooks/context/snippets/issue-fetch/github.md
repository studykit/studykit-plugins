```bash
"$WORKFLOW" github_issue_fetch.py <ref> [<ref> ...] \
  [--cache-policy default|refresh]
```

Default cache policy reuses the cached `issue.md` projection when fresh;
pass `--cache-policy refresh` to force a remote re-read. The script emits a
JSON payload with a shared `basedir` and an `issues` array; each entry holds
the basedir-relative `issue` path, `title`, `state`, `cache_hit`, and (when
present) basedir-relative `comments` paths — open `issue.md` for the body
and frontmatter. Never edit `issue.md` in place.
