## github — fetch issues

```bash
workflow issue fetch <issue> [<issue> ...] \
  [--cache-policy default|refresh]
```

The script returns paths to local `issue.md` (and any
`comment-*.md`) projections — open those files to read the body and
frontmatter. Default cache policy reuses the local copy when fresh;
pass `--cache-policy refresh` to force a remote re-read. Never edit
the returned files in place.

References are GitHub issue numbers or configured-repo references
(e.g., `123`, `#123`, `<owner>/<repo>#123`,
`https://github.com/<owner>/<repo>/issues/123`).
