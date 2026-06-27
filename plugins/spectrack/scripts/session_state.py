#!/usr/bin/env python3
"""File-backed session state for workflow hooks.

Tracks one per-(project, host, session) JSON file under
``.spectrack-cache/hook-state/``. The file contains the normalized shell
environment, one-shot announcement flags, and issue-reference dedupe state for
that session.

Helpers stay narrow: every function takes ``project``/``session_id`` plus the
minimum extras it needs and is silent on filesystem errors so hook execution
never breaks on disk hiccups. State mutations take an exclusive file lock so
parallel hook processes do not overwrite each other's parent-session updates.
"""

from __future__ import annotations

from collections.abc import Callable, Mapping
import json
import re
import shlex
import sys
from pathlib import Path
from typing import Any, TextIO

try:
    import fcntl
except ImportError:  # pragma: no cover - Windows fallback.
    fcntl = None  # type: ignore[assignment]

_SCRIPTS_DIR = str(Path(__file__).resolve().parent)
if _SCRIPTS_DIR not in sys.path:
    sys.path.insert(0, _SCRIPTS_DIR)

from issue.cache import CACHE_ROOT_NAME  # noqa: E402
from issue.keys import normalize_issue_number  # noqa: E402
from issue.jira.refs import normalize_jira_issue_key  # noqa: E402

HOOK_STATE_DIR_NAME = "hook-state"
SESSION_STATE_VERSION = 1
SESSION_ISSUE_KINDS = {"announced"}

_SAFE_TOKEN_RE = re.compile(r"[^A-Za-z0-9_.-]+")
_MAX_SESSION_SLUG_LEN = 120


def workflow_hook_state_dir(project: Path) -> Path:
    cache_root = project.expanduser().resolve(strict=False) / CACHE_ROOT_NAME
    return cache_root / HOOK_STATE_DIR_NAME


def session_state_path(project: Path, runtime: str, session_id: str) -> Path | None:
    safe_session = _safe_token(session_id)
    if not safe_session:
        return None
    safe_runtime = _safe_token(runtime) or "unknown"
    return workflow_hook_state_dir(project) / f"workflow-session-{safe_runtime}-{safe_session}.json"


def issue_state_path(project: Path, session_id: str, kind: str) -> Path | None:
    """Return the legacy split issue-state path for migration only."""

    return _legacy_issue_state_path(project, session_id, kind)


def session_policy_state_path(project: Path, runtime: str, session_id: str) -> Path | None:
    """Return the legacy split policy-state path for migration only."""

    return _legacy_session_policy_state_path(project, runtime, session_id)


def session_env_state_path(project: Path, runtime: str, session_id: str) -> Path | None:
    """Return the unified session-state path that stores environment values."""

    return session_state_path(project, runtime, session_id)


def legacy_session_env_state_path(project: Path, runtime: str, session_id: str) -> Path | None:
    """Return the legacy split shell-export path for migration only."""

    return _legacy_session_env_state_path(project, runtime, session_id)


def commit_prefix_state_path(project: Path, session_id: str) -> Path | None:
    """Return the legacy split commit-prefix path for migration only."""

    return _legacy_commit_prefix_state_path(project, session_id)


def _legacy_issue_state_path(project: Path, session_id: str, kind: str) -> Path | None:
    safe_session = _safe_token(session_id)
    if not safe_session:
        return None
    return workflow_hook_state_dir(project) / f"workflow-{kind}-issues-{safe_session}.txt"


def _legacy_session_policy_state_path(project: Path, runtime: str, session_id: str) -> Path | None:
    safe_session = _safe_token(session_id)
    if not safe_session:
        return None
    safe_runtime = _safe_token(runtime) or "unknown"
    return workflow_hook_state_dir(project) / (
        f"workflow-session-policy-{safe_runtime}-{safe_session}.txt"
    )


def _legacy_session_env_state_path(project: Path, runtime: str, session_id: str) -> Path | None:
    safe_session = _safe_token(session_id)
    if not safe_session:
        return None
    safe_runtime = _safe_token(runtime) or "unknown"
    return workflow_hook_state_dir(project) / f"workflow-env-{safe_runtime}-{safe_session}.sh"


