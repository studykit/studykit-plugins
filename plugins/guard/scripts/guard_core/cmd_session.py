"""``session-start`` (SessionStart) — the sweep, the exports, and the standing context.

Sweeps state files, ``trace.log``, and turns/ and extracts/ dirs older than retention;
exports ``GUARD_PROJECT_DIR`` and ``GUARD_REFS_DIR`` via ``$CLAUDE_ENV_FILE`` (append-once,
since this event also fires on every compaction); and states as session context the refs rule
always, the dispatch playbook's path when any agent is on, the fetch policy that sends the
session's documentation lookups to ``ext-docs-fetcher`` instead of to its own WebFetch when that
switch is on (not on Codex), and the standing reuse policy when any agent is in ``reuse``.
Each is said ONCE here rather than in every Stop, which is the whole reason this hook prints
anything.
"""

from __future__ import annotations

import os
import shlex
import time

from pathlib import Path

from .config import (
    AgentMode, ORPHAN_MAX_AGE_SECONDS, _HOST_IS_CODEX, _agent_mode, _load_config, _switch_on
)
from .paths import _project_dir, _refs_dir, _state_root, _trace, _trace_file
from .payload import _read_payload, _session_id
from .state import _audit_paused, _read_state
from .agents import AUDIT_AGENTS, _agent_id, _instance_name
from .dispatch import _playbook_path


def _session_muted(project_dir: Path, config: dict) -> bool:
    """Is the session this SessionStart opens muted? Claude only.

    A session starts muted (`state._read_state`), so at `startup` this is True and the line
    below has to say so instead of announcing audits nothing will run. It is not always
    True: SessionStart registers no matcher, so it also fires on `resume`, `clear`,
    `compact` and `fork`, where the session may already have been unmuted by
    `/guard:toggle` and the state file says so.

    Reading stdin here is safe only because the Claude entry point has not: `guard_hook.py`
    dispatches this verb without touching the payload. The Codex adapter HAS already
    consumed stdin by the time it calls this module, which is a second reason for the host
    test — the first being that Codex has no `/guard:toggle` and its own Stop path never
    reads `audit_paused`, so a Codex session is never muted.
    """
    if _HOST_IS_CODEX:
        return False
    payload = _read_payload()
    sid = _session_id(payload) if payload else None
    if sid is None:
        # No session to look up means no state to have been unmuted — the same answer a
        # fresh session gets, and the honest one when guard cannot tell.
        return True
    return _audit_paused(_read_state(project_dir, sid, config))


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
    if any(_switch_on(session_cfg, k) for k in AUDIT_AGENTS):
        # Which of the two lines goes out is the mute, not the switches. Saying "audits are
        # on" to a session that starts muted would be false in the one place a false line is
        # most expensive: nothing later in the session contradicts it, so the model spends
        # the session expecting a recommendation that never comes.
        if _session_muted(project_dir, session_cfg):
            print(
                "guard: agents are configured for this project, but audits are OFF for this "
                "session — guard starts muted, so nothing is recommended when a turn ends "
                "and no answer file is named. `/guard:toggle on` arms it for this session "
                "only; a `/guard:<agent>` command still runs one audit without arming "
                "anything. Do not mention this unless the user asks."
            )
        else:
            print(
                "guard: audits are on for this session. When a turn finishes, guard names the "
                f"agents to consider and points at {_playbook_path()}, which says how to "
                "dispatch each one and what to do with what it reports. Read only the sections "
                "you are named; do not read the file until then."
            )

    # The fetch policy, and the reason `ext-docs-fetcher` is announced here rather than named
    # per turn. Everything else guard says is about checking work already done; this is about
    # a call the session is about to make, so it has to arrive before the session reaches for
    # the tool — which means SessionStart. A `UserPromptSubmit` line would bill every turn in
    # the session for an agent that is off by default and wanted only on the questions that
    # touch documentation. Once is enough because SessionStart registers no matcher and so
    # fires on every source — `startup`, `resume`, `clear`, `compact`, `fork` — which means a
    # compaction that drops this line immediately restates it
    # (https://code.claude.com/docs/en/hooks, excerpt at
    # wiki/ref/claude-code-hooks-session-env.md).
    #
    # What this line does NOT have to do any more is forbid the fetch. `pre-fetch` denies
    # WebFetch and WebSearch in the main conversation while this switch is on, so the
    # prohibition is a rule the host applies and this text only says so, which is why the
    # sentence reads as a fact rather than an instruction. The half that stays an instruction
    # is the one no hook can reach: answering an external-behavior question from memory makes
    # no tool call, so nothing fires and nothing can be denied. That is the line's real job
    # now, and it is why shortening it to a pointer would lose something.
    #
    # Why redirect the fetch at all, when the main agent could do it perfectly well: a page
    # pulled into the main context is paid for on every turn after, a page read in passing is
    # a page nobody saves, and a session that skimmed a page cannot separate what the page
    # said from what it expected the page to say. The agent's definition argues all three.
    #
    # The agent LOOKS LOCALLY FIRST and most dispatches end there, which is why one line can
    # replace what used to be two agents — a read-only lookup that reported `none`, and a
    # fetcher the session then had to remember to dispatch. That handoff was where a session
    # gave up and answered from memory. What the merge has to preserve is the distinction the
    # lookup existed to make, and it is preserved in the REPORT: the agent says whether a path
    # was already saved or newly fetched, so the caller still knows which it got.
    #
    # There is a second entry point, at the far end of the turn: the router may pick
    # `ext-docs-fetcher` when a finished answer rested on a document nobody saved. That one is a
    # repair; this is the normal path.
    #
    # The refs directory is deliberately not repeated here: the line printed above names it,
    # and the agent resolves it itself with the `refs-dir` subcommand anyway.
    #
    # Not on Codex: it ships one named agent installed by `$guard:setup` and no fetcher among
    # them, and this module is its adapter's library — so without the host test the line would
    # forbid a tool and name no replacement.
    if _switch_on(session_cfg, "ext-docs-fetcher") and not _HOST_IS_CODEX:
        print(
            "guard: do not answer from memory a question about how an external tool, API, "
            "format or protocol behaves. This project saves copies of the documentation it "
            f"cites: dispatch {_agent_id('ext-docs-fetcher')} with the user's question verbatim "
            "and wait for it. It reports the local path of what is already saved, fetches and "
            "saves the primary source when nothing is, and says which of the two it did — or "
            "reports none. Read the files it names yourself. Your own WebFetch and WebSearch "
            "are blocked while this is on, so there is no faster route. See the "
            f"`ext-docs-fetcher` section of {_playbook_path()} the first time you dispatch it."
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
