"""``post-edit`` (PostToolUse on file-writing tools and Bash).

It records a changed file only when the current file-review rules select an audit for it,
keeping the audit buckets disjoint (``agents._edited_bucket``). It sees a subagent's writes
as well as the main agent's, since tool events fire the same hooks inside a subagent
(https://code.claude.com/docs/en/hooks).

Native file tools carry an exact target. Bash does not expose its write-set, so its targets
come from the existing worktree snapshot/hash comparison and are marked as inferred. The
explicit checkpoint states those candidates conditionally: the main session dispatches only
paths it knows it actually modified from its own tool activity, and ignores another session's
writes.
"""

from __future__ import annotations

import hashlib
import json
import subprocess

from pathlib import Path
from typing import Any

from .config import _HOST_IS_CODEX, _load_config
from .cmd_checkpoint import review_rule
from .paths import _doc_scope, _project_dir, _state_root, _trace
from .payload import _read_payload, _session_id
from .agents import _edited_bucket
from .herdr import report_pending
from .state import _read_state, _write_state


# Cap on the files one checkpoint may hand a file-reading agent. Past this the list stops
# being an audit target and becomes a sweep of the whole change: the agent must read
# every file in full to judge it — a comment against the code under it, an instruction
# file against what it points at — and the skills that dispatch these by hand ask the
# user to narrow at roughly this size for the same reason. Recording stops at the cap
# rather than dropping the oldest entries — the earliest edits of a turn are as worth
# auditing as the last, and a stable prefix keeps the recommendation reproducible.
EDITED_FILES_MAX = 100


def _tool_call_id(payload: dict[str, Any]) -> str | None:
    """Stable identifier shared by a tool's pre- and post-use payloads."""
    for key in ("tool_use_id", "call_id"):
        value = payload.get(key)
        if isinstance(value, str) and value:
            return value
    return None


def _bash_snapshot_path(project_dir: Path, session_id: str, tool_call_id: str) -> Path:
    key = hashlib.sha256(f"{session_id}\0{tool_call_id}".encode()).hexdigest()
    return _state_root(project_dir) / "bash-snapshots" / f"{key}.json"


def _bash_hash_cache_path(project_dir: Path) -> Path:
    return _state_root(project_dir) / "bash-hash-cache.json"


def _read_hash_cache(project_dir: Path) -> dict[str, dict[str, Any]]:
    try:
        value = json.loads(_bash_hash_cache_path(project_dir).read_text(encoding="utf-8"))
    except (OSError, ValueError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, dict) else {}


def _write_hash_cache(project_dir: Path, snapshot: dict[str, dict[str, Any]]) -> None:
    path = _bash_hash_cache_path(project_dir)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        tmp = path.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(snapshot, separators=(",", ":")), encoding="utf-8")
        tmp.replace(path)
    except OSError:
        pass