def _legacy_commit_prefix_state_path(project: Path, session_id: str) -> Path | None:
    safe_session = _safe_token(session_id)
    if not safe_session:
        return None
    return workflow_hook_state_dir(project) / f"workflow-commit-prefix-{safe_session}.txt"


def session_policy_was_announced(project: Path, runtime: str, session_id: str) -> bool:
    state = _read_session_state(project, runtime, session_id)
    if _flag(state, "session_policy"):
        return True
    legacy_path = _legacy_session_policy_state_path(project, runtime, session_id)
    if legacy_path is not None and legacy_path.is_file():
        record_session_policy_announced(project, runtime, session_id)
        return True
    return False


def record_session_policy_announced(project: Path, runtime: str, session_id: str) -> None:
    if _set_flag(project, runtime, session_id, "session_policy", True):
        _unlink(_legacy_session_policy_state_path(project, runtime, session_id))


def commit_prefix_was_announced(project: Path, session_id: str, runtime: str = "workflow") -> bool:
    state = _read_session_state(project, runtime, session_id)
    if _flag(state, "commit_prefix"):
        return True
    legacy_path = _legacy_commit_prefix_state_path(project, session_id)
    if legacy_path is not None and legacy_path.is_file():
        record_commit_prefix_announced(project, session_id, runtime=runtime)
        return True
    return False


def record_commit_prefix_announced(project: Path, session_id: str, runtime: str = "workflow") -> None:
    if _set_flag(project, runtime, session_id, "commit_prefix", True):
        _unlink(_legacy_commit_prefix_state_path(project, session_id))


def read_session_issues(
    project: Path,
    session_id: str,
    kind: str,
    runtime: str = "workflow",
) -> set[str]:
    if kind not in SESSION_ISSUE_KINDS:
        return set()
    state = _read_session_state(project, runtime, session_id)
    issues = _issue_set(state, kind)
    legacy_issues = _read_legacy_session_issues(project, session_id, kind)
    if legacy_issues:
        issues.update(legacy_issues)
        _write_session_issues(project, runtime, session_id, kind, issues)
        _unlink(_legacy_issue_state_path(project, session_id, kind))
    return issues


def record_session_issues(
    project: Path,
    session_id: str,
    issues: list[str],
    kind: str,
    runtime: str = "workflow",
) -> None:
    if kind not in SESSION_ISSUE_KINDS or not issues:
        return

    def mutator(state: dict[str, Any]) -> None:
        existing = _issue_set(state, kind)
        existing.update(_read_legacy_session_issues(project, session_id, kind))
        for issue in issues:
            try:
                existing.add(_normalize_issue_token(issue))
            except Exception:
                continue
        _set_state_issues(state, kind, existing)

    if _mutate_session_state(project, runtime, session_id, mutator):
        _unlink(_legacy_issue_state_path(project, session_id, kind))


def remove_session_issues(
    project: Path,
    session_id: str,
    issues: list[str],
    kind: str,
    runtime: str = "workflow",
) -> None:
    if kind not in SESSION_ISSUE_KINDS:
        return
    remove: set[str] = set()
    for issue in issues:
        try:
            remove.add(_normalize_issue_token(issue))
        except Exception:
            continue
    if not remove:
        return

    def mutator(state: dict[str, Any]) -> None:
        remaining = _issue_set(state, kind)
        remaining.update(_read_legacy_session_issues(project, session_id, kind))
        remaining -= remove
        _set_state_issues(state, kind, remaining)

    if _mutate_session_state(project, runtime, session_id, mutator):
        _unlink(_legacy_issue_state_path(project, session_id, kind))


def read_session_env_exports(project: Path, runtime: str, session_id: str) -> dict[str, str]:
    state = _read_session_state(project, runtime, session_id)
    env = _env_values(state)
    if env:
        return env
    legacy_env = _read_legacy_env_exports(project, runtime, session_id)
    if legacy_env:
        _record_migrated_legacy_env_exports(project, runtime, session_id, legacy_env)
        return legacy_env
    return {}


