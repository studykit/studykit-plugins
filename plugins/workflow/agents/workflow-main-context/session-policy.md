## workflow policy

When you need to draft or edit a workflow issue or knowledge document:

1. Ask `workflow-operator` for the matching authoring paths first. Tell it the type and, for dual-role types or knowledge work, the role (`issue` or `knowledge`). For comment-only issue updates, request the comment-scope paths.
2. Read the returned files locally before drafting any content.
3. Workflow issues: draft title, body, and labels locally, then hand the result to `workflow-operator`; it publishes and verifies the provider update.
4. Knowledge documents: edit the chosen file directly in the working tree — no operator publish step.
5. New workflow issues: stop at the pending local draft until the user explicitly approves provider issue creation.

Types:
- Issue: `task`, `bug`, `spike`, `epic`, `review`. Dual-role with the `issue` role: `research`, `usecase`.
- Knowledge: `architecture`, `ci`, `context`, `domain`, `nfr`, `spec`. Dual-role with the `knowledge` role: `research`, `usecase`.
