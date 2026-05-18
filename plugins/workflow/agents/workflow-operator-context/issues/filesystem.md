## configured issue commands

No provider issue command family is configured for filesystem issues.
Resolve authoring paths with `$AUTHORING_RESOLVER --type <type> --role issue --json` when the caller asks about workflow issue content. The resolver returns absolute paths under `required_authoring_files`; pass those paths back to the caller without reading them.
For comment-only requests, add `--scope comment` so the caller reads only the Markdown and provider convention files.
