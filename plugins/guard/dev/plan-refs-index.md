# guard: `INDEX.md` — a discoverable catalog of saved reference docs

Status: **plan, not implemented.** Target version: 0.15.0 (minor — new feature).

## Problem

The Grounded output style makes the assistant save a local copy of every cited
official doc into the refs directory (`output-styles/grounded.md:37-42`: "save its
relevant content to a **local file** in the project's **refs directory** … save there
(e.g. `$GUARD_REFS_DIR/<topic>.md`)"). Over a project's life that directory
accumulates docs, and guard exports only its path — `GUARD_REFS_DIR`
(`guard_hook.py:2053`: `fh.write(f"export GUARD_REFS_DIR={shlex.quote(str(refs))}\n")`).

Knowing only the folder name means a later session that wants to reuse a saved doc
must open files to find out what they hold. Filenames are chosen ad hoc by whichever
session saved them (`<topic>.md`), so `ls` gives a list of guesses, not an answer.
The evidence guard collects is written but not findable.

## Three problems, not one

An index solves *finding a doc inside the folder*. It does **not** solve *knowing the
index exists* — an `INDEX.md` that nothing points at is one more file in a folder the
model was already not opening. And whatever solves that for the main session does not
automatically solve it for **subagents**, which start with their own context and never
saw the main session's messages.

So this plan has three parts, and the last two are the load-bearing ones:

- **A. Generate** `INDEX.md` and keep it current (§1–§4).
- **B. Announce** it to the main session (§5–§6).
- **C. Announce** it to subagents, which don't inherit the announcement (§7).

## A. Generating the index

### 1. The blocking constraint — provenance is not in the payload

**The source URL is not in the hook payload.** Verified against the official
PostToolUse contract (local copy: `.claude/guard/refs/posttooluse-hook-input.md`;
source: <https://code.claude.com/docs/en/hooks>). The input fields are:

```json
{
  "session_id": "string",
  "prompt_id": "UUID string (present if user input has been submitted)",
  "transcript_path": "path/to/transcript.jsonl",
  "cwd": "current/working/directory",
  "permission_mode": "default|plan|acceptEdits|auto|dontAsk|bypassPermissions",
  "hook_event_name": "PostToolUse",
  "tool_name": "string",
  "tool_input": "object",
  "tool_response": "string or object",
  "tool_use_id": "string"
}
```

`tool_input` holds the tool's own arguments (for `Write`: `file_path`, `content`).
Nothing carries provenance. A hook can always learn *which file* was written, but can
only learn *what it is a copy of* by reading the file's content.

That forces the one real content decision: **the saved doc must carry a standard
header**, required by `output-styles/grounded.md`:

```markdown
---
source: https://code.claude.com/docs/en/hooks
title: PostToolUse hook contract
fetched: 2026-08-07
section: PostToolUse input schema     # optional
---
```

This is a modest addition to an instruction the style already gives — it already says
to "Name the version or section when it matters" (`grounded.md:43-44`) and to cite
"**both** the source URL and that local path" (`grounded.md:38-39`). The header makes
that existing obligation machine-readable instead of prose-only. The style must also
state that the header is what puts the doc in the index, so a model that skips it
understands the cost.

**Existing convention:** files already saved use a plain `# Title` + `Source: <url>`
prose form (e.g. `.claude/guard/refs/posttooluse-hook-input.md`). The parser
therefore accepts a fallback (§3) rather than treating pre-header files as invisible.

### 2. Hook wiring

New `PostToolUse` entry in `hooks/hooks.json`, matcher `Write|Edit|MultiEdit`,
calling a new `refs-index` subcommand. `NotebookEdit` is excluded — a saved doc copy
is markdown, never a notebook.

The hook is a **no-op unless** the resolved target is inside the refs directory,
reusing `_targets_refs_dir` (`guard_hook.py:1599-1609`), which already resolves the
target and tests `target == refs or refs in target.parents`. On every non-refs write
the hook exits after that one check.

PostToolUse **cannot block** ("Shows stderr to Claude; the tool already ran" — same
source), which suits this: a failed index update must never fail the user's write.
Every error path returns 0, matching `cmd_gate_approved` (`guard_hook.py:1531-1546`).

This fires for refs writes made **by a subagent** too — the hook is registered on the
tool, not on the thread — so the index stays current regardless of who saved.

### 3. `_ref_meta` — parse

For each refs file, read the first ~40 lines:

1. Parse YAML frontmatter if present.
2. **Fallback for header-less files:** first `# ` heading → `title`; first bare URL
   in the head → `source`; file mtime → `fetched`.
3. Neither title nor URL → listed under `## Unclassified` by filename, not dropped.

Silent omission is the same false-completeness failure the `writable list` fix
addressed in v0.14.0: a doc missing from the index reads as a doc that was never
saved.

### 4. `_write_refs_index` — full rewrite

Rewrite `INDEX.md` **whole** rather than appending:

- Appending needs dedup anyway (a re-fetched page is re-saved), and a full rewrite
  makes the index self-healing — a corrupted or hand-edited index is corrected at the
  next save.
- Input is bounded by one directory's file count: a scan plus small reads, no
  subprocess.
- Rewriting scans **all** refs files, so the index stays correct after a file is
  deleted or renamed outside a hook.

```markdown
<!-- Generated by guard. Edits are overwritten on the next reference save. -->
# Reference index

| Doc | Title | Source | Fetched |
| --- | --- | --- | --- |
| [hooks.md](hooks.md) | PostToolUse hook contract | code.claude.com/docs/en/hooks | 2026-08-07 |
```

The banner is load-bearing: without it a user edits the index and loses the edit at
the next save with no warning.

**`INDEX.md` itself must be skipped** when scanning and when reacting — otherwise
writing the index triggers the hook that writes the index. This recursion guard needs
a comment saying why, not just a condition.

## B. Making the index discoverable to the main session

### 5. Announce at SessionStart — gated on the `GUARD_REFS_DIR` export

guard's `cmd_session_start` already runs on every session and already writes
`GUARD_REFS_DIR` into the session's Bash environment (`guard_hook.py:2042-2055`). It
currently prints nothing.

Per the official contract (local copy: `.claude/guard/refs/sessionstart-hook-output.md`;
source: <https://code.claude.com/docs/en/hooks>):

> For most events, stdout is written to the debug log but not shown in the
> transcript. The exceptions are `UserPromptSubmit`, `UserPromptExpansion`, and
> **`SessionStart`**, where stdout is added as context that Claude can see and act on.

and

> SessionStart, Setup, SubagentStart | Context only |
> `hookSpecificOutput.additionalContext` adds context for Claude. … No blocking or
> decision control

So `cmd_session_start` emits `hookSpecificOutput.additionalContext` naming the index —
the same mechanism guard already uses for the guardian dispatch (`guard_hook.py:1789`).

**Emitted only when the `GUARD_REFS_DIR` export actually succeeded** — chained off the
existing `if env_file:` block (`guard_hook.py:2048`) *and* the write completing
without `OSError`, rather than announced unconditionally. The message tells the model
to resolve refs via `$GUARD_REFS_DIR` (as `grounded.md:40-42` instructs); if the
export did not happen, that route silently fails, and announcing it would produce the
confident-but-wrong behavior guard exists to prevent.

Additional constraints:

- **Only when the index is non-empty.** No saved docs → say nothing even if the export
  succeeded. A message that is usually noise gets ignored when it finally matters.
- **Count included** — "12 docs" tells the model whether the index is worth reading.
- **Short.** Injected into every session; one or two lines.
- **Reference the variable, not a hardcoded path**, so the message and the output
  style name the same thing:

```
guard: 12 reference docs are saved under $GUARD_REFS_DIR. Before fetching official
docs, check $GUARD_REFS_DIR/INDEX.md — it lists each doc's title, source URL, and
fetch date.
```

- **Announce on every `source`** (`startup`, `resume`, `clear`, `compact`, `fork`).
  Re-announcing after a `compact` is arguably most useful, since compaction is exactly
  when an earlier mention was dropped.

### 6. Second pointer — the output style

`output-styles/grounded.md` currently tells the model where to *write* docs, never to
*read* what is already there. Its official-documentation bullet gains a check-first
step: consult `INDEX.md` before fetching, and reuse a saved copy when it answers the
question.

This matters independently of §5: the style is in context for every turn, whereas a
session-start note can fall out of a long conversation. It is also the fallback when
§5 stays silent — the style already handles an unset variable ("Only if the variable
is unset, fall back to `refs_dir` from `.claude/guard.local.json`",
`grounded.md:43-45`), so the index stays reachable by the documented fallback route
with no announcement at all.

## C. Reaching subagents

### 7. `SubagentStart` hint — same message, same gate

**Subagents do see `GUARD_REFS_DIR`.** Verified experimentally in this repo by
spawning a `general-purpose` subagent and having it echo the variable:

```
GUARD_REFS_DIR=[/Users/myungo/GitHub/studykit-plugins/.claude/guard/refs]
```

`env | grep -i guard` in that subagent also listed
`GUARD_REFS_DIR=/Users/myungo/GitHub/studykit-plugins/.claude/guard/refs`. So a
`CLAUDE_ENV_FILE` export written by the main session's SessionStart hook does reach
subagent Bash environments.

(The official docs do **not** state this either way — "The documentation does not
provide information about whether subagents inherit the parent session's environment
variables or `CLAUDE_ENV_FILE` exports", local copy
`.claude/guard/refs/subagentstart-hook.md`. The grounding here is the experiment, not
the docs. It was checked on macOS with the local CLI; treat it as verified behavior of
this environment rather than a documented guarantee.)

But **availability is not discovery**. A fresh `Explore`, `Plan`, or `general-purpose`
agent has no reason to check an environment variable nobody told it about, and the
Grounded output style (§6) governs the main session, not an arbitrary subagent's
context. Without a hint, the agents most likely to go fetch a doc afresh are exactly
the ones that never learn a local copy already exists.

**Design:** a new `SubagentStart` entry in `hooks/hooks.json` (no matcher, covering
every agent type) calling a `refs-hint` subcommand. Per the same source, the event
supports context injection and places it where it will be read:

> [SessionStart, Setup, and SubagentStart]: Context only |
> `hookSpecificOutput.additionalContext` adds context for Claude. … No blocking or
> decision control

> Where the reminder appears depends on the event:
> * SessionStart, Setup, and SubagentStart: at the start of the conversation, before
>   the first prompt

The hint is **the same message as §5, under the same two conditions**:

1. `$GUARD_REFS_DIR` is set in the hook's own environment, and
2. the index is non-empty.

Condition 1 is the decision made for this plan: hint **only when the variable is
present**. Since the message names `$GUARD_REFS_DIR` — keeping one phrasing across
main session, subagents, and the output style — it must not be emitted when that
variable would not resolve. `refs-hint` therefore reads `os.environ.get("GUARD_REFS_DIR")`
directly and stays silent when it is unset or empty, rather than recomputing the path
via `_refs_dir` and printing a literal.

This differs from §5's gate in *what is checked* — §5 checks that the export it just
attempted succeeded; §7 checks that the variable it inherited is actually there — but
both reduce to the same invariant: **never point at `$GUARD_REFS_DIR` unless
`$GUARD_REFS_DIR` resolves.**

Deliberately **not** matcher-scoped to a list of agent types: any agent that can call
`WebFetch` benefits, and enumerating types would silently miss user-defined and future
ones.

`guard:guardian` is not excluded. It is already told `refs_dir` explicitly by its
dispatch (`guard_hook.py:1755`: `f"- refs_dir: {refs_path}\n"`; `agents/guardian.md:24`:
"The dispatching message names these verbatim"), so the hint is redundant for it — but
excluding it means a matcher in `hooks.json` that must stay in sync with the agent's
name. One short redundant line is the cheaper trade.

**Open risk:** this hook fires on *every* subagent spawn. It must be correspondingly
cheap — one env read, one directory scan, exit 0 on anything unexpected — and print
nothing when there is nothing to say, or it becomes a tax on every fan-out.

## Gate interaction — already handled

The hook writes into the refs directory, which the approval gate already exempts
(`cmd_gate`, `guard_hook.py:1435-1437`: `if _targets_refs_dir(...)` → `allow_refs`).
No new exemption, and **no `writable_dirs` entry** is needed — v0.14.0's allowlist is
unrelated to this feature.

## Tracked vs. ignored refs

`_refs_dir` defaults to `wiki/ref/`, git-tracked (`guard_hook.py:371-372`:
`default = project_dir / "wiki" / "ref"`), so `INDEX.md` is normally committed with
the repo — which is what makes it useful to a *later clone*, not just a later session.

A project may point `refs_dir` at an ignored path, and **this repo does**:
`git check-ignore -v .claude/guard/refs` →
`.gitignore:214:.claude/guard/	.claude/guard/refs`, while `wiki/ref` is not ignored.
When dogfooding here, `INDEX.md` is local-only — a testing footnote, not a defect: the
index is exactly as tracked as the docs it indexes.

## Files

- **`scripts/guard_hook.py`** — `cmd_refs_index`, `cmd_refs_hint`, `_ref_meta`,
  `_write_refs_index` (new); `"refs-index"` / `"refs-hint"` in `SUBCOMMANDS`
  (`:2421-2434`); `cmd_session_start` (`:1998-2057`) gains the export-gated
  `additionalContext` emission; module docstring hook list (`:20-32`, `:97`).
- **`hooks/hooks.json`** — a new `PostToolUse` entry (matcher `Write|Edit|MultiEdit`;
  the file already has two, and this differs from the existing mutating-tool block by
  excluding `NotebookEdit`), and a new `SubagentStart` entry (no matcher).
- **`output-styles/grounded.md`** — the required header (§1) and the check-first step
  (§6), both in the official-documentation bullet at `:36-48`.
- **`dev/design.md`** — hook table (`:19-23`); a section on the index's invariants
  (recursion guard, full-rewrite rationale, never-block, and the shared
  never-point-at-an-unset-variable gate behind §5 and §7).
- **`README.md`** — the refs paragraph (`:212-218`) gains a sentence that guard
  maintains an `INDEX.md` catalog and points sessions at it. User-visible surface
  only, per repo README policy.
- **`.claude-plugin/plugin.json`** — `0.14.0` → `0.15.0`.

No change: `skills/settings/SKILL.md` (the index is not configurable),
`agents/guardian.md` (already told `refs_dir` by its dispatch),
`guard.local.json.example`.

## Open question

**Strictly generated, or hand-annotatable?** This plan assumes strictly generated
(full rewrite + banner). Preserving a free-text note column across rewrites is more
useful for a human curator but adds merge logic and a failure mode where a malformed
note blocks the rewrite. Recommend strictly generated for v0.15.0.

## Verification

guard has no automated tests (the convention is the manual recipe at
`dev/design.md:254-299`), so this extends that recipe.

Generation:
- Conforming ref → appears with all four columns.
- Header-less ref → appears via the fallback parser, not dropped.
- Ref with neither title nor URL → appears under `## Unclassified`.
- Re-save the same doc → one row, not two.
- Delete a ref, save another → the deleted row is gone (full-rewrite property).
- **Write `INDEX.md` itself → no recursion.**
- Write a normal source file → hook exits without touching the refs dir.
- Corrupt `INDEX.md` by hand, save a ref → index restored.
- A parse failure on one file still writes the other rows, and returns 0.

Main-session discovery (asserted on the hook's actual stdout):
- `CLAUDE_ENV_FILE` unset → **no announcement**; session still starts.
- `CLAUDE_ENV_FILE` set but unwritable (`OSError`) → **no announcement**, no traceback.
- Export succeeds, refs dir empty/absent → **no announcement**.
- Export succeeds, refs dir non-empty → names `$GUARD_REFS_DIR/INDEX.md` and the count.

Subagent discovery:
- `GUARD_REFS_DIR` set + index non-empty → hint emitted, naming `$GUARD_REFS_DIR/INDEX.md`.
- `GUARD_REFS_DIR` unset or empty → **no hint**, whatever the refs dir contains.
- Index empty/absent → **no hint**, even with the variable set.
- Unreadable refs dir → exits 0, no traceback, subagent still starts.

`_ref_meta` is a pure function over file content and is directly unit-testable, like
`_read_turn_from_transcript` (`dev/design.md:298-299`).

Per repo convention, the end-to-end behavioral checks — does a cold main session, and
separately a cold subagent, actually consult `INDEX.md` before fetching? — must run in
a **fresh subagent**, not inline; the authoring session's context makes it a foregone
conclusion.

## Note for implementation

The plugin loaded in this session is `guard/0.13.1` from the plugin cache
(`~/.claude/plugins/cache/studykit-plugins/guard/0.13.1/bin`, seen in `PATH` during
the subagent test), not the 0.14.0 working tree. Hook changes will not take effect
here until the installed plugin is updated — worth confirming before concluding that
a new hook "doesn't fire".

## Sources

- PostToolUse input/output contract and matcher semantics; SessionStart
  stdout-as-context, `additionalContext` support, and `source` values; SubagentStart
  firing, matcher, `additionalContext` support, and context placement; the docs'
  explicit silence on subagent env inheritance —
  <https://code.claude.com/docs/en/hooks> (local copies:
  `.claude/guard/refs/posttooluse-hook-input.md`,
  `.claude/guard/refs/sessionstart-hook-output.md`,
  `.claude/guard/refs/subagentstart-hook.md`; all git-ignored in this repo).

**Unverified:** `guard_hook.py:2046-2047` cites this same page for `CLAUDE_ENV_FILE`,
but that term did not appear in the fetched content. The mechanism demonstrably works
(the subagent test above), so this is a stale-citation question, not a broken feature
— worth re-checking when that code is next touched.
