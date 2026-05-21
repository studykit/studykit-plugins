```bash
workflow issue fetch <issue> [<issue> ...] \
  [--cache-policy default|refresh]
```

Default cache policy reuses the cached `issue.md` projection when fresh;
pass `--cache-policy refresh` to force a remote re-read. The script emits a
JSON payload with a shared `basedir` and an `issues` array; each entry holds
the basedir-relative `issue` path, `title`, `state`, `cache_refreshed`, and
(when present) basedir-relative `comments` paths — open `issue.md` for the
body and frontmatter. `cache_refreshed` is `false` when the call reused the
cached projection and `true` when this op pulled fresh data from the
provider. Never edit `issue.md` in place.
