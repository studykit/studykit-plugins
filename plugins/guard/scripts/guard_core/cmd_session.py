"""``session-start`` (SessionStart) — the sweep, the exports, and the standing context.

Sweeps state files, ``trace.log``, and turns/ and extracts/ dirs older than retention;
exports ``GUARD_PROJECT_DIR`` and ``GUARD_REFS_DIR`` via ``$CLAUDE_ENV_FILE`` (append-once,
since this event also fires on every compaction); and states as session context the refs rule
always, the dispatch playbook's path when any turn-end agent is on, the ``refs-finder``
announcement when that switch is on (not on Codex), and the standing reuse policy when any
agent is in ``reuse``. Each is said ONCE here rather than in every Stop, which is the whole
reason this hook prints anything.
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
from .agents import AUDIT_AGENTS, _agent_id, _instance_name
from .dispatch import _playbook_path


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
