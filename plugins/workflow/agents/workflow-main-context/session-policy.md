## workflow policy

Delegate workflow operations to `workflow-operator` before reading local
workflow cache snapshots or running provider commands yourself.

Workflow operations: issue status/completion checks, provider reads,
comments, lifecycle changes, relationships, metadata updates,
provider-backed issue writes, cache refreshes, write-back, and authoring
path discovery.

### Authoring path resolution

Ask `workflow-operator` for matching authoring paths. Specify the type
(see Types) and, for dual-role types, the role (`issue` or `knowledge`).
Use the comment scope for comment-only updates. Read the returned paths
yourself before drafting a provider-backed change.

### Provider writes

The three provider-write intents — publish a new issue, append a comment,
and update an existing issue body — share one shape:

1. Resolve and read the authoring paths.
2. Write the body to a temp file you choose; body content only, no
   frontmatter. The cached `issue.md` body is read-only — do not edit it
   in place when updating.
3. Present the metadata, issue ref (when applicable), and draft body to
   the user and wait for explicit approval.
4. Hand `workflow-operator` the temp file path with the write intent
   (publish, append, or update), the required refs, and any optional
   metadata, state change, or relationship intent.
5. The operator runs the required freshness check, applies the mutation,
   refreshes the cache, deletes the temp file on success, and returns the
   cached `issue.md` path with the issue ref and verification result. On
   freshness drift it returns `status=blocked` with the cache paths to
   reread; reread them and retry. Relationship intent triggers a
   follow-up relationship apply step.

### Types

- Issue: `task`, `bug`, `spike`, `epic`, `review`. Dual-role with the
  `issue` role: `research`, `usecase`.
- Knowledge: `architecture`, `ci`, `context`, `domain`, `nfr`, `spec`.
  Dual-role with the `knowledge` role: `research`, `usecase`.