def record_session_env_exports(
    project: Path,
    runtime: str,
    session_id: str,
    values: Mapping[str, str],
    parent_session_id: str = "",
) -> bool:
    def mutator(state: dict[str, Any]) -> None:
        state["env"] = {str(key): str(value) for key, value in values.items() if str(key)}
        if parent_session_id:
            state["parent_session_id"] = parent_session_id
        else:
            state.pop("parent_session_id", None)

    if not _mutate_session_state(project, runtime, session_id, mutator):
        return False
    _unlink(_legacy_session_env_state_path(project, runtime, session_id))
    return True


def read_authoring_file_reads(
    project: Path,
    runtime: str,
    session_id: str,
) -> list[dict[str, str]]:
    return _authoring_file_reads(_read_session_state(project, runtime, session_id))


def record_authoring_file_read(
    project: Path,
    runtime: str,
    session_id: str,
    *,
    path: Path,
    relative_path: str,
) -> bool:
    normalized_relative = str(relative_path).strip().lstrip("/")
    if not normalized_relative:
        return False
    normalized_path = str(path.expanduser().resolve())

    def mutator(state: dict[str, Any]) -> None:
        authoring = _authoring_section(state)
        reads = {
            item["path"]: item
            for item in _authoring_file_reads(state)
            if item.get("path")
        }
        reads[normalized_path] = {
            "path": normalized_path,
            "relative_path": normalized_relative,
        }
        authoring["read_files"] = sorted(
            reads.values(),
            key=lambda item: (item["relative_path"], item["path"]),
        )

    return _mutate_session_state(project, runtime, session_id, mutator)


def read_subagent_starts(
    project: Path,
    runtime: str,
    session_id: str,
) -> list[dict[str, str]]:
    return _subagent_starts(_read_session_state(project, runtime, session_id))


def record_subagent_start(
    project: Path,
    runtime: str,
    session_id: str,
    *,
    agent_id: str | None,
    agent_type: str | None,
) -> bool:
    normalized_agent_id = str(agent_id or "").strip()
    normalized_agent_type = str(agent_type or "").strip()
    if not normalized_agent_id or not normalized_agent_type:
        return False

    def mutator(state: dict[str, Any]) -> None:
        subagents = _subagents_section(state)
        starts = {
            item["agent_id"]: item
            for item in _subagent_starts(state)
            if item.get("agent_id")
        }
        if normalized_agent_id not in starts:
            starts[normalized_agent_id] = {
                "agent_id": normalized_agent_id,
                "agent_type": normalized_agent_type,
            }
        else:
            starts[normalized_agent_id]["agent_type"] = normalized_agent_type
        subagents["started"] = list(starts.values())

    return _mutate_session_state(project, runtime, session_id, mutator)


def _read_session_state(project: Path, runtime: str, session_id: str) -> dict[str, Any]:
    path = session_state_path(project, runtime, session_id)
    if path is None or not path.is_file():
        return _empty_state(runtime, session_id)
    try:
        with path.open("r", encoding="utf-8") as handle:
            _lock(handle, exclusive=False)
            try:
                return _state_from_text(handle.read(), runtime=runtime, session_id=session_id)
            finally:
                _unlock(handle)
    except OSError:
        return _empty_state(runtime, session_id)


def _mutate_session_state(
    project: Path,
    runtime: str,
    session_id: str,
    mutator: Callable[[dict[str, Any]], None],
) -> bool:
    path = session_state_path(project, runtime, session_id)
    if path is None:
        return False
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a+", encoding="utf-8") as handle:
            _lock(handle, exclusive=True)
            try:
                handle.seek(0)
                state = _state_from_text(handle.read(), runtime=runtime, session_id=session_id)
                mutator(state)
                handle.seek(0)
                handle.truncate()
                json.dump(state, handle, indent=2, sort_keys=True)
                handle.write("\n")
                handle.flush()
            finally:
                _unlock(handle)
        return True
    except OSError:
        return False


