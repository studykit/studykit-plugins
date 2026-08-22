#!/usr/bin/env python3
"""guard hook dispatcher.

stdlib-only, executed directly via its shebang (no ``uv run``). Every subcommand
exits 0; blocking is expressed through decision payloads on stdout, never through
a non-zero exit. Internal failures are silent and fail-open (guard never blocks
because its own machinery broke).

Subcommands
-----------
- user-prompt    UserPromptSubmit. Name the file this turn's answer is to be written to,
                 so the answer exists somewhere editable while the turn is still running.
                 It has to be this hook: by Stop the answer is already printed, and a
                 printed answer cannot be corrected. guard keeps no copy of the prompt.
                 Silent when no agent that reads the turn (see ``_reads_turn``) is on — which
                 includes "every agent off" but also a project running only
                 ``comment-corrector`` — and for guard's own control commands.
- settings       CLI (argv), run by the ``guard:settings`` skill via Bash, in-session.
                 ``show`` prints the current settings; ``set <key> <value>`` changes one
                 of the per-agent settings — each named after the agent it controls
                 (``claims-auditor`` / ``deferrals-auditor`` / ``korean-corrector`` /
                 ``clarity-auditor`` / ``comment-corrector`` / ``agents-md-auditor``),
                 valued
                 ``off``/``fresh``/``reuse`` — or ``router_model`` / ``refs_dir``; ``unset
                 <key>`` removes a key from the file entirely, back to its default. The
                 agent settings also apply to the live session's ``state/<sid>.json`` when a
                 session id is available (``--session``, which the skill passes as
                 ``${CLAUDE_SESSION_ID}``, else the inherited
                 ``CLAUDE_CODE_SESSION_ID``); the rest are read from the config file at
                 use. Preserves every other key. Mutating verbs require the
                 settings-skill marker — see ``_cli_write_allowed``. Not a hook event.
- verify         UserPromptExpansion, one matcher per agent
                 (``^(guard:)?{claims,deferrals,clarity}-auditor$``,
                 ``^(guard:)?korean-corrector$``).
                 On demand, emit the dispatch instruction for that ONE agent
                 over the last completed turn (``pending_verify_prompt_id``, recorded by
                 every Stop). A switch that is off is still auditable this way — the
                 switch governs what guard recommends unasked, not what the user may ask
                 for.
- stop           Stop. A turn == the transcript ``prompt_id``. guard reads ONE transcript
                 record, for the turn's kind only (``_turn_identity``) — never its content,
                 which is the main agent's to write. Skips when ``stop_hook_active``, when
                 the prompt_id is absent, when the turn was opened by anything other than a
                 person typing (a background agent's completion, a subagent's
                 ``SendMessage``: guard's own dispatch causes those, so auditing them loops),
                 when it was opened by one of guard's own control commands, and when it was
                 opened by a user ``!`` command (no ``UserPromptSubmit`` fired for it, so no
                 answer file was ever named). Otherwise it records the turn as the pending
                 ``/guard:<agent>`` target and fills in the answer file if the turn left it
                 empty — both regardless of the switches, because the on-demand commands
                 must work in a project that keeps everything off. Then, when a turn-reading
                 agent is eligible, it emits ``additionalContext`` asking the main agent to
                 dispatch the router (``ROUTER_AGENT``) over the answer file with the
                 eligible agents and their modes, and to follow the sections its report
                 names; the eligible file-reading agents — ``comment-corrector``
                 (``reads="files"``) and ``agents-md-auditor`` (``reads="agent-docs"``) —
                 are dispatched directly over the turn's edited files instead, bypassing
                 the router. guard runs no model itself and never blocks here.
- post-edit      PostToolUse (Write/Edit/MultiEdit/NotebookEdit). Records a source file
                 or an agent instruction file written this turn (the lists the
                 ``comment-corrector`` and ``agents-md-auditor`` recommendations are built
                 from), and requires a file saved inside the
                 refs directory to be listed in that directory's ``AGENTS.md``, blocking
                 until it is. Both are independent of the agent switches.
- session-start  SessionStart. Sweep state files, ``trace.log``, and turns/ and extracts/
                 dirs older than retention, export ``GUARD_PROJECT_DIR`` and
                 ``GUARD_REFS_DIR`` via ``$CLAUDE_ENV_FILE`` (append-once, since this event
                 also fires on every compaction), and state as session context: the refs rule always,
                 the dispatch playbook's path when any turn-end agent is on, the ``refs-finder``
                 announcement when that switch is on (not on Codex), and the standing
                 reuse policy when any agent is in ``reuse``. Each is said ONCE here rather
                 than in every Stop, which is the whole reason this hook prints anything.
- toggle         UserPromptExpansion (``^(guard:)?toggle$``), for ``/guard:toggle
                 [on|off]``. Mutes or unmutes the automatic audit for THIS SESSION —
                 ``audit_paused`` in the session state, never guard.local.json, so it cannot
                 change what the project does by default. Empty argument flips; ``on`` means
                 auditing on, which clears the pause. While muted, ``stop`` recommends
                 nothing and ``user-prompt`` names no answer file, but the pending
                 ``/guard:<agent>`` target and the answer file are still recorded, so asking
                 for one audit still works. The hook does the work and prints the resulting
                 state; the command file only relays it.
- status         CLI (stdin JSON), for the user's status line. Prints one short field —
                 ``guard <n>`` armed / ``guard off`` muted / ``guard ·`` nothing switched on
                 — or NOTHING on any failure, because its stdout goes straight into the
                 user's status bar. A plugin cannot own the main ``statusLine``, so the user
                 composes this segment into theirs (``/guard:statusline`` offers to do it).
                 Reads only the small config and state files, nothing else: it runs on every
                 assistant message. Not a hook event.
- transcript     CLI (argv), run by an audit agent via Bash. ``index`` / ``turn`` / ``find``
                 over the session transcript, bounded by ``--since`` / ``--until`` /
                 ``--last``. Writes an extract FILE and prints only its path plus a
                 one-line summary, so nothing lands in a context that did not ask for it.
                 Only on an agent's request, never on a schedule. Not a hook event.
- refs-dir       Print the resolved refs directory (absolute), applying the
                 ``refs_dir`` validation. Called via Bash (claims auditor fallback / the
                 output style), not a hook event.

The three CLI verbs (``transcript``, ``settings``, ``refs-dir``) resolve the project root
with ``_cli_project_dir``: ``GUARD_PROJECT_DIR``, which SessionStart exports into the Bash
environment via ``$CLAUDE_ENV_FILE``, else the git root above the cwd. ``CLAUDE_PROJECT_DIR``
itself is never in that environment. The hook events use ``_project_dir``, which is the env
var alone and fails open. Do not merge the two: a hook guessing a root writes state somewhere
nobody looks, and a CLI verb refusing to guess answers nothing at all.

State lives project-local under ``${CLAUDE_PROJECT_DIR}/.claude/guard/``:
- ``state/<sid>.json``       — {<agent modes>, audit_paused, edited_prompt_id, edited_files, edited_agent_docs, last_audited_prompt_id, pending_verify_prompt_id, transcript_path, updated_at}
- ``turns/<sid>/<pid>.md``   — the turn's ANSWER. guard names the path at the start of the
                                turn and the main agent writes the substance there; the
                                agents audit it and the correctors edit it in place, so the
                                corrected file is what the user is shown. guard fills it in
                                only if the turn left it empty (see ``_write_turn_response``).
- ``turns/<sid>/<pid>.request.md`` — the user's REQUEST for that turn, verbatim, written by
                                guard at UserPromptSubmit. It goes to the ROUTER and to
                                nothing else: never audited, never corrected, never handed to
                                an audit agent. It is there so triage can tell the part of an
                                answer the user asked for from the part nobody asked for (see
                                ``_write_turn_request``).
- ``extracts/<dir>/…``       — what an agent pulled out of the transcript, written by the
                                ``transcript`` subcommand on request and swept with the
                                rest of the session's state. ``<dir>`` is the transcript
                                filename's stem unless the caller passes ``--session``, and
                                no caller does; Claude Code names that file after the
                                session, so in practice it reads as a session id without
                                being one by contract. Nothing reads these back by name —
                                the subcommand prints the path it wrote — so the sweep keys
                                on the directory's mtime instead.
- ``trace.log``              — file-only debug trace (enabled by GUARD_TRACE)

State is retained across the end of a session so a resumed session
(``claude --resume``) keeps its switch flags; both state and logs are
expired only by the age-based sweep at SessionStart (see ORPHAN_MAX_AGE_SECONDS).

Configuration (optional) is a JSON object at
``${CLAUDE_PROJECT_DIR}/.claude/guard.local.json``: one ``AgentMode`` per agent, keyed by
that agent's own name — ``claims-auditor`` / ``deferrals-auditor`` / ``clarity-auditor`` /
``korean-corrector`` / ``comment-corrector``, each ``"off"`` (the default) / ``"fresh"`` /
``"reuse"`` — which
together are the only control over whether guard says anything unasked and over whether an
agent is respawned per turn or held open for the session,
and ``refs_dir`` (string, default ``""``) — project-relative directory where guard saves
local copies of cited docs; empty means the git-tracked default ``wiki/ref/``, so the
collected references are committed with the repo (point it at a different tracked path,
e.g. ``"docs/refs"``, to override; values resolving outside the project, at the project
root, or into guard's own config/state fall back to the default — see ``_refs_dir``).
``router_model`` (string, default ``""``) — a model override for the router
agent only; empty leaves the choice to ``agents/router.md``, and every agent the router
recommends brings its own model from its own definition.
Unknown keys are ignored; a missing or malformed file falls back to all defaults. The
``guard:settings`` skill changes these
through the ``settings`` CLI: it writes guard.local.json and, for the switches, the
live session's state.

Requires Python 3.11+ (uses ``enum.StrEnum``).
"""

from __future__ import annotations

import json
import os
import re
import shlex
import sys
import time
from collections.abc import Iterable
from datetime import datetime, timezone
from enum import StrEnum
from pathlib import Path
from typing import Any, NamedTuple


# Codex adapters set GUARD_HOST before importing this module. Keep the historical
# Claude paths intact while preventing one host from interpreting the other's state.
# Read once into a constant: the Codex adapter imports this module, so anything below
# asking "which host" must get the same answer the paths were chosen from.
_HOST_IS_CODEX = os.environ.get("GUARD_HOST") == "codex"
if _HOST_IS_CODEX:
    STATE_DIR_REL = ".codex/guard"
    CONFIG_REL = ".codex/guard.local.json"
else:
    STATE_DIR_REL = ".claude/guard"
    CONFIG_REL = ".claude/guard.local.json"
TRACE_FILE_NAME = "trace.log"
TRACE_ENV_VAR = "GUARD_TRACE"
TRACE_TRUTHY = {"1", "true", "yes", "on"}
# Marker the `guard:settings` skill sets on the config-mutating CLI verbs. See
# _cli_write_allowed for what this does and does not buy.
CLI_WRITE_ENV_VAR = "GUARD_SETTINGS_SKILL"
ORPHAN_MAX_AGE_SECONDS = 7 * 24 * 60 * 60

class AgentMode(StrEnum):
    """How one audit agent runs. The value of that agent's config key.

    ``OFF`` — never recommended unasked. ``FRESH`` — a new instance per dispatch, which
    is the shape every agent definition is written for: judged in a fresh context, by a
    reader rather than the author. ``REUSE`` — one named instance per session, resumed on
    later turns with its full history.

    ``REUSE`` is not strictly better and not strictly worse, which is why it is the
    user's call and not a default. It buys continuity: the instance already knows this
    repository and this session's conventions, it does not re-derive the same thing every
    turn, and the main agent can go back to it ("you cleared this claim two turns ago —
    does the change I just made break it?"). It costs independence: a verdict it got
    wrong is now in its own history as settled, and every later turn inherits that error,
    where a fresh instance would have looked again. Continuity is worth most where the
    judgment is about text and conventions (the correctors); independence is worth most
    where it is about whether something is true (the auditors).

    Reuse is per SESSION, not per project — subagent transcripts live under the session
    id, so a new session starts every agent fresh whatever this says
    (``wiki/ref/claude-code-subagent-resume.md``).
    """

    OFF = "off"
    FRESH = "fresh"
    REUSE = "reuse"


# CLI spellings accepted for a mode, beyond the member values themselves. The boolean
# words are kept because "on"/"off" is what a switch has always been set with here, and
# "on" has to mean something: it means the mode the agents were designed for.
_MODE_ALIASES = {
    "on": AgentMode.FRESH, "true": AgentMode.FRESH, "yes": AgentMode.FRESH,
    "1": AgentMode.FRESH, "new": AgentMode.FRESH,
    "false": AgentMode.OFF, "no": AgentMode.OFF, "0": AgentMode.OFF,
    "keep": AgentMode.REUSE, "resume": AgentMode.REUSE,
}


DEFAULT_CONFIG: dict[str, Any] = {
    # Model for the router agent, overriding whatever `agents/router.md` declares.
    # Empty (the default) means guard says nothing about the model and the agent's own
    # frontmatter governs — the normal way a subagent's model is chosen, and the one
    # that keeps working when a host has no way to override it at dispatch. This exists
    # for the project that wants the router cheaper or sharper than the plugin ships it:
    # a router that misses means the audit silently never happens, which is the exact
    # failure guard exists to prevent, and the other direction costs just as much — a
    # model that cannot tell a backed claim from one that merely sounds backed names
    # every agent every turn, which is the same as naming none, because the user stops
    # reading the recommendation.
    "router_model": "",
    # One key per agent, named after the agent it controls — the key IS the agent's name,
    # so `settings set korean-corrector reuse` and `guard:korean-corrector` are the same
    # string and there is no second vocabulary to learn or to keep in sync. The value is
    # an `AgentMode`, so how the agent runs is the same setting as whether it runs: there
    # is no separate reuse list that could name an agent that is off.
    #
    # These are the ONLY control over whether guard says anything unasked. All of them off
    # (the default) is guard silent at Stop: no router, no recommendation, nothing added
    # to the main agent's context. There is deliberately no separate mode setting in
    # front of them — switching one on IS switching guard on, and a project that wants
    # the claim check without the deferral check just switches the one it wants.
    #
    # None of them governs the on-demand `/guard:<agent>` commands: a switch that is off
    # still leaves the user free to ask for that audit now. That is why every switch
    # ships off — guard installed is guard available, not guard running.
    "claims-auditor": AgentMode.OFF,
    "deferrals-auditor": AgentMode.OFF,
    # Can the intended reader follow the answer? The only agent whose verdict depends on
    # who is reading, which is why it carries `memory: user` rather than `local` and why
    # it degrades loudly — with no reader profile it says so and checks less, instead of
    # guessing a level and flagging either every technical term or none of them.
    "clarity-auditor": AgentMode.OFF,
    # Does a Korean response read as natural Korean, or as translated English?
    # Switching it on in an English-answering project costs nothing on those turns: the
    # router reads the response and simply does not pick it.
    "korean-corrector": AgentMode.OFF,
    # Comments in the source files THIS TURN edited. Unlike the three above it is not
    # an audit of the response: it points a corrector at real files and that corrector
    # EDITS them, unattended, in the turn the user is still reading. That is why it is
    # the one switch whose cost is a diff rather than a report.
    "comment-corrector": AgentMode.OFF,
    # The `AGENTS.md` / `CLAUDE.md` files THIS TURN edited, judged as instruction files:
    # a map pointing at the deeper docs, plus what a model gets wrong here — never the
    # implementation detail, the spec, or the thing every model already knows. Reports
    # only. Turning it on costs nothing on the many turns that touch no such file, since
    # eligibility needs one this turn actually wrote.
    "agents-md-auditor": AgentMode.OFF,
    # Which of the docs saved under `refs_dir` bear on the question the user just asked.
    # The only switch here that governs something said BEFORE an answer rather than an
    # audit of one after, so it is announced once at SessionStart and never routed.
    "refs-finder": AgentMode.OFF,
    # Where guard saves local copies of cited docs, relative to
    # the project dir. Empty = the default git-tracked `wiki/ref/`, so the collected
    # references are committed with the repo. Point it at a different tracked path
    # (e.g. "docs/refs") to override. Values that resolve outside the project, at the
    # project root, or into guard's own config/state are ignored (fall back to the
    # default) — see _refs_dir for why.
    "refs_dir": "",
}

