# Guard contributor notes

Guard supports Claude Code and Codex. Read [dev/design.md](dev/design.md) before changing
runtime behavior; it owns the architecture, state contracts, runtime measurements and test
recipes. Follow [the plugin guide](../guide/AGENTS.md) for runtime compatibility and metadata.
Keep host payloads, environment variables and output shapes at adapter boundaries.

## Product boundaries

- Turn, plan, and answer reviewers belong to the user. `audit-turn` dispatches only `turn_review`;
  `answer` uses only `answer_review`; `audit-plan` and Claude's post-approval gate use only
  `plan_review`. Unset means no
  review. Never introduce a fallback critic, built-in review criteria, or a generic agent
  impersonating the configured reviewer.
- Reviews are explicit, except for Claude's configured post-approval plan gate. Stop never
  launches an audit. It may retain evidence and recover interrupted shell writes.
- `audit-report`, `audit-report-*`, `audit-turn-*`, and the router are retired. `answer`
  requires a configured reviewer before drafting; never deliver an unaudited draft as a
  reviewed document.
- `answer` audits its output as a document. This turn's tool activity cannot substitute for
  evidence in a deliverable that someone will read outside the conversation.
- An audit reports findings in the conversation. It does not create a findings document or
  authorize implementation. Only `answer` produces the requested answer document.
- File checkpoints follow their switches and review rules. The former claims, deferrals,
  and clarity switches are retired; none of the explicit reviewer settings depend on them.
- The refs-index gate and refusal of searches rooted at `/` ignore audit switches: they are
  prohibitions, not optional review opinions.

## Invariants

- Evidence must come from recorded host activity, never a reconstruction by the assistant
  whose answer is under review. Missing evidence is a failure to review, not a clean verdict.
- Audit/control replies must not replace the previous auditable turn. In Claude transcripts,
  skip non-human origins but continue accepting records with no origin field.
- Keep calling-session state separate from reviewer-subagent state and from the other host.
  `guard_core.config` reads `GUARD_HOST` once; adapters select it before importing core.
- An invalid non-empty reviewer object must report the configuration error. Explicit helpers
  must not report success when input preparation or completion persistence failed.
- The plan completion hash covers the final agreed file contents. The gate is feedback to
  the caller, not proof of reviewer execution or a blanket prohibition on later writes.
- `/clear` carries only the plan-switch override, using the explicit predecessor record.
  Other starts read project defaults. Preserve the single-use, expiring handoff and its
  announcement; see the design notes before changing inheritance.
- File checkpoints clear only reviewed revisions. Queue resets invalidate live checkpoints;
  an old review must not clear later edits. Keep edited-file buckets disjoint.
- The answer document stays outside swept session state so a user deliverable cannot expire.
- Do not collect the full session history into every review. Supply the selected turn and
  source location so a reviewer can obtain further context when needed.
- The Korean translator and corrector are user-level agents invoked without a `guard:` prefix.
  They are one delivery step, not switchable audits. Handle unavailable names explicitly.
- Runtime scripts require `uv` and Python >=3.11. Locate plugin roots by their contents,
  never by assuming a fixed number of parent directories.

## Constraints on future changes

Do not restore automatic Stop auditing, a model call inside a hook, lexical reviewer
selection, or a child `claude -p` router. Do not restore the retired `audit_gate`, turn mute,
`reuse` mode, `reuse_agents`, or `exempt_skills`. The design notes retain the reasoning.
The `fresh` mode spelling remains a supported alias for `on`; `keep` and `resume` do not.

The removed write-refusal hook was deliberately removed, not abandoned because it failed.
Read its rationale before adding enforcement around reviewer writes. Agent memory can widen
available tools; a read-only instruction is not a host-enforced sandbox by itself.

Shipped agents, skills, commands and injected text must work in a stranger's repository.
Repository-specific paths and measurements belong in `dev/`, not those definitions.
Do not duplicate detailed mechanics here or in the end-user README.

## Verification

From the repository root, run `uv run guard/dev/check-entries.py` to validate shipped names and static agent references.
Plan, turn, and answer regression commands and the working-tree real-session recipe are in
[dev/design.md](dev/design.md), under "Explicit plan review", "Configured turn reviews", "Configured answer reviews" and
"Manual testing". Script tests alone do not verify host hook delivery or native invocation.