def _write_session_issues(
    project: Path,
    runtime: str,
    session_id: str,
    kind: str,
    issues: set[str],
) -> None:
    def mutator(state: dict[str, Any]) -> None:
        _set_state_issues(state, kind, issues)

    _mutate_session_state(project, runtime, session_id, mutator)


def _set_flag(project: Path, runtime: str, session_id: str, flag: str, value: bool) -> bool:
    def mutator(state: dict[str, Any]) -> None:
        flags = state.get("flags")
        if not isinstance(flags, dict):
            flags = {}
            state["flags"] = flags
        flags[flag] = bool(value)

    return _mutate_session_state(project, runtime, session_id, mutator)


def _empty_state(runtime: str, session_id: str) -> dict[str, Any]:
    return {
        "version": SESSION_STATE_VERSION,
        "host": _safe_token(runtime) or "unknown",
        "session_id": session_id,
        "env": {},
        "flags": {},
        "issues": {},
        "authoring": {},
        "subagents": {},
    }


def _state_from_text(text: str, *, runtime: str, session_id: str) -> dict[str, Any]:
    if not text.strip():
        return _empty_state(runtime, session_id)
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        return _empty_state(runtime, session_id)
    if not isinstance(parsed, dict):
        return _empty_state(runtime, session_id)
    return _normalize_state(parsed, runtime=runtime, session_id=session_id)


def _normalize_state(state: dict[str, Any], *, runtime: str, session_id: str) -> dict[str, Any]:
    normalized = dict(state)
    normalized["version"] = SESSION_STATE_VERSION
    normalized["host"] = _safe_token(runtime) or "unknown"
    normalized["session_id"] = session_id
    if not isinstance(normalized.get("env"), dict):
        normalized["env"] = {}
    if not isinstance(normalized.get("flags"), dict):
        normalized["flags"] = {}
    if not isinstance(normalized.get("issues"), dict):
        normalized["issues"] = {}
    if not isinstance(normalized.get("authoring"), dict):
        normalized["authoring"] = {}
    if not isinstance(normalized.get("subagents"), dict):
        normalized["subagents"] = {}
    return normalized


def _flag(state: Mapping[str, Any], name: str) -> bool:
    flags = state.get("flags")
    return isinstance(flags, Mapping) and flags.get(name) is True


def _env_values(state: Mapping[str, Any]) -> dict[str, str]:
    values = state.get("env")
    if not isinstance(values, Mapping):
        return {}
    return {
        str(key): str(value)
        for key, value in values.items()
        if str(key) and isinstance(value, str)
    }


def _issue_set(state: Mapping[str, Any], kind: str) -> set[str]:
    issues = state.get("issues")
    if not isinstance(issues, Mapping):
        return set()
    values = issues.get(kind)
    if not isinstance(values, list):
        return set()
    result: set[str] = set()
    for value in values:
        if not isinstance(value, str):
            continue
        try:
            result.add(_normalize_issue_token(value))
        except Exception:
            continue
    return result


def _set_state_issues(state: dict[str, Any], kind: str, values: set[str]) -> None:
    issues = state.get("issues")
    if not isinstance(issues, dict):
        issues = {}
        state["issues"] = issues
    ordered = _sort_issue_tokens(values)
    if ordered:
        issues[kind] = ordered
        return
    issues.pop(kind, None)


def _authoring_section(state: dict[str, Any]) -> dict[str, Any]:
    authoring = state.get("authoring")
    if not isinstance(authoring, dict):
        authoring = {}
        state["authoring"] = authoring
    return authoring


def _authoring_file_reads(state: Mapping[str, Any]) -> list[dict[str, str]]:
    authoring = state.get("authoring")
    if not isinstance(authoring, Mapping):
        return []
    values = authoring.get("read_files")
    if not isinstance(values, list):
        return []

    reads: dict[str, dict[str, str]] = {}
    for value in values:
        if not isinstance(value, Mapping):
            continue
        path = value.get("path")
        relative_path = value.get("relative_path")
        if not isinstance(path, str) or not isinstance(relative_path, str):
            continue
        path = path.strip()
        relative_path = relative_path.strip().lstrip("/")
        if not path or not relative_path:
            continue
        reads[path] = {"path": path, "relative_path": relative_path}
    return sorted(reads.values(), key=lambda item: (item["relative_path"], item["path"]))