# --------------------------------------------------------------------------- #
# environment / paths
# --------------------------------------------------------------------------- #
def _trace_enabled() -> bool:
    return os.environ.get(TRACE_ENV_VAR, "").strip().lower() in TRACE_TRUTHY


def _cli_write_allowed() -> bool:
    """True when a config-mutating CLI verb may write.

    guard never gates Bash, so the model can invoke this script directly — and the
    config-mutating verbs can weaken guard itself: `settings set claims-auditor off`
    stops the automatic audit. The `guard:settings` skill is
    `disable-model-invocation: true` (user-invoked only) and sets this marker; a bare
    model-issued Bash call does not have it.

    This is a SPEED BUMP, NOT A SECURITY BOUNDARY: the variable name is in this file,
    which the model can read, so a model that decides to defeat guard can set it. What
    it buys is (a) the unreflective path — "this gate is in my way, let me widen it" —
    fails closed, (b) the refusal names the user as the only legitimate widener, and
    (c) the attempt lands in the trace as `refused_no_skill_marker`. A model that
    deliberately sets the marker is outside guard's threat model, and either way the
    Bash call is visible to the user in the transcript.
    """
    return os.environ.get(CLI_WRITE_ENV_VAR, "").strip().lower() in TRACE_TRUTHY


def _project_dir() -> Path | None:
    """Project root for a HOOK. None when the host did not say, which fails open.

    A hook process is given `CLAUDE_PROJECT_DIR` (guard's Codex adapter sets
    `GUARD_PROJECT_DIR` the same way), so an absent value means something is wrong with the
    installation rather than that guard should guess — and guessing here would write state
    under whatever directory the host happened to launch in. CLI verbs are the opposite case
    and use `_cli_project_dir`.
    """
    value = os.environ.get("GUARD_PROJECT_DIR") or os.environ.get("CLAUDE_PROJECT_DIR")
    return Path(value) if value else None


def _cli_project_dir() -> Path:
    """Project root for a verb invoked over Bash. Never None — a CLI verb must answer.

    `CLAUDE_PROJECT_DIR` is NOT in the Bash tool's environment. It is given to hook
    processes and substituted into skill/command content; reaching the Bash environment takes
    an explicit `CLAUDE_ENV_FILE` export (`wiki/ref/claude-code-hooks-session-env.md`,
    `wiki/ref/claude-code-skill-substitutions.md`). SessionStart writes one —
    `GUARD_PROJECT_DIR`, via `_export_to_bash_env` — so on Claude Code the env branch below
    is the normal path, and everything after it is the fallback.

    That fallback still has to be right. The export is best-effort, `CLAUDE_ENV_FILE` is
    Claude Code only, and it is not documented to reach a SUBAGENT's Bash — which is exactly
    where `transcript` runs from.

    It used to be `Path.cwd()`, which is wrong in a way that stays silent. The caller is an
    agent or a skill, and an agent that had `cd`-ed into a subdirectory to read code wrote
    its extract to `<subdir>/.claude/guard/extracts/` and `settings show` reported a project
    with every switch off — a second, empty state tree beside the real one, in a directory
    the root `.gitignore` does not cover, so `git add -A` would have committed session
    extracts into the repo. That is the precise outcome guard chooses `memory: local` to
    avoid.

    Hence the git root, found by walking up from the cwd: guard's state is per-checkout, its
    ignore rules are written from the repo root, and every caller runs somewhere inside the
    checkout it is working on. `.git` is tested with `exists()` rather than `is_dir()`
    because in a worktree or submodule it is a file — and stopping at the worktree's own root
    is right, since a worktree is its own checkout with its own state.

    The cwd remains the last resort, for a project that is not a git repository at all.
    There is nothing better to offer there, and it is the behavior that was always in place.
    """
    env = os.environ.get("GUARD_PROJECT_DIR") or os.environ.get("CLAUDE_PROJECT_DIR")
    if env:
        return Path(env)
    start = Path.cwd().resolve()
    for candidate in (start, *start.parents):
        if (candidate / ".git").exists():
            return candidate
    return start


def _state_root(project_dir: Path) -> Path:
    return project_dir / STATE_DIR_REL


def _state_file(project_dir: Path, session_id: str) -> Path:
    return _state_root(project_dir) / "state" / f"{session_id}.json"


def _turn_record_file(project_dir: Path, session_id: str, prompt_id: str) -> Path:
    """The file the turn is passed between agents in. Written by guard, then extended.

    The turn goes through a file rather than through the dispatch text, and that is the
    whole coordination mechanism here. A routed turn has up to five readers — the router,
    then whichever agents it names — and pasting the turn into each dispatch means writing
    it out that many times, in a message the main agent composes itself, which is exactly
    where a turn quietly becomes a paraphrase of the turn. One file, read by everyone.

    The file is the ANSWER, not a record of it. guard names the path at the start of the
    turn, the main agent writes the substance there, the agents audit and correct it in
    place, and the corrected file is what the user is shown — so the same text never has to
    be printed twice, once flawed and once fixed. guard writes it only as a fallback, when
    the turn ended with nothing there. What surrounds the response — this turn's tool
    activity, what an earlier turn established — lives in the transcript, and an agent that
    needs any of it runs `transcript turn|find|index` and gets its own extract file. That
    keeps the author of the turn out of the record of the turn, which is the property the
    whole design rests on. The one exception is the user's request, which guard copies into
    a sibling file for the router alone (`_turn_request_file`): the router has `Read` and no
    way to extract, and materiality is the one judgment that cannot be made from the answer
    by itself.
    """
    return _state_root(project_dir) / "turns" / session_id / f"{prompt_id}.md"


# Section headings in the turn record. Fixed strings, because both the instruction that
# asks for a section and the agent definitions that say which section to read name them.
# Header on the copy GUARD writes, and only on that copy. The normal case is the main agent
# authoring this file during the turn — the file IS the answer, not a transcript of it — so
# there is no heading at all then. guard writes only when the turn ended with nothing there,
# and then the header is the honest label: this is a fallback, taken from the payload after
# the fact, and whatever the reply actually said is what the user already read.
TURN_FALLBACK_HEADER = (
    "<!-- guard: the turn ended without this file being written, so guard filled it in from "
    "the response it was handed. Audit it as the answer; corrections still go here. -->"
)


def _write_turn_response(project_dir: Path, session_id: str, prompt_id: str,
                         response: str) -> Path | None:
    """Fill in the answer file IF the turn left it empty. Returns the path, or None.

    Not an overwrite, ever. The main agent is asked at the start of the turn to write its
    answer here, and by Stop that file may already hold the answer plus whatever a corrector
    has done to it — clobbering it with the payload copy would throw away the corrections
    and replace the working document with a snapshot of an earlier state.

    So this is the fallback for a turn that ignored the ask, and it matters that there is
    one: the on-demand `/guard:*` commands audit the last completed turn whatever the
    settings say, and with no file at all they would have nothing to point an agent at.

    Best-effort, and a failure is silent: the recommendation goes out anyway and the main
    agent is asked to create the file. A guard that refused to recommend because it could
    not write a scratch file would be failing closed on its own plumbing.
    """
    path = _turn_record_file(project_dir, session_id, prompt_id)
    try:
        if path.exists() and path.stat().st_size > 0:
            return path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"{TURN_FALLBACK_HEADER}\n\n{response.rstrip()}\n",
                        encoding="utf-8")
    except OSError:
        return None
    return path


def _turn_request_file(project_dir: Path, session_id: str, prompt_id: str) -> Path:
    """The file holding the user's request for this turn. For the ROUTER only.

    A sibling of the answer file rather than a section inside it, and that separation is the
    point. Put in the answer file, the user's own sentences become text the correctors edit —
    `korean-corrector` would rewrite the user's Korean, in a file the user is then shown —
    and text the auditors weigh as part of the answer. Kept apart, the request can be handed
    to the one agent whose judgment needs it and withheld from every agent that would act on
    it. It also lands in the same per-session directory, so the SessionStart sweep reaps it
    with the answer it belongs to and there is no second tree to keep bounded.
    """
    return _state_root(project_dir) / "turns" / session_id / f"{prompt_id}.request.md"


# Header on the request file. guard writes this file itself, so unlike the answer file it
# always carries a header — and the header has work to do: the router is told the file is
# the user's words and not the answer, at the top of the file it is reading, where a
# dispatch line naming the path cannot say it.
TURN_REQUEST_HEADER = (
    "<!-- guard: the user's request for this turn, verbatim, as guard received it at "
    "UserPromptSubmit. NOT part of the answer: nothing audits it, nothing corrects it, and "
    "no audit agent is given it. It exists so the router can tell what the user asked for "
    "from what the answer volunteered. -->"
)


def _write_turn_request(project_dir: Path, session_id: str, prompt_id: str,
                        prompt: str) -> Path | None:
    """Save the user's request verbatim for the router. Returns the path, or None.

    Verbatim is the requirement, not a nicety: the router's job is to judge what the user
    asked for, and a condensed or paraphrased request is one guard's own summarizer has
    already decided the answer to. This is the only place guard keeps a copy of a prompt, and
    it is kept for one reader.

    Best-effort and silent on failure, like `_write_turn_response`: the router falls back to
    judging materiality from the answer alone, which is what it did before this file existed.
    A guard that skipped an audit because it could not write a scratch file would be failing
    closed on its own plumbing.
    """
    path = _turn_request_file(project_dir, session_id, prompt_id)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"{TURN_REQUEST_HEADER}\n\n{prompt.strip()}\n", encoding="utf-8")
    except OSError:
        return None
    return path


def _safe_project_subdir(project_dir: Path, raw: Any) -> Path | None:
    """Resolve a configured project-relative directory, or None if it is not safe.

    guard's self-neutering defense for a config key that names a directory guard
    treats specially (``refs_dir``). A value is honored only when it resolves:

    - inside the project, STRICTLY below it — ``project not in candidate.parents``
      rejects the project root itself, because a path is never in its own
      ``.parents`` and ``"."`` resolves to the project dir. A root-level exemption
      would exempt every project write and neuter the gate, so this strictness is
      load-bearing: do not relax it to a ``==``-tolerant containment test.
    - outside guard's OWN config/state — a value of ``.claude/guard`` would let the
      model write ``state/<sid>.json``, and ``.claude/guard.local.json`` would let it
      turn the audit off.

    Note what this does NOT catch: an ANCESTOR of guard's state (e.g. ``.claude``)
    is a legal value — it is neither the state root nor under it.

    Returns the resolved absolute Path, or None when the value is unusable (not a
    non-empty str, unresolvable, or failing either rule above); ``_refs_dir`` then
    falls back to its default.
    """
    if not isinstance(raw, str) or not raw.strip():
        return None
    try:
        candidate = (project_dir / raw.strip()).resolve()
        project = project_dir.resolve()
        state_root = _state_root(project_dir).resolve()
        config_path = (project_dir / CONFIG_REL).resolve()
    except OSError:
        return None
    if project not in candidate.parents:
        return None
    if candidate == state_root or state_root in candidate.parents or candidate == config_path:
        return None
    return candidate


def _refs_dir(project_dir: Path, config: dict[str, Any] | None = None) -> Path:
    """Directory where guard saves local copies of cited docs.

    Writes here are the assistant grounding its own claims (per the output style),
    not implementing the user's task.

    Default is ``wiki/ref/`` under the project, a git-tracked location so the
    collected references are committed with the repo; the ``refs_dir`` config key
    may point it at a different project path (e.g. ``docs/refs``). A configured
    value is honored only when ``_safe_project_subdir`` accepts it (strictly inside
    the project, outside guard's own config/state — see there for why); anything
    else falls back to the default, so ``refs_dir`` can never become a hole.
    """
    default = project_dir / "wiki" / "ref"
    return _safe_project_subdir(project_dir, (config or {}).get("refs_dir", "")) or default


def _project_rel(project_dir: Path, path: Path) -> str:
    """Project-relative form of an absolute path, for display. Falls back to the
    absolute path when it can't be made relative."""
    try:
        return str(path.resolve().relative_to(project_dir.resolve()))
    except (OSError, ValueError):
        return str(path)


def _trace_file(project_dir: Path) -> Path:
    return _state_root(project_dir) / TRACE_FILE_NAME


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _trace(project_dir: Path | None, session_id: str | None, cmd: str, event: str, **fields: Any) -> None:
    if not _trace_enabled() or project_dir is None:
        return
    try:
        path = _trace_file(project_dir)
        path.parent.mkdir(parents=True, exist_ok=True)
        record = {"ts": _now_iso(), "sid": session_id, "cmd": cmd, "event": event}
        record.update(fields)
        with path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
    except OSError:
        pass


# --------------------------------------------------------------------------- #
# payload / config / state
# --------------------------------------------------------------------------- #
def _read_payload() -> dict | None:
    try:
        raw = sys.stdin.read()
    except OSError:
        return None
    if not raw.strip():
        return None
    try:
        payload = json.loads(raw)
    except (json.JSONDecodeError, ValueError):
        return None
    return payload if isinstance(payload, dict) else None


_SESSION_ID_RE = re.compile(r"^[A-Za-z0-9._-]+$")
# guard's own control commands, e.g. "/guard:settings claims-auditor off", "/settings",
# "/guard:claims-auditor". `settings` is a forked skill and each per-agent command a
# UserPromptExpansion — either way the turn is a relay, not real work to log/judge. The
# name is `settings`, not `config`, precisely so the bare form does NOT match Claude Code's
# built-in `/config` command (which the optional `(guard:)?` would otherwise capture,
# making guard treat every `/config` as its own control command). `(?=\s|$)` rather than
# `\b`: the name must END here, not merely hit a word boundary — `\b` would also accept a
# longer hyphenated name (`/settings-export` matching `settings`, `/claims-auditor-extra`
# matching `claims-auditor`), which is how another plugin's command becomes guard's.
# `comment-corrector` is deliberately ABSENT: that skill's relayed findings are claims about
# real files and about edits made to them, so its turn stays auditable like any other work.
# `statusline` is absent for the same reason: it reports what is in the user's settings files
# and proposes an edit to them, which is checkable work, not a relay of guard's own state.
# `reader-profile` is here for a different reason from the rest: its turn is an interview
# about the user, so the "answer" is the user's own words read back to them, and auditing
# that would have guard grading the user on how they described themselves.
_CONTROL_CMD_RE = re.compile(
    r"^/(guard:)?(settings|toggle|reader-profile|claims-auditor|deferrals-auditor"
    r"|clarity-auditor|korean-corrector)(?=\s|$)",
    re.IGNORECASE)
