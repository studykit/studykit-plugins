## workflow policy

Use `workflow-operator` for workflow operations before reading local workflow
cache snapshots or running provider commands yourself.

Workflow operations include issue status/completion checks, provider reads,
comments, lifecycle changes, relationships, metadata updates, provider-backed
issue writes, cache refreshes, write-back, authoring path discovery, and
pending provider draft path preparation.

Main assistant responsibilities:
- Ask `workflow-operator` for workflow operations.
- Read and interpret returned local files or provider cache paths directly when content understanding is needed.
- Draft issue titles, bodies, labels, comments, and knowledge document content locally after reading the required authoring files.
- Write provider-backed issue or comment drafts to editable draft paths returned by `workflow-operator`; pass draft paths and explicit publish or update intent back for provider writes.
- Pass any issue relationship intent from the user request or authoring guidance to `workflow-operator` explicitly; do not rely on the operator to infer relationships from prose.
- Edit knowledge documents directly in the working tree after the target file and authoring paths are resolved.

Operator responsibilities:
- Resolve authoring paths and prepare pending provider draft paths.
- Perform provider/cache reads, refreshes, comments, lifecycle changes, explicitly supplied relationship changes, metadata updates, provider issue creation, write-back, and verification.
- Treat draft files as opaque provider payloads: read them only for write-back or verification, and never summarize, rewrite, or make authoring judgments about draft content.
- Return operational paths, refs, relationship metadata, and verification results without summarizing issue, comment, or knowledge content.

Authoring rules:
1. Before drafting or editing a workflow issue or knowledge document, ask `workflow-operator` for the matching authoring paths.
2. Tell it the type and, for dual-role types or knowledge work, the role (`issue` or `knowledge`).
3. For comment-only issue updates, request the comment-scope paths.
4. For new provider issues, ask `workflow-operator` to prepare the pending local draft and return the editable draft path.
5. After writing a pending provider issue draft locally, stop until the user explicitly approves provider issue creation.
6. After writing provider-backed issue or comment draft content locally, pass the draft path to `workflow-operator` to publish and verify.

Types:
- Issue: `task`, `bug`, `spike`, `epic`, `review`. Dual-role with the `issue` role: `research`, `usecase`.
- Knowledge: `architecture`, `ci`, `context`, `domain`, `nfr`, `spec`. Dual-role with the `knowledge` role: `research`, `usecase`.