def _git_worktree_snapshot(project_dir: Path, config: dict[str, Any],
                           prior: dict[str, dict[str, Any]] | None = None
                           ) -> dict[str, dict[str, Any]] | None:
    """Return metadata and cached content hashes for reviewable Git-visible files."""
    try:
        result = subprocess.run(
            ["git", "-C", str(project_dir), "ls-files", "--cached", "--others",
             "--exclude-standard", "-z"],
            capture_output=True, check=True, timeout=8,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    try:
        project = project_dir.resolve()
        state_root = _state_root(project_dir).resolve()
    except OSError:
        return None
    snapshot: dict[str, dict[str, Any]] = {}
    for raw in result.stdout.split(b"\0"):
        if not raw:
            continue
        try:
            rel = raw.decode("utf-8", errors="surrogateescape")
            target = project_dir / rel
            resolved = target.resolve()
            stat = target.stat()
        except OSError:
            continue
        if (not target.is_file() or project not in resolved.parents
                or state_root in resolved.parents
                or review_rule(project_dir, resolved, config) is None):
            continue
        cached = (prior or {}).get(rel)
        if (isinstance(cached, dict) and cached.get("mtime_ns") == stat.st_mtime_ns
                and cached.get("size") == stat.st_size
                and isinstance(cached.get("sha256"), str)):
            digest_text = cached["sha256"]
        else:
            try:
                digest = hashlib.sha256()
                with target.open("rb") as stream:
                    for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                        digest.update(chunk)
                digest_text = digest.hexdigest()
            except OSError:
                continue
        snapshot[rel] = {"mtime_ns": stat.st_mtime_ns, "size": stat.st_size,
                         "sha256": digest_text}
    return snapshot


def snapshot_shell_write_candidates(project_dir: Path, payload: dict[str, Any]) -> None:
    """Save the pre-shell Git-visible file set for comparison at PostToolUse."""
    session_id = _session_id(payload)
    tool_call_id = _tool_call_id(payload)
    if session_id is None or tool_call_id is None:
        return
    snapshot = _git_worktree_snapshot(project_dir, _load_config(project_dir),
                                      _read_hash_cache(project_dir))
    if snapshot is None:
        return
    path = _bash_snapshot_path(project_dir, session_id, tool_call_id)
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        value = {"session_id": session_id,
                 "prompt_id": payload.get("prompt_id") or payload.get("turn_id"),
                 "files": snapshot}
        path.write_text(json.dumps(value, separators=(",", ":")), encoding="utf-8")
        _write_hash_cache(project_dir, snapshot)
    except OSError:
        return


def record_shell_writes(project_dir: Path, payload: dict[str, Any],
                        config: dict[str, Any]) -> list[Path]:
    """Record files changed by one shell call and return their absolute paths."""
    session_id = _session_id(payload)
    tool_call_id = _tool_call_id(payload)
    if session_id is None or tool_call_id is None:
        return []
    path = _bash_snapshot_path(project_dir, session_id, tool_call_id)
    try:
        before_value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError, json.JSONDecodeError):
        return []
    if not isinstance(before_value, dict) or not isinstance(before_value.get("files"), dict):
        try:
            path.unlink()
        except OSError:
            pass
        return []

    try:
        path.unlink()
    except OSError:
        pass

    before = before_value["files"]
    after = _git_worktree_snapshot(project_dir, config, before)
    if after is None:
        return []
    _write_hash_cache(project_dir, after)

    def content_hash(value: Any) -> str | None:
        return value.get("sha256") if isinstance(value, dict) else None

    changed = sorted(
        rel for rel in set(before) | set(after)
        if content_hash(before.get(rel)) != content_hash(after.get(rel))
    )
    targets: list[Path] = []
    for rel in changed:
        # A deletion leaves no file for a reviewer to read. A rename's destination is independently present in `after` and is recorded.
        if rel not in after:
            continue
        synthetic_input = {"file_path": rel}
        _record_edited_source(project_dir, payload, synthetic_input, config,
                              source="shell", content_hash=content_hash(after.get(rel)))
        target = _tool_target_path(project_dir, synthetic_input)
        if target is not None:
            targets.append(target)
    if changed:
        _trace(project_dir, session_id, "post-edit", "shell_changes_recorded",
               changed=len(changed))
    return targets


def recover_shell_writes(project_dir: Path, payload: dict[str, Any],
                         config: dict[str, Any]) -> list[Path]:
    """Consume unpaired shell snapshots for this session, as at Stop after an interrupt."""
    session_id = _session_id(payload)
    prompt_id = payload.get("prompt_id")
    if session_id is None or not isinstance(prompt_id, str) or not prompt_id:
        return []
    root = _state_root(project_dir) / "bash-snapshots"
    try:
        candidates = list(root.glob("*.json"))
    except OSError:
        return []
    targets: list[Path] = []
    for path in candidates:
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError, json.JSONDecodeError):
            continue
        if (not isinstance(value, dict) or value.get("session_id") != session_id
                or value.get("prompt_id") != prompt_id):
            continue
        normalized = dict(payload)
        normalized["prompt_id"] = prompt_id
        synthetic_id = path.stem
        normalized["tool_use_id"] = synthetic_id
        expected = _bash_snapshot_path(project_dir, session_id, synthetic_id)
        try:
            expected.parent.mkdir(parents=True, exist_ok=True)
            path.replace(expected)
        except OSError:
            continue
        targets.extend(record_shell_writes(project_dir, normalized, config))
    return targets


