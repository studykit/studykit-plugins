---
name: guard-plugin-evidence-locations
description: Where to check guard-plugin claims about hook behavior, trust dialog, session mute, and answer-file fallback
metadata:
  type: project
---

When auditing a turn about the `guard` plugin's own runtime behavior (trust dialog, session
mute, answer-file fallback, `--session` settings scoping, deny-vs-suggestion argument), the
supporting doc is `guard/dev/design.md` (not auto-loaded, must Read directly) plus
`guard/AGENTS.md`. Source-level confirmation:

- Trust dialog being a separate gate from any permission mode, and "runs in a directory
  already trusted" being a free/no-edit path: `guard/dev/design.md` around line 1504-1512.
- `user-prompt` hook (`UserPromptSubmit`) writing `.request.md` and the draft-path line under
  the exact same gate (not muted, an agent reads the turn, prompt_id present):
  `guard/scripts/guard_core/cmd_turn.py` (`cmd_user_prompt`, ~line 42-76).
- Muted-session behavior (marker + response written, but no recommendation) is in
  `guard/scripts/guard_core/cmd_stop.py` around line 125-137 (`_audit_paused` check
  placed AFTER writing `pending_verify_prompt_id`/response, so a paused turn still records but
  never recommends).
- `settings set --session` mirrors a config change into the live session's `state/<sid>.json`:
  `guard/scripts/guard_core/cmd_settings.py` (`_apply_session_scalar`, ~line 52-65).
- The "deny enforces, a sentence only suggests" argument the design leans on elsewhere:
  `guard/dev/design.md` around line 151-158.

**Why:** A recent turn (2026-08-23) made a dense table of "verified live in an interactive
tmux session" claims plus several design-behavior citations; all of them traced cleanly to
these exact locations, so a future audit of a similar guard-behavior turn can go straight
there instead of grepping cold.

**How to apply:** For any future turn claiming things about guard's hook gating, check these
files/lines first before a broader repo search.

## Claims about which guard version a session actually runs

For turns claiming "the installed copy is stale / the cache runs version X" (audited
2026-08-26), the settling evidence is outside this repo:

- `~/.claude/plugins/installed_plugins.json` — per-project `installPath` / `version` /
  `gitCommitSha` for `guard@studykit-plugins`; this is what says which projects run which
  version and whether *this* repo has guard installed at all (it does not).
- `~/.claude/plugins/cache/studykit-plugins/guard/<version>/` — the versioned copies; each
  has its own `scripts/guard_core/`, so "the old version had no such key" is grepped there,
  not reasoned about.
- `~/.claude/plugins/known_marketplaces.json` — whether a marketplace is a `github` or a
  `directory` source (studykit-plugins is github, so unpushed commits cannot reach the cache).
- Whether the live session runs the working tree: `$GUARD_TOGGLE_CLI` points at
  `guard/scripts/guard_hook.py` under the repo when started with `--plugin-dir`.

**Why:** these four answer "which code was running" without asking the session, which is the
question most of these turns turn on.

**How to apply:** check these before crediting or faulting any version/installation claim.

## Verifying "no occurrence remains anywhere in the repository"

`grep -rn <pat> /Users/myungo/GitHub/studykit-plugins --exclude-dir=.git` silently does **not**
descend into dot-directories such as `.claude/` in this environment — it returned zero matches
for a string that `grep -n` on the file itself found (audited 2026-08-27). So a bare recursive
grep will falsely confirm an "it's gone everywhere" claim.

**How to apply:** settle such claims with `git grep -In <pat> -- .` (authoritative for tracked
content) plus explicit recursive greps on the dot-dirs that matter (`.claude-plugin/`,
`.agents/`, `.codex-plugin/`). Remember guard's own `.claude/guard/turns/*.md` record quotes the
old strings by design — that is not a leftover.

## Turn dispatch vs document dispatch (auditing claims about guard's own routing)

Audited 2026-08-27, for turns claiming what each dispatch path hands an agent:

