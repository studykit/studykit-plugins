"""Explicit file-audit checkpoints over the session's accumulated dirty queue."""

from __future__ import annotations

import hashlib
import json
import os
import sys

from pathlib import Path
from typing import Any

from .config import (FileReviewRule, _file_review_rule, _file_review_rules,
                     _load_config, _file_excluded)
from .herdr import report_pending
from .paths import _cli_project_dir, _project_rel, _doc_scope, _state_root
from .agents import _edited_bucket
from .state import _edit_source, _edited_files, _read_state, _write_state


_BUCKETS = ("edited_files", "edited_agent_docs", "edited_docs")
_CODEX_AGENTS = {
    "guard:doc-auditor": "guard_doc_auditor",
    "guard:agents-md-auditor": "guard_agents_md_auditor",
    "guard:ext-docs-auditor": "guard_ext_docs_auditor",
}


def _content_hash(path: str) -> str | None:
    try:
        digest = hashlib.sha256()
        with Path(path).open("rb") as stream:
            for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                digest.update(chunk)
        return digest.hexdigest()
    except OSError:
        return None


def _session_arg() -> str:
    for index, value in enumerate(sys.argv[2:], start=2):
        if value == "--session" and index + 1 < len(sys.argv):
            return sys.argv[index + 1]
    return os.environ.get("CLAUDE_CODE_SESSION_ID") or os.environ.get("CODEX_THREAD_ID") or ""


def _host_arg() -> str:
    for index, value in enumerate(sys.argv[2:], start=2):
        if value == "--host" and index + 1 < len(sys.argv):
            return sys.argv[index + 1].lower()
    return "codex" if os.environ.get("CODEX_THREAD_ID") else "claude"


def _paths_arg(args: list[str]) -> set[str] | None:
    """Parse an optional JSON path list without making paths CLI option tokens."""
    if "--paths-json" not in args:
        return None
    index = args.index("--paths-json")
    if index + 1 >= len(args):
        raise ValueError("`--paths-json` needs a JSON array of paths")
    try:
        value = json.loads(args[index + 1])
    except (json.JSONDecodeError, TypeError, ValueError) as error:
        raise ValueError("`--paths-json` must be valid JSON") from error
    if not isinstance(value, list) or not all(
            isinstance(path, str) and path for path in value):
        raise ValueError("`--paths-json` must be a JSON array of non-empty paths")
    return set(value)


def _snapshot(state: dict[str, Any]) -> dict[str, dict[str, str]]:
    prompt_id = str(state.get("edited_prompt_id") or "checkpoint")
    result: dict[str, dict[str, str]] = {}
    for bucket in _BUCKETS:
        for path in _edited_files(state, prompt_id, bucket):
            digest = _content_hash(path)
            if digest is not None:
                result[path] = {"bucket": bucket, "sha256": digest}
    return result


def _prune_missing(state: dict[str, Any]) -> None:
    """Drop paths that disappeared before a checkpoint could snapshot them."""
    retained: set[str] = set()
    for bucket in _BUCKETS:
        current = state.get(bucket)
        if not isinstance(current, list):
            continue
        state[bucket] = [path for path in current
                         if isinstance(path, str) and Path(path).is_file()]
        retained.update(state[bucket])
    provenance = state.get("edited_provenance")
    if isinstance(provenance, dict):
        state["edited_provenance"] = {
            path: value for path, value in provenance.items() if path in retained
        }


def _retain_paths(state: dict[str, Any], retained: set[str]) -> None:
    """Remove legacy queue entries that current settings no longer select."""
    for bucket in _BUCKETS:
        current = state.get(bucket)
        if isinstance(current, list):
            state[bucket] = [path for path in current if path in retained]
    provenance = state.get("edited_provenance")
    if isinstance(provenance, dict):
        state["edited_provenance"] = {
            path: value for path, value in provenance.items() if path in retained
        }


def review_rule(project_dir: Path, target: Path, config: dict[str, Any]) -> FileReviewRule | None:
    """Apply the same path policy when recording and dispatching a file."""
    project = project_dir.resolve()
    target = target.resolve()
    if (project not in target.parents or _state_root(project_dir).resolve() in target.parents
            or not target.is_file()):
        return None
    relative = _project_rel(project_dir, target)
    if _file_excluded(relative, config.get("files_exclude", [])):
        return None
    if _edited_bucket(target, _doc_scope(project_dir, config)) is None:
        return None
    return _file_review_rule(relative, _file_review_rules(config))