def _record_edited_source(project_dir: Path, payload: dict, tool_input: Any,
                          config: dict[str, Any], *, source: str = "native",
                          content_hash: str | None = None) -> None:
    """Note a file this session wrote, for the next explicit file-audit checkpoint.

    A path is retained only when a file-review rule matches it. Storage buckets do not
    select reviewers; the checkpoint resolves every path through the same rules.

    This fires for a SUBAGENT's write as well as the main agent's: tool events run the same
    configured hooks inside a subagent and the payload carries `agent_id` / `agent_type`
    (https://code.claude.com/docs/en/hooks).

    Only inside the project: an audit of a file outside the working tree is not this
    turn's work to fix. Files under guard's own state are excluded too — a turn slice is
    a record, not code.

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
    try:
        project = project_dir.resolve()
        state_root = _state_root(project_dir).resolve()
        docs = _doc_scope(project_dir, config)
    except OSError:
        return
    bucket = _edited_bucket(target, docs)
    if bucket is None:
        return
    if project not in target.parents or state_root in target.parents:
        return

    state = _read_state(project_dir, session_id, config)
    # Settings may have changed since older paths entered the queue. Reconcile before every
    # new write so the Herdr token and status state never retain a path no current rule audits.
    from .cmd_checkpoint import reconcile_queue
    reconcile_queue(project_dir, state, "codex" if _HOST_IS_CODEX else "claude")
    if review_rule(project_dir, target, config) is None:
        _write_state(project_dir, session_id, state)
        report_pending(state)
        return

    if content_hash is None:
        try:
            digest = hashlib.sha256()
            with target.open("rb") as stream:
                for chunk in iter(lambda: stream.read(1024 * 1024), b""):
                    digest.update(chunk)
            content_hash = digest.hexdigest()
        except OSError:
            return

    # This marker is diagnostic only. The queue intentionally crosses turn boundaries and is
    # cleared by checkpoint completion, not by the next prompt.
    state["edited_prompt_id"] = prompt_id
    # `.get`, not `[]`: a state file written before a bucket existed may lack the key.
    files = state.get(bucket)
    if not isinstance(files, list):
        files = []
    path = str(target)
    provenance = state.get("edited_provenance")
    if not isinstance(provenance, dict):
        provenance = {}
    provenance[path] = {"sha256": content_hash, "source": source}
    state["edited_provenance"] = provenance
    if path in files:
        _write_state(project_dir, session_id, state)
        report_pending(state)
        return
    if len(files) >= EDITED_FILES_MAX:
        truncated = state.get("edited_truncated")
        if not isinstance(truncated, dict):
            truncated = {}
        truncated[bucket] = int(truncated.get(bucket, 0)) + 1
        state["edited_truncated"] = truncated
        _write_state(project_dir, session_id, state)
        report_pending(state)
        return
    files.append(path)
    state[bucket] = files
    _write_state(project_dir, session_id, state)
    report_pending(state)
    _trace(project_dir, session_id, "post-edit", "edited_recorded",
           prompt_id=prompt_id, bucket=bucket, file=target.name, count=len(files))


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


def cmd_post_edit() -> int:
    """PostToolUse on the file-writing tools: record what was written.

    The list is consumed by an explicit file checkpoint. This is the event that actually
    sees the path, so nothing has to be reconstructed from a transcript later; Stop only
    reads back what accumulated here. It never emits anything.
    """
    project_dir = _project_dir()
    payload = _read_payload()
    if payload is None or project_dir is None:
        return 0

    config = _load_config(project_dir)
    if payload.get("tool_name") == "Bash":
        record_shell_writes(project_dir, payload, config)
        return 0
    _record_edited_source(project_dir, payload, payload.get("tool_input"), config)
    return 0
