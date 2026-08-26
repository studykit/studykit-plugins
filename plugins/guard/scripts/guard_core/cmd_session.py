"""``session-start`` (SessionStart) — the sweep, the exports, and the standing context.

Sweeps state files, ``trace.log``, and turns/ and extracts/ dirs older than retention;
exports ``GUARD_PROJECT_DIR`` and ``GUARD_REFS_DIR`` via ``$CLAUDE_ENV_FILE`` (append-once,
since this event also fires on every compaction); and states as session context the refs rule
always, the dispatch playbook's path when any agent is on, and the standing reuse policy when
any agent is in ``reuse``. Each is said ONCE here rather than in every Stop, which is the
whole reason this hook prints anything.

There is deliberately no line naming ``ext-docs-fetcher``. That agent has no switch to
announce and nothing here forbids the session's own fetching; it is selected the way any agent
is, from its description, and the refs rule below is what tells the session that a cited page
has to end up saved.
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
from .dispatch import CLI_REL, _playbook_path, _plugin_root


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


def _add_shell_command_to_path() -> bool:
    """Put guard's shell commands on the session's ``PATH``. True if written.

    Two of them share the directory and are reached the same way, by parties that never
    meet: ``guard`` is the user's, typed at a shell prompt, and ``guard-candidates`` is the
    router's, run from a subagent's Bash. Adding the directory serves both, which is why
    this is one export rather than two.

    ``CLAUDE_ENV_FILE`` is not a list of ``export`` lines — it is a shell script Claude Code
    SOURCES before each Bash command, so it can prepend a directory as readily as it can set
    a variable. That is what makes ``guard on`` work with nothing to install: no startup
    file is edited, and nothing is left behind when the session ends, because the file
    belongs to one session.

    A real executable on ``PATH``, not a shell function. A function exists only in the shell
    that sourced it, so anything one level down — a subprocess, a Makefile recipe, a script
    the agent writes — would not find ``guard``; an executable is inherited the way every
    other command is. It also behaves like a command in the ways people expect: ``command -v
    guard`` locates it, and ``guard`` inside ``$(...)`` works.

    Only guard's own ``bin`` is added, and only ever once (``_append_env_file`` matches on
    the directory). Prepending is not "reordering the user's PATH": it adds one directory
    holding one command. A user who already has a ``guard`` can set ``GUARD_TOGGLE_NAME``,
    which is the name guard's own messages then suggest — though note that variable renames
    only the SUGGESTION, not this file, so a genuine collision is theirs to resolve.

    Added unconditionally, for every project. Gating it on "guard is configured here" would
    be gating on nothing: a project with no ``guard.local.json`` loads the defaults and is an
    ordinary guard project whose switches are all ``off`` — so the condition would not
    separate the case it appears to, and the command would be missing exactly where a user
    might reach for it first.

    Best-effort and silent, like the exports: the CLI verb is reachable by path regardless,
    and a session without it is merely less convenient.
    """
    bin_dir = _plugin_root() / "shell" / "bin"
    if not (bin_dir / "guard").is_file():
        return False
    quoted = shlex.quote(str(bin_dir))
    return _append_env_file(f"export PATH={quoted}:$PATH", marker=f"export PATH={quoted}:")


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
    return _append_env_file(f"export {name}={shlex.quote(value)}")


def _append_env_file(text: str, marker: str | None = None) -> bool:
    """Append to ``$CLAUDE_ENV_FILE`` unless it already carries this. True if written.

    ``marker`` is the line that identifies a multi-line block already being present; for a
    single line the text is its own marker. SessionStart registers no matcher, so it fires
    on `startup`, `resume`, `clear`, `compact` and `fork` alike — a blind append added the
    same content once per compaction for the life of the session, which is what
    ``GUARD_REFS_DIR`` did before this check existed.
    """
    env_file = os.environ.get("CLAUDE_ENV_FILE", "").strip()
    if not env_file:
        return False
    needle = marker if marker is not None else text
    try:
        path = Path(env_file)
        if path.is_file() and needle in path.read_text(encoding="utf-8"):
            return False
        with path.open("a", encoding="utf-8") as fh:
            fh.write(text + "\n")
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

    # The CLI behind the shell toggle. `CLAUDE_PLUGIN_ROOT` is given to hook processes and
    # substituted into command bodies, but it is NOT in the Bash tool's environment, so a
    # shell wrapper has no way to find this script — and its path is not guessable: the
    # marketplace installs the plugin under a versioned cache directory. Exporting the
    # resolved path is what makes `guard on` from a prompt possible at all.
    #
    # The PATH itself is deliberately not touched. Prepending a directory to a user's PATH
    # from a session hook changes how every command in that shell resolves, for a feature
    # that needs one variable; the wrapper the user installs reads this instead.
    _export_to_bash_env("GUARD_TOGGLE_CLI", str(_plugin_root() / CLI_REL))
    _add_shell_command_to_path()

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
                "only. Do not mention this unless the user asks."
            )
        else:
            print(
                "guard: audits are on for this session. When a turn finishes, guard names the "
                f"agents to consider and points at {_playbook_path()}, which says how to "
                "dispatch each one and what to do with what it reports. Read only the sections "
                "you are named; do not read the file until then."
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
