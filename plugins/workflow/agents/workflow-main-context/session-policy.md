## workflow policy

Use `workflow-operator` for workflow operations before reading local workflow
cache snapshots or running provider commands yourself.

Workflow operations: issue status/completion checks, provider reads, comments,
lifecycle changes, relationships, metadata updates, provider-backed issue
writes, cache refreshes, write-back, authoring path discovery, and pending
provider draft path preparation.

Main assistant responsibilities:
- Ask `workflow-operator` for workflow operations and matching authoring paths. Specify the type, and the role (`issue` or `knowledge`) for dual-role or knowledge work; use the comment scope for comment-only updates.
- After reading the returned authoring files, write provider-backed issue or comment body content into the editable draft path returned by `workflow-operator`. Edit only the body of the draft file; do not modify the frontmatter.
- Pass title, labels, issue type, relationship intent, publish/update intent, and other operational metadata as explicit parameters when asking `workflow-operator` to create or update.
- For new provider issues, stop after writing the local draft until the user explicitly approves provider creation. Then hand the draft path to `workflow-operator` to publish and verify.

Operator responsibilities:
- Resolve authoring paths and prepare pending provider draft paths.
- Perform the workflow operations listed above and verify results.
- Treat draft files as opaque provider payloads: read only for write-back or verification; never summarize, rewrite, or make authoring judgments.
- Return operational paths, refs, relationship metadata, and verification results without summarizing issue, comment, or knowledge content.

Types:
- Issue: `task`, `bug`, `spike`, `epic`, `review`. Dual-role with the `issue` role: `research`, `usecase`.
- Knowledge: `architecture`, `ci`, `context`, `domain`, `nfr`, `spec`. Dual-role with the `knowledge` role: `research`, `usecase`.
