"""Where guard's state lives, and how the project root is found.

There are two root resolvers and merging them breaks one of the two. Hook events use
``_project_dir`` — the env var alone, failing open — because a hook is handed
``CLAUDE_PROJECT_DIR`` and a hook that guessed would write state somewhere nobody looks. The
CLI verbs (``transcript``, ``settings``, ``refs-dir``) use ``_cli_project_dir``:
``GUARD_PROJECT_DIR``, which SessionStart exports into the Bash environment via
``$CLAUDE_ENV_FILE``, else the git root above the cwd. ``CLAUDE_PROJECT_DIR`` itself is never
in that environment, so a CLI verb refusing to guess would answer nothing at all.

State is project-local under ``${CLAUDE_PROJECT_DIR}/.claude/guard/`` (``.codex/guard/`` on
Codex):

- ``state/<sid>.json``   the session's own state — see ``state``
- ``turns/<sid>/…``      the turn's answer and the request beside it — see ``turnrec``
- ``extracts/<dir>/…``   what an agent pulled out of the transcript — see ``transcript``
- ``trace.log``          file-only debug trace, enabled by ``GUARD_TRACE``

It is retained across the end of a session so a resumed session (``claude --resume``) keeps
its switch flags, and expired only by the age-based sweep at SessionStart (see
``config.ORPHAN_MAX_AGE_SECONDS``).
"""

from __future__ import annotations

import json
import os

from pathlib import Path
from datetime import datetime, timezone
from typing import Any

from .config import CONFIG_REL, STATE_DIR_REL, TRACE_FILE_NAME, _trace_enabled


def _project_dir() -> Path | None:
    """Project root for a HOOK. None when the host did not say, which fails open.

    A hook process is given `CLAUDE_PROJECT_DIR` (guard's Codex adapter sets
    `GUARD_PROJECT_DIR` the same way), so an absent value means something is wrong with the
    installation rather than that guard should guess — and guessing here would write state
    under whatever directory the host happened to launch in. CLI verbs are the opposite case
    and use `_cli_project_dir`.

    `CLAUDE_PROJECT_DIR` wins, and the order is the whole point. The host sets it per hook
    process, so it always describes THIS session; `GUARD_PROJECT_DIR` is guard's own export
    for the Bash environment, which outlives the session that wrote it. With the other
    precedence, a `claude` started from a guard session's Bash — a nested run, or just
    `cd ../other-repo && claude` — inherits the first project's path and writes the second
    project's turn records into the first. That was observed, not theorized: a test session
    in /tmp wrote its turn record into this repository.
    """
    value = os.environ.get("CLAUDE_PROJECT_DIR") or os.environ.get("GUARD_PROJECT_DIR")
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


def _clear_handoff_file(project_dir: Path) -> Path:
    """Where a `/clear`ed session leaves its switches for the session replacing it.

    One file per project, not per session: it is written by exactly one event (`SessionEnd`
    with `reason: "clear"`) and consumed by the next `SessionStart` with `source: "clear"`,
    which then deletes it. A second concurrent session cannot be mistaken for the predecessor
    because the record NAMES the session that ended — recency never enters into it.

    It sits beside `state/` rather than inside it so the age sweep, which reaps that directory
    on a seven-day policy, cannot be confused by a file that is meant to live for milliseconds.
    Its own expiry is ``CLEAR_INHERIT_MAX_AGE_SECONDS``.
    """
    return _state_root(project_dir) / "clear-handoff.json"


def _knowledge_dirs(project_dir: Path, config: dict[str, Any] | None = None) -> list[Path]:
    """The directories holding this project's operational knowledge. Empty when unset.

    Read by `design-environment`, which audits a proposal against the system as actually
    deployed — topology, environments, runbooks. That material routinely lives OUTSIDE the
    repository (a personal or team knowledge base), which is why this is not
    ``_safe_project_subdir``: an absolute path and a ``~`` are the expected shapes here, and
    confining it to the project would exclude the case the key exists for.

    A LIST, because the knowledge is normally split rather than centralized — one directory
    per system, per team, or per source, and a design touching two systems needs both. Order
    is preserved and is the user's statement of precedence: the reading agent starts at the
    front.

    Nothing writes here and nothing derives a write path from it, so the containment rules
    that make ``refs_dir`` a self-neutering hazard do not apply. What is checked is only
    that each value resolves to a real directory; a typo then drops that entry rather than
    the whole setting, and it drops SILENTLY here — the ``settings`` CLI is where a bad path
    is reported, because this runs on a dispatch and an agent cannot act on a warning it was
    not built to read.
    """
    out: list[Path] = []
    for _, resolved in _knowledge_dir_entries(project_dir, config):
        if resolved is not None and resolved not in out:
            out.append(resolved)
    return out


def _knowledge_dir_entries(project_dir: Path, config: dict[str, Any] | None = None
                           ) -> list[tuple[str, Path | None]]:
    """Each configured knowledge-dir entry as written, paired with the directory it resolves
    to — ``None`` when it resolves to nothing that exists.

    Split out of ``_knowledge_dirs`` so the two audiences can differ while the normalization
    does not: the dispatch path drops a bad entry silently (above), and the ``settings`` CLI
    reports it. Duplicating the rules instead is how the two would come to disagree about
    what a ``~`` or a relative path means.
    """
    raw = (config or {}).get("knowledge_dir", [])
    # A bare string is accepted as a one-element list: it is what a user who has one
    # directory will write, and what every earlier version of this key was.
    if isinstance(raw, str):
        raw = [raw]
    if not isinstance(raw, list):
        return []
    out: list[tuple[str, Path | None]] = []
    for entry in raw:
        if not isinstance(entry, str) or not entry.strip():
            continue
        text = entry.strip()
        try:
            candidate = Path(text).expanduser()
            if not candidate.is_absolute():
                candidate = project_dir / candidate
            candidate = candidate.resolve()
        except (OSError, RuntimeError):
            out.append((text, None))
            continue
        out.append((text, candidate if candidate.is_dir() else None))
    return out


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