# In the transcript, a slash command is expanded to
# "<command-name>/guard:settings</command-name>" (see session b30dbaec). Pull the command
# name out of that tag; a raw typed form ("/guard:settings claims-auditor off") is handled by
# the fallback in _turn_command_name.
_COMMAND_NAME_RE = re.compile(r"<command-name>\s*(/?[^<\n]+?)\s*</command-name>", re.IGNORECASE)


def _session_id(payload: dict) -> str | None:
    sid = payload.get("session_id")
    if not isinstance(sid, str) or not sid:
        return None
    # Defensive: session_id is interpolated into state/log filenames. Reject any
    # value that could escape the state directory (path separators, `..`). Note
    # the charclass alone still admits "..", so exclude that explicitly.
    if ".." in sid or not _SESSION_ID_RE.match(sid):
        return None
    return sid


def _message_of(record: Any) -> dict[str, Any]:
    msg = record.get("message") if isinstance(record, dict) else None
    return msg if isinstance(msg, dict) else {}


def _turn_command_name(user_text: str) -> str:
    """The slash command that opened the turn, normalized (leading '/' stripped,
    lowercased), or '' when the turn was not opened by a slash command.

    Slash commands reach the transcript expanded as
    ``<command-name>/guard:settings</command-name>``; a raw typed form
    (``/guard:settings claims-auditor off``) is handled by the fallback.
    """
    text = user_text.strip()
    m = _COMMAND_NAME_RE.search(text)
    if m:
        name = m.group(1).strip()
    elif text.startswith("/"):
        name = text.split()[0]
    else:
        return ""
    return name.lstrip("/").lower()


def _is_control_command_name(name: str) -> bool:
    """True when a normalized command name is one of guard's own control commands
    (``settings``/``reader-profile``/``*-auditor``/``korean-corrector``, with or without
    the ``guard:`` prefix)."""
    return bool(name) and bool(_CONTROL_CMD_RE.match("/" + name))


# Text the host injects into a `user` record that is not the user talking: hook output,
# slash-command envelopes, `!` command echoes, the compaction caveat. Matched as a prefix
# on the record's text. Without this filter the record's "user request" is whatever the
# host happened to prepend, which is both wrong and the kind of wrong an auditor cannot
# detect — it has no other copy of the request to compare against. The same list drives
# hindsight's transcript renderer (`plugins/hindsight/skills/review/scripts/render.py`).
# The envelope a user `!` command's input arrives in. It is also the record that ANCHORS
# such a turn, which is what `_turn_identity` keys its Stop skip on.
_BASH_TAG = "<bash-input>"

_INJECTED_PREFIXES = (
    "<system-reminder", "<command-name>", "<command-message>", "<command-args",
    "<local-command", "<bash-input", "<bash-stdout", "<bash-stderr", "Caveat:",
    "<task-notification", "<user-prompt-submit-hook>",
)

# Caps on the tool activity guard slices into a turn record. Generous, because the record
# is a file rather than context — but not unbounded: whoever is dispatched Reads the whole
# file, so an uncapped 5MB transcript turn would arrive in an auditor's context intact.
# Per-result first, so one runaway command cannot crowd out ten useful ones, then a total.
TOOL_RESULT_MAX_CHARS = 4000
TOOL_ACTIVITY_MAX_CHARS = 30000


def _transcript_records(path: Path):
    """Yield the transcript's records as dicts, in file order. Malformed lines skipped.

    Streamed with ``errors="replace"``: these files reach several megabytes, and one
    undecodable byte must not cost the whole read.
    """
    try:
        fh = path.open(encoding="utf-8", errors="replace")
    except OSError:
        return
    with fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                rec = json.loads(line)
            except (json.JSONDecodeError, ValueError):
                continue
            if isinstance(rec, dict):
                yield rec


def _turn_slice(transcript_path: Any, prompt_id: Any) -> dict[str, Any] | None:
    """Everything guard can read about one turn from the transcript. None when it cannot.

    Returns ``{origin_kind, command_name, user, assistant, tools}``. A turn is
    anchored on the FIRST record whose top-level ``promptId`` equals ``prompt_id``, and the
    slice runs to the next record carrying a DIFFERENT non-empty promptId. That positional
    rule is not a convenience: only ``user`` records carry a promptId at all — the assistant
    records, and the ``tool_use`` blocks inside them, carry none — so a filter on promptId
    would drop precisely the tool activity this exists to collect. Verified on a real
    4.8MB, 21-turn transcript: promptIds occur in contiguous runs, one run per turn.

    Skipped: ``isMeta`` (guard's own injected feedback), ``isSidechain`` (a subagent's
    records, which are not this turn's activity even when they share the file), and user
    text that is really host-injected envelope (``_INJECTED_PREFIXES``), which a user `!`
    command's input and output are: neither is the user asking for anything.

    Fail-open throughout: an unreadable transcript, a malformed line, or a prompt_id absent
    from the file yields None or a partial slice, never a raise.
    """
    if not isinstance(transcript_path, str) or not isinstance(prompt_id, str) or not prompt_id:
        return None
    path = Path(transcript_path)
    if not path.is_file():
        return None

    user = ""
    assistant: list[str] = []
    tools: list[dict[str, str]] = []
    origin_kind = ""
    command_name = ""
    in_turn = False

    for rec in _transcript_records(path):
        rec_pid = rec.get("promptId")
        if not in_turn:
            if rec_pid != prompt_id:
                continue
            in_turn = True
            origin = rec.get("origin")
            if isinstance(origin, dict):
                origin_kind = str(origin.get("kind") or "")
            anchor = _message_of(rec).get("content")
            command_name = _turn_command_name(anchor if isinstance(anchor, str) else "")
        elif isinstance(rec_pid, str) and rec_pid and rec_pid != prompt_id:
            break

        if rec.get("isMeta") is True or rec.get("isSidechain") is True:
            continue

        content = _message_of(rec).get("content")
        if isinstance(content, str):
            if not user and not content.lstrip().startswith(_INJECTED_PREFIXES):
                user = content
            continue
        if not isinstance(content, list):
            continue
        for part in content:
            if not isinstance(part, dict):
                continue
            ptype = part.get("type")
            if ptype == "text":
                txt = str(part.get("text", "")).strip()
                if txt:
                    assistant.append(txt)
            elif ptype == "tool_use":
                name = part.get("name", "tool")
                inp = part.get("input")
                cmd = inp.get("command") if isinstance(inp, dict) else None
                if not isinstance(cmd, str) or not cmd:
                    cmd = f"[{name}] {json.dumps(inp, ensure_ascii=False)[:400]}"
                tools.append({"command": cmd, "output": ""})
            elif ptype == "tool_result":
                res = part.get("content")
                if isinstance(res, list):
                    res = " ".join(str(x.get("text", "")) for x in res if isinstance(x, dict))
                out = str(res if res is not None else "")
                for t in reversed(tools):
                    if not t["output"]:
                        t["output"] = out
                        break
                else:
                    tools.append({"command": "[tool_result]", "output": out})

    if not in_turn:
        return None
    return {
        "origin_kind": origin_kind,
        "command_name": command_name,
        "user": user,
        "assistant": "\n\n".join(assistant),
        "tools": tools,
    }


def _extract_dir(project_dir: Path, session_id: str) -> Path:
    return _state_root(project_dir) / "extracts" / (session_id or "unknown")


def _write_extract(path: Path, body: str) -> bool:
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body, encoding="utf-8")
        return True
    except OSError:
        return False


def _render_turn(turn: dict[str, Any], turn_id: str) -> str:
    """One turn as an extract file reads: request, tool activity, response. Verbatim.

    Verbatim is the whole point of extracting with a script instead of asking an agent to
    write down what happened. A copy made by the turn's own author gets tidied, and a
    tidied turn is one where the claim actually made is no longer the claim being audited.
    Truncation is marked in place so a reader can tell a short command from a cut one.
    """
    parts: list[str] = []
    for t in turn.get("tools", []):
        if not isinstance(t, dict):
            continue
        out = str(t.get("output", ""))
        if len(out) > TOOL_RESULT_MAX_CHARS:
            out = out[:TOOL_RESULT_MAX_CHARS] + "\n…(output truncated by guard)"
        parts.append(f"$ {t.get('command', '')}\n→ {out}")
    activity = "\n\n".join(parts).strip()
    if len(activity) > TOOL_ACTIVITY_MAX_CHARS:
        # Keep the TAIL: the later calls are the ones the response was written from.
        activity = ("…(earlier tool activity in this turn omitted by guard)\n"
                    + activity[-TOOL_ACTIVITY_MAX_CHARS:])
    return "\n\n".join([
        f"# Turn {turn_id}",
        "## The user's request",
        (str(turn.get("user", "")).strip() or "(not in the transcript)"),
        "## Tool activity",
        (activity or "(none)"),
        "## What the assistant said",
        (str(turn.get("assistant", "")).strip() or "(not in the transcript)"),
    ]) + "\n"


def _turn_index(path: Path) -> list[dict[str, str]]:
    """Every turn in the transcript, in order: its id, when it started, its opening line.

    An index, not content — small enough that an agent can read it whole and then ask for
    the two or three turns that look relevant. Turns opened by a host-injected envelope
    (a task-notification, a hook relay) are labelled as such rather than dropped: an agent
    looking for where a number came from is better served by seeing the gap.
    """
    out: list[dict[str, str]] = []
    for rec in _transcript_records(path):
        pid = rec.get("promptId")
        if not isinstance(pid, str) or not pid:
            continue
        if out and out[-1]["turn"] == pid:
            continue
        content = _message_of(rec).get("content")
        text = content if isinstance(content, str) else ""
        head = " ".join(text.split())
        kind = ""
        if head.lstrip().startswith(_INJECTED_PREFIXES):
            kind = " [host-injected]"
            head = head[:80]
        out.append({
            "turn": pid,
            "at": str(rec.get("timestamp") or ""),
            "head": (head[:160] or "(no text)") + kind,
        })
    return out


def _turn_window(order: list[str], since: str, until: str, last: str) -> set[str]:
    """Which turn ids an extraction may look at, given the caller's window.

    A session transcript runs to megabytes and hundreds of turns, and an agent auditing
    the turn that just finished has no use for turn 3. Bounding the scan is therefore an
    input, not an optimization: without it `find` returns matches from an hour ago with
    equal prominence, and the agent pays to read them.

    ``since``/``until`` are turn ids, inclusive on both ends; an id that is not in the
    transcript is ignored rather than treated as empty, since the alternative is an
    extraction that silently returns nothing. ``last`` keeps the N most recent turns of
    whatever survives, so `--until <the audited turn> --last 10` reads as "the ten turns
    ending at this one" — which is the shape an auditor actually asks for.
    """
    lo, hi = 0, len(order)
    if since and since in order:
        lo = order.index(since)
    if until and until in order:
        hi = order.index(until) + 1
    window = order[lo:hi]
    try:
        n = int(last)
    except (TypeError, ValueError):
        n = 0
    if n > 0:
        window = window[-n:]
    return set(window)


def cmd_transcript() -> int:
    """Extract part of the session transcript INTO A FILE and print only its path.

    Argv::

        transcript index|turn|find --transcript P
                   [--turn ID] [--pattern RE]
                   [--since ID] [--until ID] [--last N] [--out F]

    Written for the audit agents, not for the main session. An agent auditing a claim needs
    to know what the session actually ran and said — often several turns back — and there
    are three bad ways to give it that. Asking the main agent to write it down makes the
    turn's own author the source for the record of the turn. Having guard accumulate every
    turn into a file, forever, pays for a full record on every turn to serve the few that
    are ever audited. Printing the extract to stdout puts it in the CALLER's context, which
    is the cost this whole design exists to avoid.

    So: the extract goes to a file, stdout carries the path and a one-line summary, and the
    agent Reads what it asked for — or hands the path to another agent, which is the cheap
    way for two of them to look at the same evidence.

    Fail-open like every other subcommand: an unreadable transcript, an unknown turn, or a
    bad pattern prints a one-line reason and exits 0. An agent that cannot get an extract
    must say so and judge on what it has, not stall.
    """
    argv = sys.argv[2:]
    op = argv[0].lower() if argv else ""
    opts: dict[str, str] = {}
    i = 1
    while i < len(argv) - 1:
        if argv[i].startswith("--"):
            opts[argv[i][2:]] = argv[i + 1]
            i += 2
        else:
            i += 1

    if op not in ("index", "turn", "find"):
        print("guard transcript: expected `index`, `turn`, or `find`.", file=sys.stderr)
        return 0
    tpath = opts.get("transcript", "")
    path = Path(tpath) if tpath else None
    if path is None or not path.is_file():
        print(f"guard transcript: no readable transcript at {tpath or '(none given)'}",
              file=sys.stderr)
        return 0

    project_dir = _cli_project_dir()
    session_id = opts.get("session", "") or path.stem
    out = Path(opts["out"]) if opts.get("out") else None
    rows = _turn_index(path)
    order = [r["turn"] for r in rows]
    window = _turn_window(order, opts.get("since", ""), opts.get("until", ""),
                          opts.get("last", ""))

    if op == "index":
        shown = [r for r in rows if r["turn"] in window]
        body = "# Turns in this session\n\n" + "\n".join(
            f"- `{r['turn']}` {r['at']} — {r['head']}" for r in shown) + "\n"
        dest = out or _extract_dir(project_dir, session_id) / "index.md"
        if not _write_extract(dest, body):
            print(f"guard transcript: could not write {dest}", file=sys.stderr)
            return 0
        print(f"{dest}\n{len(shown)} of {len(rows)} turns, oldest first.")
        _trace(project_dir, session_id, "transcript", "index", turns=len(shown))
        return 0

    if op == "turn":
        turn_id = opts.get("turn", "")
        turn = _turn_slice(str(path), turn_id)
        if turn is None:
            print(f"guard transcript: turn {turn_id or '(none given)'} is not in "
                  f"{path.name}", file=sys.stderr)
            return 0
        body = _render_turn(turn, turn_id)
        dest = out or _extract_dir(project_dir, session_id) / f"turn-{turn_id}.md"
        if not _write_extract(dest, body):
            print(f"guard transcript: could not write {dest}", file=sys.stderr)
            return 0
        print(f"{dest}\n{len(turn.get('tools', []))} tool calls, {len(body)} chars.")
        _trace(project_dir, session_id, "transcript", "turn", turn=turn_id,
               tools=len(turn.get("tools", [])))
        return 0

    pattern = opts.get("pattern", "")
    try:
        rx = re.compile(pattern, re.IGNORECASE)
    except (re.error, TypeError):
        print(f"guard transcript: {pattern!r} is not a valid regex", file=sys.stderr)
        return 0
    hits: list[str] = []
    seen: set[str] = set()
    current = ""
    for rec in _transcript_records(path):
        pid = rec.get("promptId")
        if isinstance(pid, str) and pid:
            current = pid
        if current not in window or rec.get("isSidechain") is True:
            continue
        blob = json.dumps(_message_of(rec).get("content"), ensure_ascii=False)
        m = rx.search(blob)
        if m:
            lo = max(0, m.start() - 200)
            hits.append(f"- turn `{current}`: …{blob[lo:m.end() + 200]}…")
            seen.add(current)
    body = (f"# Matches for `{pattern}`\n\n"
            f"Searched {len(window)} of {len(order)} turns.\n\n"
            + ("\n".join(hits) if hits else "(no match)") + "\n")
    dest = out or _extract_dir(project_dir, session_id) / "find.md"
    if not _write_extract(dest, body):
        print(f"guard transcript: could not write {dest}", file=sys.stderr)
        return 0
    print(f"{dest}\n{len(hits)} matches across {len(seen)} turns; "
          f"searched {len(window)} of {len(order)}.")
    _trace(project_dir, session_id, "transcript", "find", hits=len(hits))
    return 0