def _subagents_section(state: dict[str, Any]) -> dict[str, Any]:
    subagents = state.get("subagents")
    if not isinstance(subagents, dict):
        subagents = {}
        state["subagents"] = subagents
    return subagents


def _subagent_starts(state: Mapping[str, Any]) -> list[dict[str, str]]:
    subagents = state.get("subagents")
    if not isinstance(subagents, Mapping):
        return []
    values = subagents.get("started")
    if not isinstance(values, list):
        return []

    starts: dict[str, dict[str, str]] = {}
    for value in values:
        if not isinstance(value, Mapping):
            continue
        agent_id = value.get("agent_id")
        agent_type = value.get("agent_type")
        if not isinstance(agent_id, str) or not isinstance(agent_type, str):
            continue
        agent_id = agent_id.strip()
        agent_type = agent_type.strip()
        if not agent_id or not agent_type:
            continue
        starts[agent_id] = {"agent_id": agent_id, "agent_type": agent_type}
    return list(starts.values())


def _read_legacy_session_issues(project: Path, session_id: str, kind: str) -> set[str]:
    path = _legacy_issue_state_path(project, session_id, kind)
    if path is None or not path.is_file():
        return set()
    try:
        return {
            _normalize_issue_token(line)
            for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip()
        }
    except Exception:
        return set()


def _read_legacy_env_exports(project: Path, runtime: str, session_id: str) -> dict[str, str]:
    path = _legacy_session_env_state_path(project, runtime, session_id)
    if path is None or not path.is_file():
        return {}
    try:
        return _parse_shell_exports(path.read_text(encoding="utf-8"))
    except OSError:
        return {}


def _record_migrated_legacy_env_exports(
    project: Path,
    runtime: str,
    session_id: str,
    values: Mapping[str, str],
) -> None:
    canonical_session_id = values.get("SPECTRACK_SESSION_ID") or session_id
    record_session_env_exports(
        project,
        runtime,
        session_id,
        values,
        parent_session_id=canonical_session_id if canonical_session_id != session_id else "",
    )
    _unlink(_legacy_session_env_state_path(project, runtime, session_id))


def _parse_shell_exports(content: str) -> dict[str, str]:
    values: dict[str, str] = {}
    for line in content.splitlines():
        try:
            parts = shlex.split(line, posix=True)
        except ValueError:
            continue
        if len(parts) != 2 or parts[0] != "export" or "=" not in parts[1]:
            continue
        key, value = parts[1].split("=", 1)
        if key:
            values[key] = value
    return values


def _lock(handle: TextIO, *, exclusive: bool) -> None:
    if fcntl is None:
        return
    operation = fcntl.LOCK_EX if exclusive else fcntl.LOCK_SH
    fcntl.flock(handle.fileno(), operation)


def _unlock(handle: TextIO) -> None:
    if fcntl is None:
        return
    fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


def _unlink(path: Path | None) -> None:
    if path is None:
        return
    try:
        path.unlink(missing_ok=True)
    except OSError:
        return


def _safe_token(value: str) -> str:
    if not value:
        return ""
    sanitized = _SAFE_TOKEN_RE.sub("_", value).strip("._-")
    return sanitized[:_MAX_SESSION_SLUG_LEN]


def _normalize_issue_token(value: str) -> str:
    try:
        return normalize_issue_number(value)
    except Exception:
        return normalize_jira_issue_key(value)


def _sort_issue_tokens(values: set[str]) -> list[str]:
    def key(value: str) -> tuple[int, str, int]:
        if value.isdigit():
            return (0, "", int(value))
        return (1, value, 0)

    return sorted(values, key=key)
