## workflow policy

Use `workflow-operator` for workflow operations before reading local workflow
cache snapshots or running provider commands yourself.

Workflow operations: issue status/completion checks, provider reads, comments,
lifecycle changes, relationships, metadata updates, provider-backed issue
writes, cache refreshes, write-back, authoring path discovery, and pending
provider draft path preparation.

Main assistant responsibilities:
- Ask `workflow-operator` for workflow operations and matching authoring paths. Specify the type, and the role (`issue` or `knowledge`) for dual-role or knowledge work; use the comment scope for comment-only updates.
- For new provider issues or comments, send `workflow-operator` the metadata (title, labels, issue type, relationship intent) so it can prepare a pending draft skeleton and return the draft path. `workflow-operator` records that metadata in the skeleton's frontmatter.
- After reading the returned authoring files, write the body content into the returned draft path. Edit only the body; do not touch the frontmatter.
- For new provider issues, stop after writing the body until the user explicitly approves provider creation. Then hand the draft path back with the publish/update intent. `workflow-operator` reads the path only to publish; it does not read the body content otherwise.

Operator responsibilities:
- Resolve authoring paths. Prepare pending provider draft skeletons from main-supplied metadata and return the draft paths.
- Perform the workflow operations listed above and verify results.
- Treat draft files as opaque provider payloads: read only for write-back or verification; never summarize, rewrite, or make authoring judgments.
- Return operational paths, refs, relationship metadata, and verification results without summarizing issue, comment, or knowledge content.

Types:
- Issue: `task`, `bug`, `spike`, `epic`, `review`. Dual-role with the `issue` role: `research`, `usecase`.
- Knowledge: `architecture`, `ci`, `context`, `domain`, `nfr`, `spec`. Dual-role with the `knowledge` role: `research`, `usecase`.
