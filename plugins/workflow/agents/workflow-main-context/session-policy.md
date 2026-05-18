## workflow policy

Use `workflow-operator` for workflow operations before reading local workflow
cache snapshots or running provider commands yourself.

Workflow operations: issue status/completion checks, provider reads, comments,
lifecycle changes, relationships, metadata updates, provider-backed issue
writes, cache refreshes, write-back, and authoring path discovery.

Main assistant responsibilities:
- Ask `workflow-operator` for workflow operations and matching authoring paths. Specify the type, and the role (`issue` or `knowledge`) for dual-role or knowledge work; use the comment scope for comment-only updates.

New provider issue flow:
1. Ask `workflow-operator` for matching authoring paths (specify type and, for dual-role types, role).
2. Read the returned authoring paths.
3. Write the issue body to a temp file you choose; body content only, no frontmatter.
4. Present the metadata and the draft body to the user. Wait for explicit publish approval.
5. After approval, hand `workflow-operator` the metadata (title, labels, issue type, role, relationship intent) and the temp file path with publish intent.
6. `workflow-operator` publishes, refreshes the cache, deletes the temp file on success, and returns the cached issue file path with the issue ref and success/failure. On failure the temp file is preserved for retry.

Operator responsibilities:
- Resolve authoring paths.
- Perform the workflow operations listed above and verify results.
- Treat caller-provided temp body files as opaque provider payloads: read only to publish or verify; never summarize, rewrite, or make authoring judgments.
- After a successful publish, refresh the cache, delete the temp file, and return the cached issue file path.
- Return operational paths, refs, relationship metadata, and verification results without summarizing issue, comment, or knowledge content.

Types:
- Issue: `task`, `bug`, `spike`, `epic`, `review`. Dual-role with the `issue` role: `research`, `usecase`.
- Knowledge: `architecture`, `ci`, `context`, `domain`, `nfr`, `spec`. Dual-role with the `knowledge` role: `research`, `usecase`.
