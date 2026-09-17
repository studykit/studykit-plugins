"""Explicit file-audit checkpoints over the session's accumulated dirty queue."""

from __future__ import annotations

import hashlib
import json
import os
import sys

from pathlib import Path
from typing import Any

from .config import AgentMode, _agent_mode, _doc_review_rule, _doc_review_rules, _load_config
from .herdr import report_pending
from .paths import _cli_project_dir, _project_rel
from .state import _edit_source, _edited_files, _read_state, _write_state


_BUCKETS = ("edited_files", "edited_agent_docs", "edited_refs", "edited_docs")
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


def _plan(project_dir: Path, state: dict[str, Any], host: str,
          snapshot: dict[str, dict[str, str]]) -> list[dict[str, Any]]:
    config = _load_config(project_dir)
    groups: dict[tuple[str, str, bool], list[str]] = {}

    source_paths = [path for path, item in snapshot.items()
                    if item["bucket"] == "edited_files"]
    if (host == "claude" and source_paths
            and _agent_mode(state, "comment-corrector") != AgentMode.OFF):
        for path in source_paths:
            conditional = _edit_source(state, path) != "native"
            groups.setdefault(("agent", "guard:comment-corrector", conditional), []).append(path)

    if _agent_mode(state, "doc-auditor") != AgentMode.OFF:
        rules = _doc_review_rules(config)
        for path, item in snapshot.items():
            if item["bucket"] == "edited_files":
                continue
            rule = _doc_review_rule(_project_rel(project_dir, Path(path)), rules)
            if rule is None:
                continue
            name = rule.name
            if host == "codex" and rule.kind == "agent":
                name = _CODEX_AGENTS.get(name, name)
            conditional = _edit_source(state, path) != "native"
            groups.setdefault((rule.kind, name, conditional), []).append(path)

    return [
        {"kind": kind, "name": name, "conditional": conditional, "paths": paths}
        for (kind, name, conditional), paths in groups.items()
    ]


def _show(project_dir: Path, session_id: str, host: str) -> int:
    config = _load_config(project_dir)
    state = _read_state(project_dir, session_id, config)
    _prune_missing(state)
    snapshot = _snapshot(state)
    groups = _plan(project_dir, state, host, snapshot)
    reviewed = {path for group in groups for path in group["paths"]}
    payload = {"files": snapshot, "groups": groups,
               "unreviewed": [path for path in snapshot if path not in reviewed],
               "truncated": state.get("edited_truncated", {})}
    token = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
    payload["token"] = token
    checkpoints = state.get("file_checkpoints")
    if not isinstance(checkpoints, dict):
        checkpoints = {}
    truncated = state.get("edited_truncated")
    checkpoints[token] = {
        "files": snapshot,
        "truncated": dict(truncated) if isinstance(truncated, dict) else {},
    }
    # Display refreshes also call `show`; keep several live tokens so a panel refresh cannot
    # invalidate an audit already in flight, but bound stale snapshot growth.
    state["file_checkpoints"] = dict(list(checkpoints.items())[-8:])
    _write_state(project_dir, session_id, state)
    report_pending(state)
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
        return _show(project_dir, session_id, _host_arg())
    if action == "complete" and len(args) > 1:
        return _complete(project_dir, session_id, args[1])
    print("guard: use `file-checkpoint show` or `file-checkpoint complete <token>`.",
          file=sys.stderr)
    return 1
