Publish a `review` issue (used by the blocker-handling flow):

```bash
workflow issue new \
  --type review \
  --title <title> \
  --body-file <body-path>
```

Required: `--type`, `--title`, `--body-file`. The body file is the draft
path returned by `workflow authoring_resolver.py --type review`.
Capture the returned review ref from the script's JSON output.