def _plan(project_dir: Path, state: dict[str, Any], host: str,
          snapshot: dict[str, dict[str, str]]) -> list[dict[str, Any]]:
    config = _load_config(project_dir)
    groups: dict[tuple[str, str, bool], list[str]] = {}
    for path in snapshot:
        rule = review_rule(project_dir, Path(path), config)
        if rule is None:
            continue
        kind, name = rule.kind, rule.name
        if (kind, name) == ("skill", "guard:audit-docs"):
            kind, name = "agent", "guard:doc-auditor"
        if host == "codex" and kind == "agent":
            name = _CODEX_AGENTS.get(name, name)
        conditional = _edit_source(state, path) != "native"
        groups.setdefault((kind, name, conditional), []).append(path)
    return [
        {"kind": kind, "name": name, "conditional": conditional, "paths": paths}
        for (kind, name, conditional), paths in groups.items()
    ]


def reconcile_queue(project_dir: Path, state: dict[str, Any], host: str
                    ) -> tuple[dict[str, dict[str, str]], list[dict[str, Any]]]:
    """Keep only paths selected by current settings and return their dispatch plan."""
    _prune_missing(state)
    queued = _snapshot(state)
    groups = _plan(project_dir, state, host, queued)
    selected = {path for group in groups for path in group["paths"]}
    _retain_paths(state, selected)
    return ({path: item for path, item in queued.items() if path in selected}, groups)


def _show(project_dir: Path, session_id: str, host: str,
          selected: set[str] | None = None) -> int:
    config = _load_config(project_dir)
    state = _read_state(project_dir, session_id, config)
    snapshot, groups = reconcile_queue(project_dir, state, host)
    if selected is not None:
        snapshot = {path: item for path, item in snapshot.items() if path in selected}
        groups = [
            {**group, "paths": [path for path in group["paths"] if path in selected]}
            for group in groups
        ]
        groups = [group for group in groups if group["paths"]]
    truncated = state.get("edited_truncated", {}) if selected is None else {}
    payload = {"files": snapshot, "groups": groups,
               "truncated": truncated}
    token = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
    payload["token"] = token
    checkpoints = state.get("file_checkpoints")
    if not isinstance(checkpoints, dict):
        checkpoints = {}
    checkpoints[token] = {
        "files": snapshot,
        "groups": groups,
        "truncated": dict(truncated) if isinstance(truncated, dict) else {},
    }
    # Display refreshes also call `show`; keep several live tokens so a panel refresh cannot
    # invalidate an audit already in flight, but bound stale snapshot growth.
    state["file_checkpoints"] = dict(list(checkpoints.items())[-8:])
    _write_state(project_dir, session_id, state)
    report_pending(state)
    print(json.dumps(payload, ensure_ascii=False))
    return 0


def _show_token(project_dir: Path, session_id: str, token: str) -> int:
    """Read an immutable checkpoint prepared by the Herdr selection UI."""
    config = _load_config(project_dir)
    state = _read_state(project_dir, session_id, config)
    checkpoints = state.get("file_checkpoints")
    checkpoint = checkpoints.get(token) if isinstance(checkpoints, dict) else None
    if not isinstance(checkpoint, dict):
        print("guard: checkpoint token is stale; request a new audit.", file=sys.stderr)
        return 1
    files = checkpoint.get("files")
    groups = checkpoint.get("groups")
    truncated = checkpoint.get("truncated")
    if not isinstance(files, dict) or not isinstance(groups, list):
        print("guard: checkpoint token cannot be resumed; request a new audit.",
              file=sys.stderr)
        return 1
    payload = {
        "files": files,
        "groups": groups,
        "truncated": truncated if isinstance(truncated, dict) else {},
        "token": token,
    }
    print(json.dumps(payload, ensure_ascii=False))
    return 0