- What a document dispatch carries: `guard/scripts/guard_core/cmd_inputs.py`
  `_inputs_for_file` (prints only `file:` + `knowledge dir:`), and
  `guard/agents/report-router.md` Output (~L156-164, "no turn id and no transcript").
- What a turn dispatch carries: `guard/hooks/context/dispatch-playbook.md` L128, but the
  transcript half is CONDITIONAL — `dispatch.py:148` emits the history line only `if transcript`,
  and `cmd_inputs.py` prints `transcript:`/`turn:` only when session state recorded one. So
  "a turn dispatch always carries a transcript path" is false; `AGENTS.md:57` says the routed
  dispatch is down to `- turn: <id>`.
- Adding an agent = one new key in `AUDIT_AGENTS` (`scripts/guard_core/agents.py:86-93`), which is
  simultaneously the config switch, the candidates entry and the `subagent_type` (agents.py:21-25).
- `knowledge_dir` is NOT general "evidence outside the repo": it is the project's DEPLOYED-system
  knowledge (topology, environments, runbooks), read by `design-environment` only —
  `config.py:199-213`, `paths.py:159-179`, `agents/design-environment.md:28-29`.

**How to apply:** check these before crediting a claim about which inputs a path guarantees.

### Does the DOCUMENT path honor `reuse` / named instances? (No — audited 2026-08-27)

The `guard-<key>` reused-instance protocol lives ONLY in `hooks/context/dispatch-playbook.md`
L108-118 (turn path). On the document path: `cmd_inputs._inputs_for_file` prints no playbook,
`agents/report-router.md:28` tells the router "do not send your caller to the playbook", its
Output template (L156) says "Dispatch each of these as its own subagent" and carries no mode
line, and L44 tells the router to ignore the mode. So a claim that turn and document dispatch
"share a reused `guard-claims-auditor` instance" is NOT supported by `_instance_name`
(agents.py:72) alone — that function only derives the name; nothing on the document path uses it.

Also: the `report-router` refusal paragraph (L55-59) covers `korean-translator` AND
`korean-corrector`, not korean-corrector alone.

## Claims about what `korean-corrector` can and cannot catch (audited 2026-08-27)

`agents/korean-corrector.md` defines four axes: 복합문 / 번역체 / AI 문체 / register. **Axis 2
(번역체) explicitly lists "English word order forced into Korean" and "literal calques"**, so a
claim of the form "직역 is not one of the corrector's axes" is contradicted by that section. What
the file does support is narrower and is stated in "The one way this audit fails": the axis is a
phrase-level checklist and "a fluent, calque-free passage can still be unreadable", plus
"Change only what a finding names" / "do not rewrite the file" limit repair to local edits.

**How to apply:** for turns arguing that the corrector structurally cannot fix document-level
직역, check the axis-2 bullets before crediting the argument, and check whether a single observed
`번역체 0` report is being generalized into a statement about the specification.

## Renaming an agent: where a name is built rather than written (re-audited 2026-08-27)

`_agent_id` and `_instance_name` are GONE — they used to derive `guard:<key>` / `guard-<key>`
from the AUDIT_AGENTS key in `cmd_session.py` and `cmd_settings.py`, which is what made a
literal-string grep miss them. Both call sites were deleted with the reuse protocol. If a turn
cites them, check `git grep _instance_name -- scripts/` before crediting it.

What replaces that hazard: `agents._path_entry` is the ONE place a roster key becomes a
dispatchable name, and `cmd_candidates` is its only caller. A claim that "the translation
happens in one place" is now true, and checkable there.

`dev/build-agents.py`, `dev/agent-src/`, `*.tmpl.md` and `partials/` do NOT exist. A generator
by that name was built and then removed when the shared audits stopped being two agents each;
`dev/design.md` § "One audit, two paths" keeps the record. `dev/` holds
`agent-frontmatter-rationale.md`, `check-entries.py`, `design.md`, `fixtures/`,
`handoff-audit-workflow.md`.