def _turn_identity(transcript_path: Any, prompt_id: Any) -> dict[str, Any] | None:
    """What KIND of turn this is, read from the transcript anchor. Never its content.

    Returns ``{origin_kind, command_name, bash_input}``, or None (fail-open) when the
    transcript is unreadable or the prompt_id is not in it. Every user of it is a skip,
    not an audit:

    - ``origin_kind`` — a typed prompt is ``"human"``. Anything else that opens a turn is
      machinery reporting in, and each such kind arrives with a fresh promptId and
      ``promptSource`` "system": ``"task-notification"`` for a background subagent's
      completion (NOT ``isMeta``, so otherwise indistinguishable from a typed prompt) and
      ``"peer"`` for an inbound ``SendMessage`` from a subagent or another session
      (``isMeta``). Both observed in 2.1.239. Recommending an audit on either is
      self-perpetuating, because guard's own dispatch is what produces them: the audit
      agents are background tasks, and they message the session back.
    - ``command_name`` — the slash command that opened the turn, so a turn opened by
      one of guard's own control commands can be skipped.
    - ``bash_input`` — the turn was opened by a user `!` command rather than a prompt.
      Such a turn carries no ``origin`` at all (verified in 2.1.239, session 6bc60bbf), so
      the ``origin_kind`` skip above lets it through; see `cmd_stop` for why it must not.

    Only the ANCHOR record is examined; records derived from the turn carry
    ``promptId=None`` and nothing about them changes the turn's kind. Kept separate from
    ``_turn_slice`` because the skips must be decided before guard does any work, and
    reading one record is cheaper than slicing a turn out of a multi-megabyte file.
    """
    if not isinstance(transcript_path, str) or not isinstance(prompt_id, str) or not prompt_id:
        return None
    path = Path(transcript_path)
    if not path.is_file():
        return None
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return None
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except (json.JSONDecodeError, ValueError):
            continue
        if not isinstance(rec, dict) or rec.get("promptId") != prompt_id:
            continue
        origin = rec.get("origin")
        content = _message_of(rec).get("content")
        text = content if isinstance(content, str) else ""
        return {
            "origin_kind": str(origin.get("kind") or "") if isinstance(origin, dict) else "",
            "command_name": _turn_command_name(text),
            "bash_input": text.lstrip().startswith(_BASH_TAG),
        }
    return None


def _load_config(project_dir: Path) -> dict[str, Any]:
    """Load the JSON config at guard.local.json, if present. Fail-open to defaults.

    Only keys present in DEFAULT_CONFIG are honored, and only when the supplied value
    matches the default's JSON type (every key is a str: the agent modes,
    ``router_model``, ``refs_dir``), so a malformed value can never change a setting by
    accident.
    """
    config = dict(DEFAULT_CONFIG)
    path = project_dir / CONFIG_REL
    if not path.is_file():
        return config
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, ValueError):
        return config
    if not isinstance(data, dict):
        return config
    for key, default in DEFAULT_CONFIG.items():
        # An ``AgentMode`` default round-trips through JSON as a plain str, and
        # ``isinstance("reuse", AgentMode)`` is False — so the accepted type has to be
        # widened for those keys or every mode in the file is silently dropped and only
        # the session state is ever honored. The accessor (``_agent_mode``) validates the
        # value; this only checks the shape.
        want = str if isinstance(default, StrEnum) else type(default)
        if key in data and isinstance(data[key], want):
            config[key] = data[key]
    return config


def _load_raw_config(project_dir: Path) -> dict[str, Any]:
    """Read guard.local.json as a raw dict (unmerged, no defaults applied), or {} if
    missing/malformed. Used by the ``settings`` CLI so it can edit one key in place
    while preserving every other key the user has set."""
    path = project_dir / CONFIG_REL
    if not path.is_file():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, ValueError):
        return {}
    return data if isinstance(data, dict) else {}


def _write_config(project_dir: Path, data: dict[str, Any]) -> bool:
    """Atomically write guard.local.json. Returns True on success."""
    path = project_dir / CONFIG_REL
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.parent / (path.name + ".tmp")
        tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        tmp.replace(path)
        return True
    except OSError:
        return False


def _read_state(project_dir: Path, session_id: str, config: dict[str, Any]) -> dict[str, Any]:
    default = {
        **{k: str(_agent_mode(config, k)) for k in AUDIT_AGENTS},
        # Per-turn guards keyed by the transcript prompt_id (a turn == one promptId).
        "last_audited_prompt_id": "",
        # The most recent auditable turn's prompt_id — the target a `/guard:<agent>`
        # command dispatches its agent for. Recorded by every Stop, switches or not.
        "pending_verify_prompt_id": "",
        # The session's transcript, recorded at Stop so the on-demand `/guard:*` path can
        # hand it to an agent that needs history. That payload does not carry it, and the
        # path is a session-long fact, so remembering it is cheaper than making the agent
        # go looking for a file it has no reliable way to name.
        "transcript_path": "",
        # Files written during one turn, accumulated by PostToolUse and read back at Stop
        # to decide whether a file-reading agent has anything to look at. Stored WITH the
        # prompt_id they belong to: a bare list would outlive its turn and point an agent
        # at files the current turn never touched. Two lists, one marker — the split is by
        # which agent can judge the file (source code for `comment-corrector`, instruction
        # files for `agents-md-auditor`), while "which turn was this" is the same question
        # for both and a second marker could only drift from the first.
        "edited_prompt_id": "",
        "edited_files": [],
        "edited_agent_docs": [],
        # Session-only mute, flipped by `/guard:toggle`. NOT a mode in front of the agent
        # switches the way the removed `audit_gate` was: it lives only in session state, so
        # it can never change what the project does by default, and the `status` subcommand
        # puts it in the user's status line so the muted state is visible rather than
        # remembered. A hidden mute is the failure that killed the old gate.
        "audit_paused": False,
        "updated_at": None,
    }
    path = _state_file(project_dir, session_id)
    if not path.is_file():
        return default
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError, ValueError):
        return default
    if not isinstance(data, dict):
        return default
    keys = (*AUDIT_AGENTS, "last_audited_prompt_id", "pending_verify_prompt_id",
            "transcript_path", "audit_paused",
            "edited_prompt_id", "edited_files", "edited_agent_docs", "updated_at")
    default.update({k: data[k] for k in keys if k in data})
    return default


def _write_state(project_dir: Path, session_id: str, state: dict[str, Any]) -> None:
    state["updated_at"] = _now_iso()
    path = _state_file(project_dir, session_id)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(state, ensure_ascii=False), encoding="utf-8")
        tmp.replace(path)
    except OSError:
        pass


def _parse_mode(value: str) -> AgentMode | None:
    """Parse a CLI mode word; None when the spelling is not recognized (the caller
    reports the error rather than guessing, since guessing here could silently turn an
    agent off or leave a stale instance in charge)."""
    v = value.strip().lower()
    if v in _MODE_ALIASES:
        return _MODE_ALIASES[v]
    try:
        return AgentMode(v)
    except ValueError:
        return None


def _agent_mode(cfg: dict[str, Any], key: str) -> AgentMode:
    """One agent's mode from a config or session-state dict, coerced to a valid member.

    Anything unrecognized lands on the default rather than raising: a hand-edited config
    must not be able to break the hook, and the ``settings`` CLI is where a bad value
    gets rejected out loud. A stringy value that is not a mode word therefore reads as
    ``off`` — the safe direction, since the alternative is guard acting on a setting the
    user did not write.
    """
    try:
        return AgentMode(str(cfg.get(key, DEFAULT_CONFIG[key])).strip().lower())
    except ValueError:
        return AgentMode(DEFAULT_CONFIG[key])


def _switch_on(cfg: dict[str, Any], key: str) -> bool:
    """Whether this agent may be recommended at all."""
    return _agent_mode(cfg, key) is not AgentMode.OFF


def _router_model(cfg: dict[str, Any]) -> str:
    """The model override for the router agent, or "" to leave the choice to the agent.

    Never validated against a list of names — an alias, a full id, or a provider's own
    name are all legitimate and the set moves. An empty value is not a fallback to some
    default here: it means guard prints no model line at all, so `agents/router.md`
    decides, which is where a subagent's model normally comes from.
    """
    return str(cfg.get("router_model", "")).strip()


# --------------------------------------------------------------------------- #
# the agents guard can recommend
# --------------------------------------------------------------------------- #
class AuditAgent(NamedTuple):
    """One agent guard can recommend. Mechanical facts only — no prose.

    Keyed in ``AUDIT_AGENTS`` by the agent's own bare name, which is also its config
    switch key, its playbook section, and — namespaced — its ``subagent_type``. One string
    for one agent: the setting the user types, the key in the state file, the section that
    says how to dispatch it, and the agent that gets dispatched cannot drift apart because
    they are the same string.

    ``reads`` is what the agent is pointed at — ``"turn"`` for the turn record guard
    wrote, ``"files"`` for the source files the turn edited, ``"agent-docs"`` for the
    ``AGENTS.md`` / ``CLAUDE.md`` files it edited, ``"prompt"`` for the user's question.
    It selects the paths the dispatch carries and gates eligibility, since a file-reading
    agent with no matching edit has no input at all.

    ``"files"`` and ``"agent-docs"`` are separate values rather than one "the turn's
    edits", because the two agents behind them judge different things and a shared list
    would hand each one files it has nothing to say about. ``comment-corrector`` judges a
    comment against the code under it and a markdown file gives it none; the agent-doc
    auditor judges instruction files against what an instruction file is for and a ``.py``
    is not one. Same reason ``_SOURCE_SUFFIXES`` and ``_AGENT_DOC_NAMES`` are disjoint:
    nothing may land in both lists, or one turn's edit would be audited twice under two
    criteria, one of which does not apply to it.

    ``"prompt"`` is the odd one and marks an agent that runs at the *other end* of a turn.
    Everything else here audits a finished response, so guard names it at Stop and hands it
    a path guard itself wrote. A ``"prompt"`` agent works on the question instead, before
    an answer exists — so there is no path to hand over (guard deliberately keeps no copy
    of the prompt; the main session is its only source), nothing at Stop to route it into,
    and its standing policy is stated once at SessionStart rather than per turn. Which is
    why ``_eligible_agents`` excludes it: the router triages finished turns, and a
    prompt-time agent has no material in one.

    ``verify_command`` marks the agents that also have their own ``/guard:*`` command over
    the last completed turn; it is what stops ``cmd_verify`` from dispatching an agent no
    command can reach.

    ``needs_history`` is whether this agent may need to look past the response — at the
    request, at what the turn ran, at what an earlier turn established. Those agents are
    given the transcript path and the turn id so they can extract what they need with the
    ``transcript`` subcommand; the others are not, because a pointer an agent has no use
    for is one it may chase anyway. Three need it: `claims-auditor`, since a claim made here
    is often grounded by a command run three turns ago; `deferrals-auditor`, since the
    request is what separates a deferral the assistant owed from a decision it correctly
    handed back; and `clarity-auditor`, since whether a term still needs explaining depends
    on whether an earlier turn already explained it. The correctors do not — Korean prose is
    judged as prose, and comments are judged against the code under them.

    What the agent DOES, how to dispatch it, and what to do with its report are all in
    ``hooks/context/dispatch-playbook.md``, under the section named by this key. None of
    it belongs here: every string guard prints is paid for in the main agent's context on
    the turn it prints it, and this text is the same on every turn — so it is stored once
    and read only when a turn is actually routed to that agent.
    """

    reads: str
    verify_command: bool
    needs_history: bool


# The plugin namespace every agent name is qualified with to become a `subagent_type`.
AGENT_NAMESPACE = "guard:"


def _agent_id(name: str) -> str:
    """The dispatchable `subagent_type` for an agent name (a plain AUDIT_AGENTS key)."""
    return AGENT_NAMESPACE + name


def _instance_name(name: str) -> str:
    """The addressable instance name for an agent held open across turns.

    Hyphen rather than colon, and prefixed: it is a `name` on the Agent call, not a
    `subagent_type`, and the two must not be confusable in the dispatch text. One name
    per agent per session is the whole scheme — guard needs no registry of running
    instances, because the name is derived from the agent, so the main agent can look for
    it and guard can name it without either of them tracking anything.
    """
    return "guard-" + name


# Order here is the order the agents appear in a recommendation. The three read-only
# auditors come first: their findings may change what the correctors should be run on.
# `refs-finder` sits last because it never appears in that recommendation at all — it runs
# before the answer, not after it — so its position is free.
AUDIT_AGENTS: dict[str, AuditAgent] = {
    "claims-auditor": AuditAgent(reads="turn", verify_command=True, needs_history=True),
    "deferrals-auditor": AuditAgent(reads="turn", verify_command=True, needs_history=True),
    "clarity-auditor": AuditAgent(reads="turn", verify_command=True, needs_history=True),
    "korean-corrector": AuditAgent(reads="turn", verify_command=True, needs_history=False),
    "comment-corrector": AuditAgent(reads="files", verify_command=False, needs_history=False),
    "agents-md-auditor": AuditAgent(reads="agent-docs", verify_command=False,
                                    needs_history=False),
    "refs-finder": AuditAgent(reads="prompt", verify_command=False, needs_history=False),
}


# Source files whose comments `comment-corrector` can judge. Deliberately not "every
# file the turn touched": the agent judges comments against the code under them, and a
# markdown or JSON edit gives it nothing to judge. Extension-based rather than
# content-sniffing because this runs on every edit and must stay a dict lookup.
_SOURCE_SUFFIXES = frozenset({
    ".py", ".pyi", ".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs", ".go", ".rs",
    ".java", ".kt", ".kts", ".c", ".h", ".cc", ".cpp", ".hpp", ".cs", ".rb", ".php",
    ".swift", ".scala", ".sh", ".bash", ".zsh", ".lua", ".sql", ".m", ".mm", ".dart",
    ".ex", ".exs", ".vue", ".svelte", ".zig",
})

# Filenames `agents-md-auditor` can judge. Matched on the name, not the suffix: what makes
# one of these auditable is that a coding agent loads it as standing instruction, and that
# is a property of the name the host looks for, not of it being markdown. Every other
# markdown file in a repository is prose nobody is instructed by, and auditing one against
# what an instruction file may contain would flag an ordinary document for having content.
#
# Lowercased before the lookup, since a repository may spell either one in any case and the
# host resolves them case-insensitively on macOS and Windows regardless.
_AGENT_DOC_NAMES = frozenset({"agents.md", "claude.md"})