def _complete(project_dir: Path, session_id: str, token: str) -> int:
    config = _load_config(project_dir)
    state = _read_state(project_dir, session_id, config)
    checkpoints = state.get("file_checkpoints")
    if not isinstance(checkpoints, dict) or token not in checkpoints:
        print("guard: checkpoint token is stale; pending files were left unchanged.",
              file=sys.stderr)
        return 1
    checkpoint = checkpoints.get(token)
    if not isinstance(checkpoint, dict):
        return 1
    snapshot = checkpoint.get("files")
    if not isinstance(snapshot, dict):
        return 1
    cleared: set[str] = set()
    for path, item in snapshot.items():
        if not isinstance(path, str) or not isinstance(item, dict):
            continue
        before = item.get("sha256")
        now = _content_hash(path)
        if now is None or now == before:
            cleared.add(path)
    for bucket in _BUCKETS:
        current = state.get(bucket)
        if isinstance(current, list):
            state[bucket] = [path for path in current if path not in cleared]
    provenance = state.get("edited_provenance")
    if isinstance(provenance, dict):
        state["edited_provenance"] = {
            path: value for path, value in provenance.items() if path not in cleared
        }
    before_truncated = checkpoint.get("truncated")
    current_truncated = state.get("edited_truncated")
    if isinstance(before_truncated, dict) and isinstance(current_truncated, dict):
        remaining_truncated: dict[str, int] = {}
        for bucket, count in current_truncated.items():
            before = before_truncated.get(bucket, 0)
            if not isinstance(count, int) or not isinstance(before, int):
                continue
            if count - before > 0:
                remaining_truncated[bucket] = count - before
        state["edited_truncated"] = remaining_truncated
    state["file_checkpoints"] = {
        key: value for key, value in checkpoints.items() if key != token
    }
    _write_state(project_dir, session_id, state)
    report_pending(state)
    print(json.dumps({"cleared": len(cleared),
                      "remaining": len(_snapshot(state))}, ensure_ascii=False))
    return 0


def _clear(project_dir: Path, session_id: str, selected: set[str] | None = None) -> int:
    """Discard all or selected queue paths and invalidate in-flight checkpoints."""
    config = _load_config(project_dir)
    state = _read_state(project_dir, session_id, config)
    queued = {
        path
        for bucket in _BUCKETS
        for path in state.get(bucket, [])
        if isinstance(path, str) and path
    }
    cleared = queued if selected is None else queued & selected
    if selected is not None and not cleared:
        print(json.dumps({"cleared": 0, "remaining": len(queued)}, ensure_ascii=False))
        return 0
    for bucket in _BUCKETS:
        current = state.get(bucket)
        state[bucket] = ([path for path in current if path not in cleared]
                         if isinstance(current, list) else [])
    provenance = state.get("edited_provenance")
    state["edited_provenance"] = ({
        path: value for path, value in provenance.items() if path not in cleared
    } if isinstance(provenance, dict) else {})
    if selected is None:
        state["edited_truncated"] = {}
    remaining = {
        path
        for bucket in _BUCKETS
        for path in state.get(bucket, [])
        if isinstance(path, str) and path
    }
    if not remaining and not state.get("edited_truncated"):
        state["edited_prompt_id"] = ""
    # An audit that started before this explicit reset must not complete against files
    # recorded after it. Later edits create a fresh queue and require a fresh checkpoint.
    state["file_checkpoints"] = {}
    _write_state(project_dir, session_id, state)
    report_pending(state)
    print(json.dumps({"cleared": len(cleared), "remaining": len(remaining)},
                     ensure_ascii=False))
    return 0


def cmd_file_checkpoint() -> int:
    project_dir = _cli_project_dir()
    session_id = _session_arg()
    if not session_id:
        print("guard: file checkpoint needs a project and session id.", file=sys.stderr)
        return 1
    args = sys.argv[1:]
    if args and args[0] == "file-checkpoint":
        args = args[1:]
    action = args[0] if args else "show"
    if action == "show":
        if "--token" in args:
            index = args.index("--token")
            if index + 1 >= len(args):
                print("guard: `--token` needs a checkpoint token.", file=sys.stderr)
                return 1
            return _show_token(project_dir, session_id, args[index + 1])
        try:
            selected = _paths_arg(args)
        except ValueError as error:
            print(f"guard: {error}.", file=sys.stderr)
            return 1
        return _show(project_dir, session_id, _host_arg(), selected)
    if action == "clear":
        try:
            selected = _paths_arg(args)
        except ValueError as error:
            print(f"guard: {error}.", file=sys.stderr)
            return 1
        return _clear(project_dir, session_id, selected)
    if action == "complete" and len(args) > 1:
        return _complete(project_dir, session_id, args[1])
    print("guard: use `file-checkpoint show [--paths-json <json-array> | "
          "--token <token>]`, `file-checkpoint clear "
          "[--paths-json <json-array>]`, or "
          "`file-checkpoint complete <token>`.",
          file=sys.stderr)
    return 1