Codex naming, for turns about `$guard:claims-auditor`: `hooks/scripts/hook_codex.py:143` matches
the **slash** prompt prefix `/guard:claims-auditor`; the installed agent is named
`guard_claims_auditor` (`skills/setup/scripts/install_agent.py:24`,
`skills/setup/templates/claims-auditor.toml:1`), and it is the only template setup installs.

## Peer-session claims (`ListAgents`, agent-registry staleness) — audited 2026-08-27

- A `ListAgents` row carries only `name [ref] · kind · idle/running · started Nh ago`. It does
  NOT carry a cwd or project path, so "session `kb-*` is a different project" rests on the name
  prefix alone; corroborate with `~/.claude/plugins/installed_plugins.json` project paths or ask.
- Agent-registry staleness ("a session started before the rename cannot dispatch the new name")
  is real and settled by the transcript: search the transcript for
  `Agent type '<name>' not found. Available agents:` — the list in that error is the registry.
- But the fix ("restart and the new names appear") holds only for a session that loads guard
  from THIS working tree (`--plugin-dir`; `GUARD_TOGGLE_CLI` points into the repo).
  `installed_plugins.json` has **no** entry for `/Users/myungo/GitHub/studykit-plugins`, so a
  peer session that loads guard from the versioned cache would not see uncommitted renames even
  after a restart. Check before crediting advice aimed at another session.

## The two audit switches stopped sharing a default (v0.116.0, audited 2026-09-02)

`DEFAULT_CONFIG` now has `audit-turn: "off"` and `audit-plan: "on"` (`config.py`, the
`AUDIT_TURN_KEY`/`AUDIT_PLAN_KEY` entries), and `AgentMode.FRESH = "fresh"` became
`AgentMode.ON = "on"` with `"fresh"` kept as a `_MODE_ALIASES` entry read through
`_parse_mode` inside `_agent_mode` (not only at the CLI).

Two places still described the two switches under the OLD single rule after that commit, and
were fixed in v0.116.1 once this audit named them — `config.py`'s `_audit_on` docstring and
`dev/design.md`'s config reference (~L1928). Both now state the per-key fallback. The lesson
outlives the fix: a `DEFAULT_CONFIG` change leaves prose behind in the accessor's own docstring
and in the design doc's config reference, so those are the two places to check before crediting
any "every place was updated" claim about a switch default.

Also: the `/clear` handoff record is written when the switches differ from the config **or**
the session recorded a handover file (`cmd_session.py`, `if (audit_paused, plan_paused) ==
_default_paused(config) and not handover:`), so an "only when the switches differ" claim is
too narrow.

**How to apply:** for turns about guard's switch defaults, these are the counterexamples to a
completeness claim.

## "guard's shell commands are missing from PATH" claims (audited 2026-09-02)

- The PATH prepend is written by `cmd_session.py::_add_shell_command_to_path` (~L64-105),
  called from `cmd_session_start` (~L449) after the `project_dir is None` early return.
- **`SessionStart` registers no matcher** (`hooks/hooks.json`), so per
  `wiki/ref/claude-code-hooks-session-env.md:70-81` it fires on `startup`, `resume`, `clear`,
  `compact` and `fork`. So "SessionStart already fired, therefore the PATH entry was never
  written for this session" is a **broken inference** — a later compaction/resume writes it.
  `_append_env_file` exists precisely because it fires repeatedly.
- A "no code fix would address this" claim is contradicted by `dispatch.py` (~L89-105), which
  records the removed `is_file()` fallback and names the fix: "the router [should] distinguish
  'the command failed' from 'nothing to audit' in its report".
- Per-session runtime state that IS in the repo: `.claude/guard/state/<sid>.json` (has
  `audit_paused`, `transcript_path`) and `.claude/guard/turns/<sid>/` — these prove guard's
  hooks ran in a session even when its Bash PATH lacked the wrappers.

**How to apply:** a subagent's own `command -v guard-inputs` is about ITS session id
(`CLAUDE_CODE_SESSION_ID`), which for a forked child session differs from the audited turn's
session — do not use it to refute a PATH claim about the other session.