# --------------------------------------------------------------------------- #
# the router
#
# guard makes NO model call of its own. When a turn finishes, the Stop hook decides one
# mechanical thing — is any agent even eligible — and then asks the main agent to dispatch
# ONE subagent, the router. The router reads the finished response and answers with the
# INSTRUCTIONS: which of the eligible specialists would find something in it, why each,
# and the dispatch for each.
#
# It writes the dispatch rather than guard printing it because of where the cost falls.
# guard's context lands in the main agent on every routed turn; the router's own
# definition is read once, by the router, and only when a turn is actually routed. A
# per-candidate dispatch block in the hook's `additionalContext` is paid four times over
# on every turn to be used at most four times and usually zero — the router clearing a
# turn is the common case. So the hook carries only what the router cannot know (where the
# answer file is, which agents are on, their modes, the edited files, the transcript
# pointer) and `agents/router.md` carries everything that describes an agent.
#
# That the router is an agent and not a `claude -p` child guard spawns itself is the
# design. A spawned child made the Stop hook block for the router's whole runtime at
# the end of every turn the user was waiting on, and it dragged in a set of problems
# that exist only because it was a child: it had to carry `--safe-mode` or guard's own
# Stop hook would fire inside it and recurse, it needed an explicit tool denylist
# because omitting `--allowedTools` leaves a child fully tooled, `--bare` was
# unusable because it takes auth down to `ANTHROPIC_API_KEY` only, and every one of
# spawn / timeout / exit code / envelope parsing was a failure path guard had to tell
# apart from a clean verdict. As a subagent none of that exists: it runs in the host's
# own dispatch machinery, its model lives in its definition, and the hook returns
# immediately.
#
# What travels as a FILE and what travels as PROSE is a per-case choice, not a policy.
# A file earns its place when the text has several readers who must all see the same
# thing (the turn record: the router plus every agent it names), or when it is long
# enough that carrying it in a message would crowd out the message (the Korean rewrite).
# Everything short and single-hop stays prose in the dispatch or the report: the roster,
# the edited-file list, the router's picks and its reason per pick. Routing a two-line
# verdict through a file would only add a read.
#
# The roster is built HERE, not in `agents/router.md`, because eligibility is per turn
# and per project: which switches are on, and which files this turn wrote. The router's
# definition holds everything that is the same every turn — the method, and the dispatch
# template per agent. An agent absent from the roster cannot be picked, which beats
# describing a disabled agent and appending "but this one is off".
#
# The result-handling line for an agent lives in exactly one place: its section of
# `hooks/context/dispatch-playbook.md`. Both paths read it from there — the on-demand
# `/guard:<agent>` path via `_agent_pointer`, the routed path via the router's own
# report — so there is nothing in Python to keep in sync with the markdown, and no
# duplicated guidance that could drift between the two.
# --------------------------------------------------------------------------- #
ROUTER_AGENT = "guard:router"


def _reads_turn(keys: Iterable[str]) -> bool:
    """Does any of ``keys`` read the turn's answer file?

    The gate on everything the answer file costs. That file exists for the agents whose
    input it IS (``reads="turn"``); ``comment-corrector`` reads the source files the turn
    wrote and never opens it. So a configuration with only ``comment-corrector`` on must
    not pay for it — neither the per-prompt instruction telling the session to write into
    it, nor the dispatch line naming it.
    """
    return any(AUDIT_AGENTS[k].reads == "turn" for k in keys if k in AUDIT_AGENTS)


def _eligible_agents(state: dict[str, Any], edited: list[str],
                     agent_docs: list[str] | None = None) -> list[str]:
    """The agents the router may choose from, in ``AUDIT_AGENTS`` order.

    Two mechanical gates, and only mechanical ones — everything that needs judgment is
    the router's call:

    - the switch, which is the user saying they are willing to have this agent run;
    - for a file-reading agent, at least one file of its own kind this turn wrote,
      because that list is the agent's whole input and nobody downstream can invent one.

    ``agent_docs`` defaults to none rather than being required, for the Codex adapter:
    it shares this function but mirrors no edited-file recording of its own, so every
    file-reading agent is ineligible there and passing empty lists is the honest answer.

    A ``reads="prompt"`` agent is excluded outright: it works on the question, so a
    finished turn holds nothing for it. Excluded HERE rather than where the dispatch is
    built, because ``eligible`` is also what decides whether ``cmd_stop`` emits anything at
    all — leaving it in would make a turn look routable on the strength of an agent that
    already ran, and Codex's adapter, which shares this function, would recommend it.

    Notably absent: any language test for ``korean-corrector``. Deciding whether a
    response is Korean enough to audit is a reading task, and the router does it better
    than a Hangul ratio that has to guess how many English identifiers a Korean answer
    may carry before it stops being Korean.
    """
    inputs = {"files": edited, "agent-docs": agent_docs or []}
    out: list[str] = []
    for key, spec in AUDIT_AGENTS.items():
        if not _switch_on(state, key):
            continue
        if spec.reads == "prompt":
            continue
        if spec.reads in inputs and not inputs[spec.reads]:
            continue
        out.append(key)
    return out


# --------------------------------------------------------------------------- #
# dispatch text
# --------------------------------------------------------------------------- #
# The input line each file-reading agent's path list is introduced by. Worded as what the
# agent is being handed, not as what to look for: the criteria are the agent's own and live
# in its definition, so a lead that previewed them would be the caller telling it what to
# find. The `in place` on the corrector is the exception and is not a criterion — it warns
# the main agent that those files come back changed.
_FILE_INPUT_LABELS = {
    "files": "- files to audit (comments only, in place):",
    "agent-docs": "- agent instruction files to audit:",
}


def _agent_inputs(project_dir: Path, session_id: str, prompt_id: str, key: str,
                  files: dict[str, list[str]]) -> list[str]:
    """The dispatch inputs for one agent: ONLY what the main agent cannot supply itself.

    For a turn-reading agent that is the answer file — the same path for every agent in one
    dispatch, so they all read and correct the one document the user will be shown.

    For a file-reading agent it is instead the paths this turn edited that its own criteria
    apply to, recorded by PostToolUse and looked up here by the agent's ``reads`` value: a
    main agent asked to recall which files it wrote will approximate, and these are the
    agents pointed at the repository rather than at the answer.

    ``session_id`` / ``prompt_id`` are here to BUILD that path, never to be handed over: an
    agent working on one turn has no use for guard's identifiers, and an extra pointer is
    one more thing it can wander into instead of doing its job.
    """
    reads = AUDIT_AGENTS[key].reads
    if reads in _FILE_INPUT_LABELS:
        return [_FILE_INPUT_LABELS[reads]] + [f"    {p}" for p in files.get(reads, ())]
    return ["- answer file: "
            f"{_turn_record_file(project_dir, session_id, prompt_id).resolve()}"]


# The playbook the main agent is sent to by section name. Resolved from this file's own
# location rather than from `CLAUDE_PLUGIN_ROOT`: the same script is the Codex adapter's
# library and a plain CLI the settings skill calls over Bash, and only one of those three
# has the env var set.
PLAYBOOK_REL = "hooks/context/dispatch-playbook.md"


def _playbook_path() -> Path:
    return Path(__file__).resolve().parent.parent / PLAYBOOK_REL


def _agent_pointer(project_dir: Path, session_id: str, prompt_id: str, keys: list[str],
                   files: dict[str, list[str]], modes: dict[str, AgentMode]) -> str:
    """Name the playbook sections for these agents and hand over their per-turn inputs.

    This is the whole dispatch instruction, and what is NOT in it is the point: how to
    dispatch an agent, what its report means, and what to do about it are the same on every
    turn, so they are stored once in the playbook and read only when a turn is actually
    routed. What guard prints is only what the playbook cannot know — which agents, in
    which mode, and the paths for this turn.

    The alternative, printing each agent's dispatch block here, costs the same text in the
    main agent's context on every routed turn, times every candidate, to be used by at
    most the ones the router picks and usually none. Having the ROUTER reproduce those
    blocks instead is no better: it makes an LLM re-type instructions it was handed, which
    is exactly where wording drifts.

    ``modes`` is passed in rather than re-read from config because the caller resolved it
    from session state, which can differ from the file for the live session.
    """
    lines = [f"Follow {_playbook_path()}, these sections in this order:"]
    for key in keys:
        lines.append(f"- `{key}`={modes[key].value}")
        lines.extend("  " + line for line in _agent_inputs(
            project_dir, session_id, prompt_id, key, files))
    return "\n".join(lines)


def _dispatch_context(project_dir: Path, session_id: str, prompt_id: str, lead: str,
                      keys: list[str], modes: dict[str, AgentMode],
                      files: dict[str, list[str]] | None = None,
                      transcript: str = "") -> str:
    """``additionalContext`` asking the main agent to dispatch these agents directly.

    The no-router path, reached two ways and for the same reason — there is nothing to
    triage, so routing would only add a hop. Either the user named the audit themselves
    with a `/guard:<agent>` command, or `cmd_stop` is dispatching a file-reading agent,
    whose selection is not a question the router can answer.
    """
    keys = list(keys)
    block = _agent_pointer(project_dir, session_id, prompt_id, keys, files or {}, modes)
    if transcript and any(AUDIT_AGENTS[k].needs_history for k in keys):
        block += f"\n- history: transcript {transcript}, turn {prompt_id}"
    return "\n\n".join([lead, block])


def _router_context(project_dir: Path, session_id: str, prompt_id: str, lead: str,
                    eligible: list[str], modes: dict[str, AgentMode],
                    config: dict[str, Any], transcript: str = "") -> str:
    """``additionalContext`` for the Stop path: the playbook pointer, then this turn's data.

    Every line here is paid in the main agent's context at the end of EVERY routed turn,
    including the many the router then clears, so the test each line has to pass is: could
    the playbook have said this instead? If yes, it is deleted from here and said there,
    where it is read once by whoever needs it.

    Everything that used to spell out the procedure failed that test and is gone. What is
    left is one imperative and a list of fields, because the ROUTER now returns the next
    instruction itself: it names the playbook and the sections to follow, so the main agent
    never reads a section about routing and the playbook has none. The rest — dispatch in one
    message, in the order named, a clean result is one line, gather nothing yourself — is in
    the playbook's `Dispatching` section, read once by whoever is sent there.

    What is left cannot come from anywhere else: where the playbook is, where the record is,
    which agents are switched on and in what mode, and the transcript pointer for the agents
    whose section asks for it. The field names are terse on purpose — the playbook says what
    each one is for.

    Deliberately absent: any summary of the turn, from guard or from the main agent. Priming
    an audit with the author's account of the work is how an unexamined claim becomes an
    established one — every agent reads the turn itself and forms its own view, which is why
    the record is required to be verbatim.

    The ROUTER is always a fresh instance, whatever the agents are set to. Its question is
    about this turn, and an instance carrying the last five turns is one that can answer it
    from the wrong one — the failure would be silent, and routing is the step nothing else
    checks. Cheapness is not what it is tuned for: a router that misreads the turn either
    ships the defect or spends a subagent for every agent it named for nothing, and both cost
    more than the routing call itself ever will. Hence the model in `agents/router.md` is a
    capable one rather than the cheapest that could hold the method.
    """
    model = _router_model(config)
    fields = [f"- playbook: {_playbook_path()}"]
    # The two turn files share a long absolute prefix, so it is spelled ONCE and each file
    # is named relative to it as `{turn dir}/<name>`. The placeholder is written into the
    # value rather than explained anywhere: a dispatch that shows the substitution needs no
    # prose about it, and the layout itself stays in `_turn_record_file` /
    # `_turn_request_file` — a router told how to BUILD these paths would be a second copy
    # of that layout, in prose, and a drifted copy reads nothing and clears every turn.
    #
    # Emitted in the same shape whether or not the request file exists. The dir form is a
    # few characters longer than one plain absolute path, and paying those is worth more
    # than giving the router two input shapes to tell apart.
    answer = _turn_record_file(project_dir, session_id, prompt_id).resolve()
    fields.append(f"- turn dir: {answer.parent}")
    # Unconditional: every candidate reaching the router is a `reads="turn"` agent, so the
    # answer file is always the thing being routed on. The file-reading agents are
    # dispatched around the router (see `cmd_stop`) and their path lists go with that
    # dispatch, which is why no candidate line here carries a path.
    fields.append(f"- answer file: {{turn dir}}/{answer.name}")
    # The user's own words, for the ROUTER and no other agent. Its one judgment is
    # materiality, and materiality is relative to what was asked: the same explanatory
    # paragraph is the answer's substance when the user asked how something works, and
    # padding when they asked for a one-line setting change. Routing on the answer alone
    # cannot separate those, and it fails in the expensive direction — a turn that merely
    # READS like an explanation draws agents that find nothing, which is what teaches the
    # user to wave the recommendation through. What the request may and may not do with a
    # pick is stated in `agents/router.md`, read once by the router, not here, where it
    # would be paid on every routed turn. Conditional on the file existing because
    # `cmd_user_prompt` is what writes it: a turn it never saw still routes on the answer.
    # The hook decides that, not the router — absence learned from a failed Read cannot be
    # told apart from a path the router built wrong, and that failure is silent.
    request = _turn_request_file(project_dir, session_id, prompt_id).resolve()
    if request.is_file():
        fields.append(f"- request file: {{turn dir}}/{request.name}")
    fields.append("- candidates: " + ", ".join(f"`{k}`={modes[k].value}" for k in eligible))
    if transcript and any(AUDIT_AGENTS[k].needs_history for k in eligible):
        fields.append(f"- history: transcript {transcript}, turn {prompt_id}")
    if model:
        # Phrased as an instruction, unlike every other field, because it is the only one
        # consumed BEFORE the playbook is opened: the router is dispatched straight off
        # this block and only its report sends the main agent to a playbook section, so
        # there is no later text that could say what to do with a bare value. Left as
        # `- router model: opus` it reads as a fact about the router rather than an
        # argument to pass, and the dispatch silently falls back to `agents/router.md`.
        fields.append(
            f"- dispatch `guard:router` with `model: {model}` — overrides agents/router.md")
    return lead + "\n\n" + "\n".join(fields)


# The lead for a routed turn. There is no second mode: a switch the user turned on is
# the user saying they want this audit, so asking again every turn would be a formality
# that trains them to wave it through. What the main agent must not do is quietly swallow
# the result — the report is the point.
_ROUTE_LEAD = (
    "guard: audit the turn you just finished. Dispatch `guard:router` (subagent_type: "
    "\"guard:router\") with the inputs below and follow its report."
)


# The lead for the file-reading agents, which never go through the router. It says what the
# turn did rather than what to look for: each agent's criteria are its own, and a lead that
# previewed them would be the caller telling it what to find. One lead covers however many
# of them are eligible, because the per-agent input lines below it already say which files
# each one gets — a lead per agent would be the same sentence twice.
_DIRECT_LEAD = (
    "guard: this turn edited files in the repository. Audit them."
)


# Same dispatch, when a router block precedes it. The one thing the main agent could
# plausibly get wrong here is sequencing — the router block above it ends in "follow its
# report", which reads as something to finish first — so the concurrency is spelled out.
# Waiting would cost a round trip for agents that share no input with the routed ones.
_DIRECT_LEAD_WITH_ROUTER = (
    "guard: this turn also edited files in the repository. Audit them. Dispatch these in "
    "the SAME message as the router above — they read neither the answer file nor the "
    "router's report, so they wait for nothing."
)


# --------------------------------------------------------------------------- #
# subcommands
# --------------------------------------------------------------------------- #
# What the main agent is told at the START of a turn, when guard has anything switched on.
# It fires on EVERY prompt, including the many that are never audited, so it is one sentence
# and a path.
#
# The substance goes in the FILE and the reply stays short, and that ordering is the whole
# point: it makes the full text cross the wire once. Answer in the reply and the audited
# version has to be printed a second time; answer in the file and a correction is a small
# edit to it, with the reply carrying only what changed. The file is also the only version
# that CAN be corrected — a reply that has already been printed cannot be, and the earlier
# shape left the user reading the flawed text with a list of fixes underneath it.
_DRAFT_LEAD = (
    "guard: put your answer's substance in {path}; keep the reply short and name that path. "
    "guard audits that file when the turn ends."
)


def cmd_user_prompt() -> int:
    """UserPromptSubmit. Names the file the turn's answer is written to, and saves the request.

    It has to be this hook, for both jobs. The draft path, because a Stop hook is too late:
    by the time Stop runs the answer has already been printed to the user, and a printed
    answer cannot be corrected — audit-then-correct only works if the answer also exists
    somewhere editable, and only the main agent can put it there while the turn is running.
    The request, because this is the only event that carries it; guard's turn store holds the
    answer and nothing else, and the router cannot go to the transcript for it.

    guard keeps no general copy of the user's prompt — it used to, as half of a turn store
    nothing reads any more. What `_write_turn_request` restores is narrower than what was
    removed: one reader, the router, and one question, how much of the answer the user
    actually asked for.

    Silent when no on agent reads the turn (``_reads_turn``) — an unconfigured guard, or one
    running only ``comment-corrector``, adds nothing to any prompt. Also silent for guard's
    own control commands, whose turns are never audited.
    """
    project_dir = _project_dir()
    payload = _read_payload()
    if payload is None or project_dir is None:
        return 0
    session_id = _session_id(payload)
    if session_id is None:
        return 0
    prompt = payload.get("prompt")
    prompt = prompt if isinstance(prompt, str) else ""
    if _CONTROL_CMD_RE.match(prompt.strip()):
        _trace(project_dir, session_id, "user-prompt", "skip_control_cmd")
        return 0

    config = _load_config(project_dir)
    state = _read_state(project_dir, session_id, config)
    # Muted by `/guard:toggle`: no audit is coming, so naming a file for the answer would
    # ask the user to read a file nothing is going to correct.
    if _audit_paused(state):
        _trace(project_dir, session_id, "user-prompt", "skip_paused")
        return 0
    prompt_id = payload.get("prompt_id")
    # Gated on the agents that READ the answer file, not on every switch: see `_reads_turn`.
    on = [k for k in AUDIT_AGENTS if _switch_on(state, k)]
    if not _reads_turn(on) or not (isinstance(prompt_id, str) and prompt_id):
        _trace(project_dir, session_id, "user-prompt", "seen")
        return 0

    # Before the lead, so a write that fails cannot be mistaken for the turn being
    # unroutable: the lead goes out either way and the router adapts to the file's absence.
    if prompt.strip():
        _write_turn_request(project_dir, session_id, prompt_id, prompt)
    path = _turn_record_file(project_dir, session_id, prompt_id).resolve()
    print(_DRAFT_LEAD.format(path=path))
    _trace(project_dir, session_id, "user-prompt", "draft_path", prompt_id=prompt_id)
    return 0


def _emit_expansion(msg: str) -> None:
    output = {"hookSpecificOutput": {"hookEventName": "UserPromptExpansion", "additionalContext": msg}}
    json.dump(output, sys.stdout)


def _emit_stop_context(msg: str) -> None:
    """Emit a Stop hook's ``additionalContext``.

    Not ``decision: "block"``. Per the official hooks docs
    (https://code.claude.com/docs/en/hooks, "Stop decision control"; excerpt at
    ``wiki/ref/claude-code-stop-hook-decision-control.md``) both keep the conversation
    going so Claude can act on the text, and both run under the same loop protections
    (``stop_hook_active`` and the 8-consecutive-continuation cap). The difference is how
    it reads: block surfaces as a hook error, while this is labelled ``Stop hook
    feedback``. guard's recommendation is guard working, not guard failing.
    """
    output = {"hookSpecificOutput": {"hookEventName": "Stop", "additionalContext": msg}}
    json.dump(output, sys.stdout)


def cmd_verify() -> int:
    """UserPromptExpansion for the per-agent ``/guard:<agent>`` commands.

    The agent comes from argv (``verify claims-auditor`` | ``deferrals-auditor`` |
    ``clarity-auditor`` | ``korean-corrector``), one per command, so each skill dispatches
    exactly its own agent and the choice is not a dispatch input the model has to be
    trusted to honor.

    Works regardless of the switches: a switch governs what guard recommends UNASKED,
    while running the command is the user asking for this one audit now. Refusing it
    would leave the user no way to check the very agent they keep switched off, which is
    the main reason to keep it off in the first place.

    ``pending_verify_prompt_id`` names the turn, and the record for it already holds that
    turn's response — every Stop writes that section, whatever the switches say, which is
    what makes this command work in a project that keeps every switch off. The main agent
    still appends the request, the tool activity, and the earlier evidence, exactly as on
    a routed turn.
    """
    key = sys.argv[2].strip().lower() if len(sys.argv) > 2 else ""
    spec = AUDIT_AGENTS.get(key)
    if spec is None or not spec.verify_command:
        return 0
    project_dir = _project_dir()
    payload = _read_payload()
    if payload is None or project_dir is None:
        return 0
    session_id = _session_id(payload)
    if session_id is None:
        return 0

    config = _load_config(project_dir)
    state = _read_state(project_dir, session_id, config)

    pid = state.get("pending_verify_prompt_id") or ""
    if not pid:
        _emit_expansion("guard: no completed turn is available to audit yet. "
                        f"Ask something first, then run `/guard:{key}`.")
        _trace(project_dir, session_id, "verify", "no_pending", agent=key)
        return 0

    context = _dispatch_context(
        project_dir, session_id, pid,
        "guard: audit the last completed turn, on request.", [key],
        {key: _agent_mode(state, key)},
        transcript=str(state.get("transcript_path") or ""))
    _emit_expansion(context)
    _trace(project_dir, session_id, "verify", "dispatch", agent=key, prompt_id=pid)
    return 0


# Cap on the files one turn may hand a file-reading agent. Past this the list stops
# being an audit target and becomes a sweep of the whole change: the agent must read
# every file in full to judge it — a comment against the code under it, an instruction
# file against what it points at — and the skills that dispatch these by hand ask the
# user to narrow at roughly this size for the same reason. Recording stops at the cap
# rather than dropping the oldest entries — the earliest edits of a turn are as worth
# auditing as the last, and a stable prefix keeps the recommendation reproducible.
EDITED_FILES_MAX = 20

# Which state list a PostToolUse target belongs in, if any. The two tests are disjoint by
# construction (`_SOURCE_SUFFIXES` holds no `.md`), so the order here does not decide
# anything — but a name landing in both would be audited twice under criteria only one of
# which applies to it, which is why any future entry must keep them disjoint.
def _edited_bucket(target: Path) -> str | None:
    if target.suffix.lower() in _SOURCE_SUFFIXES:
        return "edited_files"
    if target.name.lower() in _AGENT_DOC_NAMES:
        return "edited_agent_docs"
    return None


def _record_edited_source(project_dir: Path, payload: dict, tool_input: Any,
                          config: dict[str, Any]) -> None:
    """Note a file this turn wrote, for a later file-reading agent's recommendation.

    Two lists, chosen by `_edited_bucket`: source files for `comment-corrector`, agent
    instruction files for `agents-md-auditor`. Anything else is not recorded — an agent
    handed a file its criteria say nothing about spends its context proving that.

    Only inside the project: an audit of a file outside the working tree is not this
    turn's work to fix. Files under guard's own state are excluded too — a turn slice is
    a record, not code, and guard's own `AGENTS.md` under the refs dir is an index the
    `post-edit` refs check already governs.

    Silent and best-effort. A miss here costs one skipped recommendation; a raise here
    would surface as a hook failure on an ordinary edit, which is far worse.
    """
    prompt_id = payload.get("prompt_id")
    session_id = _session_id(payload)
    if not isinstance(prompt_id, str) or not prompt_id or session_id is None:
        return
    target = _tool_target_path(project_dir, tool_input)
    if target is None:
        return
    bucket = _edited_bucket(target)
    if bucket is None:
        return
    try:
        project = project_dir.resolve()
        state_root = _state_root(project_dir).resolve()
    except OSError:
        return
    if project not in target.parents or state_root in target.parents:
        return

    state = _read_state(project_dir, session_id, config)
    # A new turn resets BOTH lists off the one marker; without this, files from the
    # previous turn would ride along into this turn's recommendation. Resetting only the
    # bucket being written would leave the other holding the previous turn's files under
    # this turn's id, which is the same bug with an extra step.
    if state.get("edited_prompt_id") != prompt_id:
        state["edited_prompt_id"] = prompt_id
        state["edited_files"] = []
        state["edited_agent_docs"] = []
    files = state[bucket]
    if not isinstance(files, list):
        files = []
    path = str(target)
    if path in files or len(files) >= EDITED_FILES_MAX:
        return
    files.append(path)
    state[bucket] = files
    _write_state(project_dir, session_id, state)
    _trace(project_dir, session_id, "post-edit", "edited_recorded",
           prompt_id=prompt_id, bucket=bucket, file=target.name, count=len(files))


def _edited_files(state: dict[str, Any], prompt_id: str, bucket: str) -> list[str]:
    """The files of one bucket THIS turn wrote, as recorded by PostToolUse.

    Empty unless the recorded list belongs to this prompt_id and the files still exist:
    a turn that edited a file and then deleted or moved it leaves nothing to audit, and
    handing an agent a missing path would spend it on a read failure.
    """
    if state.get("edited_prompt_id") != prompt_id:
        return []
    files = state.get(bucket)
    if not isinstance(files, list):
        return []
    return [f for f in files if isinstance(f, str) and f and Path(f).is_file()]


def _tool_target_path(project_dir: Path, tool_input: Any) -> Path | None:
    """Absolute, resolved target path of a mutating tool call, or None.

    Reads the path from the PreToolUse `tool_input` (`file_path` for
    Write/Edit/MultiEdit, `notebook_path` for NotebookEdit). Resolving means a
    relative path or `..` cannot smuggle a write past the path-based checks below.
    """
    if not isinstance(tool_input, dict):
        return None
    raw = tool_input.get("file_path") or tool_input.get("notebook_path")
    if not isinstance(raw, str) or not raw:
        return None
    try:
        target = Path(raw)
        if not target.is_absolute():
            target = project_dir / target
        return target.resolve()
    except OSError:
        return None


def _targets_refs_dir(project_dir: Path, tool_input: Any, config: dict[str, Any]) -> bool:
    """True when a mutating tool's target path is inside the refs directory
    (`wiki/ref/` by default, or the validated `refs_dir` config path)."""
    target = _tool_target_path(project_dir, tool_input)
    if target is None:
        return False
    try:
        refs = _refs_dir(project_dir, config).resolve()
    except OSError:
        return False
    return target == refs or refs in target.parents


def cmd_stop() -> int:
    project_dir = _project_dir()
    payload = _read_payload()
    if payload is None or project_dir is None:
        return 0
    session_id = _session_id(payload)
    if session_id is None:
        return 0

    # Recursion / re-entry guard: never continue twice in a row.
    if payload.get("stop_hook_active") is True:
        _trace(project_dir, session_id, "stop", "skip_active")
        return 0

    response = payload.get("last_assistant_message")
    if not (isinstance(response, str) and response.strip()):
        return 0

    # The turn is the transcript prompt_id. Without it there is no per-turn marker to
    # write and no way to tell a real turn from a background completion — fail open.
    prompt_id = payload.get("prompt_id")
    if not (isinstance(prompt_id, str) and prompt_id):
        _trace(project_dir, session_id, "stop", "skip_no_prompt_id")
        return 0

    config = _load_config(project_dir)
    state = _read_state(project_dir, session_id, config)

    # How the turn was opened decides whether guard says anything at all. Three skips, and
    # the first is not politeness: guard audits an answer to the USER, so a turn opened by
    # anything other than a person typing is machinery reporting in — a background agent's
    # completion, a subagent's `SendMessage` — and auditing it puts guard in a loop with
    # itself, since guard's own dispatch is what produced it. The turn also gets no record
    # file and does not become the `/guard:<agent>` target, so the main agent is left
    # holding exactly one answer file per question: the user's.
    #
    # Every named non-human kind is skipped rather than a list of the two seen so far, so a
    # kind added later cannot reopen the loop. An ABSENT kind still audits: if `origin`
    # stops being emitted, guard staying noisy is recoverable and guard going silently
    # dormant is not.
    identity = _turn_identity(payload.get("transcript_path"), prompt_id)
    if identity is not None:
        origin_kind = identity["origin_kind"]
        if origin_kind and origin_kind != "human":
            _trace(project_dir, session_id, "stop", "skip_nonhuman_turn",
                   prompt_id=prompt_id, origin_kind=origin_kind)
            return 0
        # A turn opened by one of guard's own control commands is guard reporting on
        # guard: the response is a relay of an audit, not an answer to a question the
        # user asked. Skipping it BEFORE the record write below is the load-bearing
        # part — were such a turn to become the pending target, the next
        # `/guard:<agent>` would audit the previous audit's relay instead of the answer
        # the user actually wants checked.
        cmd_name = identity["command_name"]
        if cmd_name and _is_control_command_name(cmd_name):
            _trace(project_dir, session_id, "stop", "skip_control_cmd",
                   prompt_id=prompt_id, command=cmd_name)
            return 0
        # A turn opened by a user `!` command. `UserPromptSubmit` does not fire for one —
        # a `!` command is not a prompt — so no answer file was ever named, and guard's
        # whole premise is audit-then-CORRECT: the answer has to exist somewhere editable
        # while the turn is still running. What Stop would hand an auditor here is the
        # fallback copy it just made of an answer already printed, which no correction can
        # reach. (Verified in 2.1.239, session 6bc60bbf: every turn in the transcript got
        # the draft path except the `!` one.) This skip was removed in v0.45.0 on a
        # different rationale — that guard cut the turn slice itself and the `!` output
        # landed after the response, so evidence trailed the claims. That reason is indeed
        # gone; this one replaces it, and is about the record, not the evidence.
        #
        # Before the record write, like the control-command skip above: a `!` turn must not
        # displace the user's actual question as the `/guard:<agent>` target.
        if identity.get("bash_input"):
            _trace(project_dir, session_id, "stop", "skip_bash_input", prompt_id=prompt_id)
            return 0

    # Both of these happen whether or not any switch is on. They are what the on-demand
    # `/guard:<agent>` commands target, and those are the user asking for an audit now —
    # refusing them because the automatic recommendation is off would take away the very
    # thing switching everything off is meant to leave in place.
    #
    # Writing the response here rather than in the recommendation path is deliberate: it
    # is the one part of the record guard is handed for free, and it is the part that must
    # not pass through the author's hands. An hour-old turn the user asks about is still
    # quoted exactly.
    state["pending_verify_prompt_id"] = prompt_id
    if isinstance(payload.get("transcript_path"), str):
        state["transcript_path"] = payload["transcript_path"]
    _write_turn_response(project_dir, session_id, prompt_id, response)

    # Muted by `/guard:toggle`. Checked AFTER the two lines above, on purpose: the pending
    # target and the response still get recorded, so `/guard:claims-auditor` on the turn the
    # user just muted still has something to audit. Muting stops the recommendation, not the
    # user's ability to ask for one.
    if _audit_paused(state):
        _write_state(project_dir, session_id, state)
        _trace(project_dir, session_id, "stop", "skip_paused", prompt_id=prompt_id)
        return 0

    # Once per turn. `stop_hook_active` already covers the normal path, but the
    # recommendation asks the main agent to dispatch background agents, and each of
    # those completions opens a transcript turn of its own; a marker keyed on the
    # prompt_id does not depend on the payload flag surviving that.
    if state.get("last_audited_prompt_id") == prompt_id:
        _write_state(project_dir, session_id, state)
        _trace(project_dir, session_id, "stop", "skip_already_recommended",
               prompt_id=prompt_id)
        return 0

    edited = _edited_files(state, prompt_id, "edited_files")
    agent_docs = _edited_files(state, prompt_id, "edited_agent_docs")
    eligible = _eligible_agents(state, edited, agent_docs)
    modes = {k: _agent_mode(state, k) for k in eligible}
    if not eligible:
        _write_state(project_dir, session_id, state)
        _trace(project_dir, session_id, "stop", "none_eligible", prompt_id=prompt_id)
        return 0

    # The marker is spent before the recommendation goes out, not after. One
    # recommendation per turn, whatever the main agent does with it: the alternative is
    # a turn that gets re-recommended because the first dispatch is still in flight.
    state["last_audited_prompt_id"] = prompt_id
    _write_state(project_dir, session_id, state)

    transcript = payload.get("transcript_path")
    transcript = transcript if isinstance(transcript, str) else ""
    # Split by what each agent reads, because only one of the two groups is a triage
    # question. Routing asks "is there material here for this agent", and for a
    # file-reading agent that is a diff-level judgment — logic changed, or just a rename
    # or a formatting pass — the router cannot make from what it would be given: a file
    # list is the agent's input, not a diff, and reading those files shows their current
    # state, never what this turn changed in them. So routing them can only restate what
    # `_eligible_agents` already decided, and bill a subagent for it.
    #
    # The two dispatches also need no ordering between them. The auditors-before-correctors
    # rule in the playbook exists so a corrector does not rewrite a sentence an auditor was
    # about to flag, and it is entirely about the answer file — which no file-reading agent
    # opens. Sharing no input with the routed agents, they go out in the same message and
    # run alongside the router rather than after it. They need no ordering among themselves
    # either: their file lists are disjoint by construction (`_edited_bucket`), so the one
    # that edits cannot touch what the one that only reports is reading.
    routed = [k for k in eligible if AUDIT_AGENTS[k].reads == "turn"]
    direct = [k for k in eligible if AUDIT_AGENTS[k].reads in ("files", "agent-docs")]
    blocks: list[str] = []
    if routed:
        blocks.append(_router_context(project_dir, session_id, prompt_id, _ROUTE_LEAD,
                                      routed, modes, config, transcript))
    if direct:
        lead = _DIRECT_LEAD_WITH_ROUTER if routed else _DIRECT_LEAD
        blocks.append(_dispatch_context(
            project_dir, session_id, prompt_id, lead, direct, modes,
            {"files": edited, "agent-docs": agent_docs}, transcript))
    context = "\n\n".join(blocks)
    outcome = "routed" if routed and not direct else (
        "dispatched_direct" if direct and not routed else "routed_and_direct")
    # `additionalContext`, not `decision: "block"`. Per the official hooks docs
    # (https://code.claude.com/docs/en/hooks, "Stop decision control"; excerpt saved at
    # wiki/ref/claude-code-stop-hook-decision-control.md) the two continue the
    # conversation identically and share the same loop protections, but block is
    # reported as a hook ERROR while this shows as `Stop hook feedback`. A
    # recommendation is guard working as designed, so it must not look like a failure.
    _emit_stop_context(context)
    _trace(project_dir, session_id, "stop", outcome, prompt_id=prompt_id,
           eligible=",".join(eligible))
    return 0


def _export_to_bash_env(name: str, value: str) -> bool:
    """Persist one ``export`` into the session's Bash environment. True if written.

    SessionStart is handed ``CLAUDE_ENV_FILE``, a path whose ``export`` lines reach every
    later Bash command Claude Code runs (`wiki/ref/claude-code-hooks-session-env.md`). It is
    the only channel by which a Bash-invoked verb learns something the HOST decided rather
    than inferring it, and guard uses it for two values: the project root and the resolved
    refs directory.

    ``GUARD_``-prefixed names only, never ``CLAUDE_PROJECT_DIR``: the host owns that name,
    other tooling reads its presence as "running inside a hook", and guard exporting it into
    every shell in the session would be guard answering for the host.

    Appended only when the identical line is not already present. SessionStart registers no
    matcher, so it fires on `startup`, `resume`, `clear`, `compact` and `fork` alike, and a
    blind append added the same export once per compaction for the life of the session —
    which is what `GUARD_REFS_DIR` did before this became shared.

    Best-effort, silent on failure: everything that reads these has a fallback, and the
    session's context lines go out either way.
    """
    env_file = os.environ.get("CLAUDE_ENV_FILE", "").strip()
    if not env_file:
        return False
    line = f"export {name}={shlex.quote(value)}"
    try:
        path = Path(env_file)
        if path.is_file() and line in path.read_text(encoding="utf-8").splitlines():
            return False
        with path.open("a", encoding="utf-8") as fh:
            fh.write(line + "\n")
    except OSError:
        return False
    return True


def cmd_session_start() -> int:
    # Sweep both state and logs on the same age policy. State is intentionally NOT
    # cleared at SessionEnd: a session can be resumed later (`claude --resume`), and
    # its switch flags must survive the gap. Age-based expiry is the
    # only reaper, so a resumed session keeps its state as long as it is touched
    # within the retention window.
    project_dir = _project_dir()
    if project_dir is None:
        return 0
    # Before the sweep: the sweep can fail on a filesystem error, and this export is what
    # keeps the CLI verbs off their inferred fallback for the rest of the session.
    exported = _export_to_bash_env("GUARD_PROJECT_DIR", str(project_dir))
    root = _state_root(project_dir)
    cutoff = time.time() - ORPHAN_MAX_AGE_SECONDS
    for sub in ("state",):
        d = root / sub
        if not d.is_dir():
            continue
        try:
            entries = list(d.iterdir())
        except OSError:
            continue
        for entry in entries:
            try:
                if entry.is_file() and entry.stat().st_mtime < cutoff:
                    entry.unlink()
            except OSError:
                pass
    # `trace.log` sits at the root, not under `state/`, so the loop above never reached it
    # and the log grew without bound — the same way `extracts` did, and found the same way.
    # What the age policy buys here is narrower than it looks: every trace write refreshes
    # the mtime, so this reaps a log left behind by a project that has stopped tracing, and
    # never one being actively written. Bounding a live log needs a size check, which this
    # is not.
    trace = _trace_file(project_dir)
    try:
        if trace.is_file() and trace.stat().st_mtime < cutoff:
            trace.unlink()
    except OSError:
        pass
    # Dir-per-session trees. Swept on the directory's own mtime, never on its name: an
    # extract directory is named from `--session` when the caller passes one and from the
    # transcript's filename when it does not, so nothing here may assume the name is a
    # session id. `extracts` was missing from this sweep and grew without bound — the
    # agents that extract history write there on every audit, and guard runs in other
    # people's repositories, where a directory nothing reaps is a directory nobody asked
    # for.
    for sub in ("turns", "extracts"):
        sub_root = root / sub
        if not sub_root.is_dir():
            continue
        try:
            sess_dirs = list(sub_root.iterdir())
        except OSError:
            continue
        for d in sess_dirs:
            try:
                if not (d.is_dir() and d.stat().st_mtime < cutoff):
                    continue
                # One level of children only, which is all either tree has. rmdir then
                # fails on a dir holding anything deeper rather than deleting blind.
                for child in d.iterdir():
                    try:
                        child.unlink()
                    except OSError:
                        pass
                d.rmdir()
            except OSError:
                pass
    # The resolved refs directory, so a Bash caller gets it with one `echo` instead of
    # re-deriving the `refs_dir` validation from the raw config.
    session_cfg = _load_config(project_dir)
    refs = _refs_dir(project_dir, session_cfg)
    _export_to_bash_env("GUARD_REFS_DIR", str(refs))

    # The injected contract states the general rule — a doc-based claim cites the source
    # URL and a local saved copy — but not where this project keeps that copy, which
    # is per-project config (`refs_dir`). Inject the resolved path here instead: for
    # SessionStart, plain stdout becomes context the model can act on (docs:
    # https://code.claude.com/docs/en/hooks, "Exit code 0"). Without it the judge
    # would fail a docs claim for a missing refs copy that nothing told the model
    # where to write.
    print(
        "guard: when a claim rests on official documentation, save the cited content "
        f"to this project's refs directory — {refs} — and cite both the source URL "
        "and that local path. The same path is in $GUARD_REFS_DIR for Bash."
    )

    # Name the playbook once, at the session's opening, when guard has anything switched
    # on. The Stop hook repeats the path on each routed turn — one line, and it must,
    # because context compaction can drop this one — but stating it here is what lets that
    # line stay a path instead of an explanation of what the file is for.
    #
    # `reads="prompt"` is excluded from the test: that agent runs before the answer, so a
    # project running only it has no audit at all and this sentence would be false.
    if any(_switch_on(session_cfg, k) for k, spec in AUDIT_AGENTS.items()
           if spec.reads != "prompt"):
        print(
            "guard: audits are on for this project. When a turn finishes, guard names the "
            f"agents to consider and points at {_playbook_path()}, which says how to "
            "dispatch each one and what to do with what it reports. Read only the sections "
            "you are named; do not read the file until then."
        )

    # `refs-finder` is the one agent guard announces here instead of naming it per turn,
    # and this is the whole announcement. It runs BEFORE an answer exists, so there is no
    # Stop recommendation to ride on; the alternative was a line on every UserPromptSubmit,
    # billing every turn in the session for an agent that is off by default and wanted only
    # on the questions that touch saved docs. Once is enough because SessionStart registers
    # no matcher and so fires on every source — `startup`, `resume`, `clear`, `compact`,
    # `fork` — which means a compaction that drops this line immediately restates it
    # (https://code.claude.com/docs/en/hooks, excerpt at
    # wiki/ref/claude-code-hooks-session-env.md).
    #
    # Not on Codex: it ships one named agent installed by `$guard:setup` and no
    # refs-finder, and this module is its adapter's library — so without the host test it
    # would be told to dispatch an agent that does not exist there.
    #
    # The refs directory is deliberately not repeated: the line printed just above names
    # it, and the agent resolves it itself with the `refs-dir` subcommand anyway.
    if _switch_on(session_cfg, "refs-finder") and not _HOST_IS_CODEX:
        print(
            "guard: this project saves copies of the documentation it cites. Before "
            "answering a question that could rest on one — how a tool, API, format or "
            f"protocol behaves — dispatch {_agent_id('refs-finder')} with the user's "
            "question verbatim and wait for it; it names the saved references that bear "
            "on the question, or reports none. See the `refs-finder` section of "
            f"{_playbook_path()} the first time you dispatch it."
        )

    # The standing reuse policy is stated ONCE, here, rather than in every Stop
    # recommendation. Reuse is a session-long fact — the instance lives under the session
    # id — so the session's opening is where it belongs, and repeating it per turn would
    # pay for it on every turn. The per-turn text still carries the mechanic (resume this
    # name, or dispatch under it), because that is what changes with which agents were
    # picked; what it does not carry is the explanation.
    #
    # A mode changed mid-session leaves this line stale, which is exactly why
    # `cmd_settings` prints its own transition note: the two together are how the main
    # agent learns the policy and then learns it changed.
    reused = [k for k in AUDIT_AGENTS if _agent_mode(session_cfg, k) is AgentMode.REUSE]
    if reused:
        named = ", ".join(f"{_agent_id(k)} as `{_instance_name(k)}`" for k in reused)
        print(
            "guard: these guard agents run as ONE instance for this whole session, not a "
            f"fresh one per turn — {named}. Keep those instances; they can message each "
            "other and you by name. Every other guard agent, the router included, is "
            "fresh each time. The playbook says how to reach a reused instance."
        )
    _trace(project_dir, None, "session-start", "swept", exported_project_dir=exported)
    return 0


def _parse_settings_argv(argv: list[str]) -> tuple[list[str], str | None]:
    """Split a ``settings`` CLI argv into positionals and the ``--session <id>`` value."""
    positional: list[str] = []
    session: str | None = None
    i = 0
    while i < len(argv):
        tok = argv[i]
        if tok == "--session":
            if i + 1 < len(argv):
                session = argv[i + 1].strip() or None
                i += 2
                continue
            i += 1
            continue
        positional.append(tok)
        i += 1
    return positional, session


def _apply_session_scalar(project_dir: Path, session_id: str | None, key: str, value: Any) -> None:
    """Mirror a switch change into the live session's
    ``state/<sid>.json`` so it takes effect at once, not only for sessions started later.
    These are the only settings cached in session state (seeded from config at session
    start); the rest are read from the config file at use, so writing the file is enough
    for them. No-op without a session id."""
    if not session_id:
        return
    config = _load_config(project_dir)
    state = _read_state(project_dir, session_id, config)
    state[key] = value
    _write_state(project_dir, session_id, state)


def _config_show_lines(project_dir: Path, session_id: str | None) -> list[str]:
    """Render current guard settings for the ``guard:settings`` skill to display. Shows the
    guard.local.json defaults; for the switches it also shows the live session value when
    it differs from the default (the session may have been changed after)."""
    raw = _load_raw_config(project_dir)
    cfg = _load_config(project_dir)
    state = None
    if session_id and _state_file(project_dir, session_id).is_file():
        state = _read_state(project_dir, session_id, cfg)

    def switch_line(key: str) -> str:
        default = _agent_mode(cfg, key)
        live = _agent_mode(state, key) if state is not None else default
        suffix = " — one instance for the session" if live is AgentMode.REUSE else ""
        if live != default:
            return f"{key}: {live} (this session; default {default}){suffix}"
        return f"{key}: {default}{suffix}"

    refs_rel = raw.get("refs_dir") if isinstance(raw.get("refs_dir"), str) else ""
    # The mute is listed first and only when it is on: it overrides every line below it, so a
    # reader who sees the switches without it would read the wrong answer to "is guard
    # running". It is session state, so there is no default to show alongside.
    muted = ["audits: OFF for this session (/guard:toggle on to restore)"] if (
        state is not None and _audit_paused(state)) else []
    return [
        *muted,
        *(switch_line(k) for k in AUDIT_AGENTS),
        "router_model: " + (_router_model(cfg) or "(agents/router.md)"),
        "refs_dir: " + (refs_rel if refs_rel else "(default wiki/ref/)"),
    ]


def _live_agent_mode(project_dir: Path, session_id: str | None,
                     cfg: dict[str, Any], key: str) -> AgentMode:
    """The mode ``key`` is running under right now — session state when there is a
    session, the config file otherwise. Read BEFORE a write, so the change can be
    reported."""
    return _agent_mode(_read_state(project_dir, session_id, cfg) if session_id else cfg, key)


def _mode_transition_note(key: str, before: AgentMode, after: AgentMode) -> str:
    """The note a mode change owes the session, or "" when it owes none.

    A mode change is the one setting change that leaves something behind: an instance the
    main agent may still be addressing. Nothing in guard can see or stop that instance —
    this CLI has no channel to it — so the change has to be reported to the session that
    can, and this text is that report. It reaches the main agent because the skill relays
    what the CLI printed.
    """
    if before is AgentMode.REUSE and after is not AgentMode.REUSE:
        return (f"guard: {key} is no longer reused. Stop sending to "
                f"`{_instance_name(key)}` — shut it down if your session offers a way to "
                f"— and from the next turn dispatch a new instance each time.")
    if after is AgentMode.REUSE and before is not AgentMode.REUSE:
        return (f"guard: {key} now runs as one instance for the session, named "
                f"`{_instance_name(key)}`. Dispatch it under that name once, then "
                f"SendMessage it on later turns instead of dispatching again.")
    return ""


def _settings_unset(project_dir: Path, session_id: str | None,
                    positional: list[str]) -> int:
    """``settings unset <key>`` — delete one key from guard.local.json.

    Deleting an agent switch is a change to what guard does, not just to the file, so it
    goes through the same two steps a ``set`` does: the session's cached mode is reset to
    the default and any reuse transition is reported. Deleting a key guard does not
    honor touches neither.
    """
    if not positional:
        print("guard settings: usage: settings unset <key>", file=sys.stderr)
        return 0
    key = positional[0]
    raw = _load_raw_config(project_dir)
    # Case-sensitive on purpose: this removes a key by its literal name in the file, and
    # a lowercased guess would miss the misspelled or foreign-cased key that is exactly
    # what someone reaches for this verb to clear.
    if key not in raw:
        print(f"guard settings: no key {key!r} in .claude/guard.local.json — nothing to "
              f"remove. Keys present: " + (", ".join(raw) if raw else "(none)"))
        _trace(project_dir, session_id, "settings", "unset_absent", key=key)
        return 0

    cfg = _load_config(project_dir)
    transition = ""
    if key in AUDIT_AGENTS:
        before = _live_agent_mode(project_dir, session_id, cfg, key)
        after = AgentMode(DEFAULT_CONFIG[key])
        _apply_session_scalar(project_dir, session_id, key, after.value)
        transition = _mode_transition_note(key, before, after)
    del raw[key]

    if not _write_config(project_dir, raw):
        print("guard settings: failed to write .claude/guard.local.json", file=sys.stderr)
        return 0

    known = key in DEFAULT_CONFIG
    # `str()` first: an `AgentMode` default would otherwise print as `<AgentMode.OFF: 'off'>`.
    print(f"guard: removed {key!r} — "
          + (f"back to the default ({str(DEFAULT_CONFIG[key])!r})." if known
             else "guard does not honor that key, so nothing changes."))
    print()
    for line in _config_show_lines(project_dir, session_id):
        print(line)
    if transition:
        print()
        print(transition)
    _trace(project_dir, session_id, "settings", "unset", key=key, known=known)
    return 0


def cmd_settings() -> int:
    """View/change guard.local.json settings — the CLI behind the ``guard:settings`` skill.

        settings [show]                      — print the current settings
        settings set <key> <value>           — change one setting
        settings unset <key>                 — delete one key from the file

    Settable keys: the agent switches (the keys of ``AUDIT_AGENTS`` — each is the name
    of the agent it admits), ``router_model`` (the router agent's model, and nothing
    else's), and ``refs_dir``. The switches
    also apply to the live session's ``state/<sid>.json`` when a session id is available
    (``--session <id>``, which the forked skill passes as ``${CLAUDE_SESSION_ID}``, else
    the inherited ``CLAUDE_CODE_SESSION_ID``) so the change takes effect at once and
    persists as the new default; the rest are read from the config file at use.
    ``set`` preserves every other key in the file. ``unset`` is the one way to remove a
    key, and it exists because that preservation has no other exit: a key guard stopped
    honoring (``exempt_skills``, ``audit_gate``) is invisible to ``show`` and survives
    every ``set`` forever, and the file may only be written through this CLI, so without
    this verb the only way to clear one is the hand-edit the skill forbids. It deletes
    any key, live or dead, rather than only the dead ones — guard cannot know which keys
    a newer version owns, so pruning on its own judgment would silently discard a
    downgraded user's config. Project dir from ``_cli_project_dir`` — the git root, not the
    cwd, or a `set` run from a subdirectory would write a second config file the session
    never reads."""
    positional, session_arg = _parse_settings_argv(sys.argv[2:])
    op = positional[0].lower() if positional else "show"

    project_dir = _cli_project_dir()
    session_id = session_arg or (os.environ.get("CLAUDE_CODE_SESSION_ID", "").strip() or None)

    if op not in ("set", "unset"):
        for line in _config_show_lines(project_dir, session_id):
            print(line)
        _trace(project_dir, session_id, "settings", "show")
        return 0

    if not _cli_write_allowed():
        print("guard settings: refusing to change settings outside /guard:settings. "
              "Ask the user to run `/guard:settings` — only the user changes guard's "
              "own configuration.", file=sys.stderr)
        _trace(project_dir, session_id, "settings", "refused_no_skill_marker")
        return 0

    if op == "unset":
        return _settings_unset(project_dir, session_id, positional[1:])

    if len(positional) < 3:
        print("guard settings: usage: settings set <key> <value>", file=sys.stderr)
        return 0
    key = positional[1].lower()
    value = positional[2]

    raw = _load_raw_config(project_dir)
    cfg = _load_config(project_dir)
    transition = ""

    if key in AUDIT_AGENTS:
        v = _parse_mode(value)
        if v is None:
            print(f"guard settings: {key} must be one of "
                  f"{[m.value for m in AgentMode]} (got {value!r})", file=sys.stderr)
            return 0
        # Read the mode this replaces BEFORE writing, so the transition can be reported.
        # A mode change is the one setting change that leaves something behind: an
        # instance the main agent may still be addressing. Nothing in guard can see or
        # stop that instance — the settings CLI runs in a forked skill with no channel to
        # it — so the change has to be reported to the session that CAN, and this print
        # is that report. It reaches the main agent because the skill relays what the CLI
        # printed.
        before = _live_agent_mode(project_dir, session_id, cfg, key)
        raw[key] = v.value
        _apply_session_scalar(project_dir, session_id, key, v.value)
        transition = _mode_transition_note(key, before, v)
    elif key == "router_model":
        # "" is a legitimate value here, not an error: it hands the choice back to
        # `agents/router.md`, which is how a router model is normally set.
        raw["router_model"] = value.strip()
    elif key == "refs_dir":
        raw["refs_dir"] = value  # "" resets to the default; _refs_dir validates at use
    else:
        print(f"guard settings: unknown or unsettable key {key!r}. Settable: "
              + ", ".join(AUDIT_AGENTS)
              + ", router_model, refs_dir.",
              file=sys.stderr)
        return 0

    if not _write_config(project_dir, raw):
        print("guard settings: failed to write .claude/guard.local.json", file=sys.stderr)
        return 0

    for line in _config_show_lines(project_dir, session_id):
        print(line)
    if transition:
        print()
        print(transition)
    _trace(project_dir, session_id, "settings", "set", key=key)
    return 0


def cmd_refs_dir() -> int:
    """Print the resolved refs directory (absolute), applying `refs_dir` validation.

    The single query point for "where do cited-doc copies go": the claims auditor falls
    back to it when its dispatch omits `refs_dir`, and anything with the script
    path can use it instead of re-implementing _refs_dir's fallback rules.

    A CLI verb, so `_cli_project_dir`. On `_project_dir` it printed NOTHING to every caller
    it has — the Bash environment has no `CLAUDE_PROJECT_DIR` to find — which is not a
    fail-open, since the whole verb is the answer it was asked for.
    """
    project_dir = _cli_project_dir()
    print(_refs_dir(project_dir, _load_config(project_dir)))
    return 0


REFS_INDEX_NAME = "AGENTS.md"
# Files in the refs dir that are the index machinery itself, never indexed entries.
_REFS_INDEX_SKIP = {REFS_INDEX_NAME, "CLAUDE.md"}


def cmd_post_edit() -> int:
    """PostToolUse on the file-writing tools. Two jobs on the one payload.

    1. Record the source file, if that is what was written, against this turn — the
       list `comment-corrector` is pointed at when Stop recommends it. This is the event
       that actually sees the path, so nothing has to be reconstructed from a transcript
       later; Stop only reads back what accumulated here.
    2. Require a file saved inside the refs dir to be listed in the refs index
       (``AGENTS.md``). A saved reference nothing points at is a file the next reader
       never finds, so the index is the deliverable, not a courtesy. This fires *after*
       the write rather than blocking it: the natural order is save-then-index, and
       blocking the save would force an index entry for a file that does not exist yet.

    Job 2 blocks with ``decision: "block"`` so the reason returns to the model as work
    to finish; job 1 never emits anything. Silent in every other case — a write outside
    the refs dir, the index itself, or a file already listed.
    """
    project_dir = _project_dir()
    payload = _read_payload()
    if payload is None or project_dir is None:
        return 0

    config = _load_config(project_dir)
    tool_input = payload.get("tool_input")
    _record_edited_source(project_dir, payload, tool_input, config)
    if not _targets_refs_dir(project_dir, tool_input, config):
        return 0
    target = _tool_target_path(project_dir, tool_input)
    if target is None or target.name in _REFS_INDEX_SKIP:
        return 0

    reason = refs_index_gap(project_dir, target, config)
    if reason is None:
        _trace(project_dir, None, "post-edit", "refs_listed", file=target.name)
        return 0

    json.dump({"decision": "block", "reason": reason}, sys.stdout)
    _trace(project_dir, None, "post-edit", "refs_missing", file=target.name)
    return 0


def refs_index_gap(project_dir: Path, target: Path, config: dict[str, Any]) -> str | None:
    """The block reason when ``target`` is missing from the refs index, else None.

    Host-neutral so both adapters enforce one rule. Matching is by file name anywhere
    in the index text rather than by table structure: the index is prose a human
    maintains, and pinning the check to a column layout would fail the moment someone
    reformats it.
    """
    index = _refs_dir(project_dir, config) / REFS_INDEX_NAME
    try:
        if target.name in index.read_text(encoding="utf-8"):
            return None
    except OSError:
        pass  # No index yet: the first saved reference is what creates it.
    return (
        f"guard: `{target.name}` is saved but not listed in the reference index. "
        f"Add a row for it to `{_project_rel(project_dir, index)}` — file name, what "
        "it covers, and the source — so the next reader finds it without opening "
        "every file. Then continue."
    )


# Status-line colours. Dim for the state guard chose not to shout about, green for armed,
# yellow for muted — the one state the user set and can forget. Kept as constants because a
# status line that emits a stray escape sequence garbles the user's terminal row.
_ANSI_RESET = "\033[0m"
_ANSI_ARMED = "\033[32m"
_ANSI_MUTED = "\033[33m"
_ANSI_IDLE = "\033[2m"


def _audit_paused(state: dict[str, Any]) -> bool:
    """Is the automatic audit muted for this session? Only ever True from `/guard:toggle`."""
    return state.get("audit_paused") is True


def cmd_toggle() -> int:
    """UserPromptExpansion for `/guard:toggle [on|off]`. Mute or unmute this session.

    The hook does the work rather than telling the model to: `command_args` carries the
    argument (hooks docs, excerpt in the refs dir as `claude-code-statusline.md`), so no
    argument means flip, `on`/`off` set it outright, and the outcome does not depend on a
    model reading a procedure correctly.

    Session state only. It cannot touch guard.local.json, which is what makes this safe to
    reach for mid-conversation: whatever the project decided is still what the next session
    starts with. `on` means auditing on, so it CLEARS the pause — the user's vocabulary is
    about guard, not about the flag's name.
    """
    project_dir = _project_dir()
    payload = _read_payload()
    if payload is None or project_dir is None:
        return 0
    session_id = _session_id(payload)
    if session_id is None:
        _emit_expansion("guard: no usable session id, so there is no session to mute.")
        return 0

    arg = payload.get("command_args")
    arg = arg.strip().lower() if isinstance(arg, str) else ""
    config = _load_config(project_dir)
    state = _read_state(project_dir, session_id, config)

    if arg in ("", "flip", "toggle"):
        paused = not _audit_paused(state)
    elif arg in ("on", "resume", "enable"):
        paused = False
    elif arg in ("off", "pause", "disable", "mute"):
        paused = True
    else:
        _emit_expansion(
            f"guard: `{arg}` is not an argument for /guard:toggle — use `on`, `off`, or "
            "nothing to flip. Nothing changed; say so in one line."
        )
        return 0

    state["audit_paused"] = paused
    _write_state(project_dir, session_id, state)
    armed = [k for k in AUDIT_AGENTS if _switch_on(state, k)]

    if paused:
        msg = ("guard: audits are OFF for this session. Nothing is recommended when a turn "
               "ends, and answers are no longer written to a file. `/guard:toggle on` "
               "restores it and the project's own settings are untouched. A `/guard:*` "
               "command still works if you want one audit now.")
    elif armed:
        msg = ("guard: audits are ON for this session again — "
               + ", ".join(f"`{k}`" for k in armed) + ". Nothing else changed.")
    else:
        msg = ("guard: no longer muted, but every agent is `off` for this project, so nothing "
               "will run. `/guard:settings` is where you switch one on.")
    _emit_expansion(msg + " Relay this in one line and do nothing else.")
    _trace(project_dir, session_id, "toggle", "set", arg=arg or "flip", paused=paused)
    return 0


def cmd_status() -> int:
    """Status-line segment: is guard auditing this session? Reads stdin, prints one field.

    A plugin cannot install the MAIN status line — only `agent` and `subagentStatusLine` are
    honored in a plugin's settings.json — so this prints a segment the user composes into
    whatever status line they already run. The excerpt is saved in the refs dir as
    `claude-code-statusline.md`.

    Two documented constraints shape the body. It runs on every assistant message, debounced
    at 300ms, and a newer update cancels the one in flight: so it reads only the small
    config and state JSON files and does nothing else — no git, no transcript, no subprocess.
    And its stdout goes
    straight into the user's status bar: so every failure prints NOTHING rather than an
    error message, because a status line is the one place guard must never shout from.
    """
    try:
        payload = json.loads(sys.stdin.read() or "{}")
    except (json.JSONDecodeError, ValueError, OSError, UnicodeDecodeError):
        return 0
    if not isinstance(payload, dict):
        return 0

    # The status-line payload names the launch directory, which is where guard's state hangs
    # off. `CLAUDE_PROJECT_DIR` is the fallback so the same command works when a user wires
    # it into a script that does not forward the JSON.
    ws = payload.get("workspace")
    root = ws.get("project_dir") if isinstance(ws, dict) else None
    for cand in (root, payload.get("cwd"), os.environ.get("CLAUDE_PROJECT_DIR")):
        if isinstance(cand, str) and cand.strip():
            root = cand.strip()
            break
    else:
        return 0
    session_id = _session_id(payload)
    if not isinstance(root, str) or session_id is None:
        return 0

    try:
        project_dir = Path(root)
        state = _read_state(project_dir, session_id, _load_config(project_dir))
    except Exception:
        return 0

    armed = [k for k in AUDIT_AGENTS if _switch_on(state, k)]
    if _audit_paused(state):
        # Muted is the state worth a colour: the user chose it and can forget it.
        print(f"{_ANSI_MUTED}guard off{_ANSI_RESET}")
    elif armed:
        print(f"{_ANSI_ARMED}guard {len(armed)}{_ANSI_RESET}")
    else:
        # Nothing switched on for this project: not an error and not something the user did
        # this session, so it gets a dot rather than a word — "installed, idle" without
        # asking for attention on every redraw.
        print(f"{_ANSI_IDLE}guard ·{_ANSI_RESET}")
    return 0


SUBCOMMANDS = {
    "user-prompt": cmd_user_prompt,
    "post-edit": cmd_post_edit,
    "verify": cmd_verify,
    "settings": cmd_settings,
    "stop": cmd_stop,
    "session-start": cmd_session_start,
    "refs-dir": cmd_refs_dir,
    "transcript": cmd_transcript,
    "toggle": cmd_toggle,
    "status": cmd_status,
}


def main() -> int:
    if len(sys.argv) < 2:
        return 0
    handler = SUBCOMMANDS.get(sys.argv[1])
    if handler is None:
        return 0
    try:
        return handler()
    except Exception as e:  # never let guard's own failure surface as a hook error
        _trace(_project_dir(), None, sys.argv[1] if len(sys.argv) > 1 else "?", "exception", error=repr(e))
        return 0


if __name__ == "__main__":
    sys.exit(main())
