"""User-confirmed file checkpoints. Host adapters own MCP and native hook payloads."""

from __future__ import annotations

from contextlib import contextmanager, redirect_stderr, redirect_stdout
import io
import json
import os
from pathlib import Path
import re
import secrets
import string
import time
from typing import Any
import uuid

from .cmd_checkpoint import _complete, _plan, _review_fingerprint, _show, _show_token, _snapshot, review_rule
from .config import _HOST_IS_CODEX, _load_config
from .dispatch import _plugin_root
from .paths import _state_root
from .state import _read_state, _write_state


QUESTION_SECONDS = 300
MAX_SEEN = 2048
REVIEW_ID_PATTERN = r"[A-Za-z0-9]{8}"


def _path(project: Path, session: str) -> Path:
    if not re.fullmatch(r"[A-Za-z0-9._-]+", session) or ".." in session:
        raise ValueError("Invalid Guard session id")
    return _state_root(project) / "stop-consent" / f"{session}.json"


@contextmanager
def _locked(path: Path):
    """Only consent-state transitions are locked; no lock is held while asking the user."""
    path.parent.mkdir(parents=True, exist_ok=True)
    lock = path.with_suffix(".lock")
    deadline = time.monotonic() + 2
    while True:
        try:
            lock.mkdir()
            break
        except FileExistsError:
            try:
                if time.time() - lock.stat().st_mtime > 60:
                    lock.rmdir()
                    continue
            except FileNotFoundError:
                continue
            if time.monotonic() >= deadline:
                raise RuntimeError("Another Guard consent update is in progress")
            time.sleep(.02)
    try:
        yield
    finally:
        lock.rmdir()


def _read(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"seen": {}}
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict) or not isinstance(value.get("seen", {}), dict):
        raise ValueError("Invalid Guard Stop consent state")
    return value


def _write(path: Path, state: dict[str, Any]) -> None:
    temporary = path.with_name(path.name + "." + uuid.uuid4().hex + ".tmp")
    try:
        with os.fdopen(os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600), "w", encoding="utf-8") as stream:
            json.dump(state, stream, ensure_ascii=False)
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)


def _eligible(project: Path, session: str, host: str) -> dict[str, Any]:
    config = _load_config(project)
    state = _read_state(project, session, config)
    files = {}
    fingerprints = {}
    for path, revision in sorted(_snapshot(state).items()):
        rule = review_rule(project, Path(path), config)
        if rule is None or rule.on_stop != "ask":
            continue
        files[path] = revision
        fingerprints[path] = _review_fingerprint(revision, rule)
    return {"files": files, "fingerprints": fingerprints,
            "groups": _plan(project, state, host, files),
            "truncated": state.get("edited_truncated", {})}


def prepare(project_dir: Path, session_id: str, host: str, *,
            stop_hook_active: bool = False) -> dict[str, Any]:
    """Freeze previously unoffered ask-enabled revisions from the existing session queue."""
    if host not in {"claude", "codex"}:
        raise ValueError("Unknown Guard host")
    if (host == "codex") != _HOST_IS_CODEX:
        raise ValueError("Host does not match the loaded Guard configuration")
    if stop_hook_active:
        return {"status": "continuation"}
    project = project_dir.resolve(strict=True)
    path = _path(project, session_id)
    eligible = _eligible(project, session_id, host)
    if not eligible["files"]:
        return {"status": "empty"}
    with _locked(path):
        state = _read(path)
        pending = state.get("pending")
        if isinstance(pending, dict) and time.time() - pending.get("created_at", 0) < QUESTION_SECONDS:
            return {"status": "pending"}
        seen = state.get("seen", {})
        selected = {name: revision for name, revision in eligible["files"].items()
                    if seen.get(name, {}).get("fingerprint") != eligible["fingerprints"][name]}
        if not selected:
            return {"status": "unchanged"}
        fingerprints = {name: eligible["fingerprints"][name] for name in selected}
        request_id = uuid.uuid4().hex
        groups = [{**group, "paths": [name for name in group["paths"] if name in selected]}
                  for group in eligible["groups"]]
        groups = [group for group in groups if group["paths"]]
        state["pending"] = {"request_id": request_id, "created_at": time.time(),
                            "files": selected, "fingerprints": fingerprints,
                            "groups": groups, "host": host}
        _write(path, state)
    names = [Path(name).relative_to(project).as_posix() for name in selected]
    reviewers = sorted({group["kind"] + ":" + group["name"] for group in groups})
    description = "\n".join(names[:20])
    if len(names) > 20:
        description += f"\n… and {len(names) - 20} more files"
    scope = names[0] if len(names) == 1 else f"{len(names)} changed files"
    message = (f"Guard: review {scope}? Reviewers: {', '.join(reviewers)}\n"
               f"Files:\n{description}\n"
               "Approval includes scope lookup and marking reviewed revisions complete, not fixing findings. "
               "Only the listed checkpoint will be reviewed. Declining or cancelling keeps "
               "these files pending and suppresses another question for these revisions. "
               "This question expires after 5 minutes; use audit-files to retry.")
    if any(value for value in eligible["truncated"].values() if isinstance(value, int)):
        message += "\nThe queue is capped: this is a partial checkpoint."
    return {"status": "ask", "request_id": request_id, "message": message,
            "requested_schema": {"type": "object", "properties": {
                "review_action": {"type": "string", "title": "Review decision",
                    "oneOf": [{"const": "review", "title": "Run the configured reviewers"},
                              {"const": "later", "title": "Keep pending for later"}]}},
                "required": ["review_action"]}}


def _finish(state: dict[str, Any], request: dict[str, Any], outcome: str) -> None:
    seen = state.setdefault("seen", {})
    for name, fingerprint in request["fingerprints"].items():
        seen.pop(name, None)
        seen[name] = {"fingerprint": fingerprint, "outcome": outcome}
    state["seen"] = dict(list(seen.items())[-MAX_SEEN:])
    state.pop("pending", None)
    state["last_answer"] = {"request_id": request["request_id"], "outcome": outcome,
                            "answered_at": time.time()}


def _same_groups(left: list[dict[str, Any]], right: list[dict[str, Any]]) -> bool:
    def canonical(groups: list[dict[str, Any]]) -> list[str]:
        return sorted(json.dumps({**group, "paths": sorted(group["paths"])}, sort_keys=True)
                      for group in groups)
    return canonical(left) == canonical(right)


def _dispatch(review_id: str) -> dict[str, Any]:
    arguments = json.dumps({"review_id": review_id})
    return {"decision": "block", "reason": (
        "Guard: review approved. Continue with the configured reviewers; implementation is not approved.\n"
        "Call Guard's review MCP tool get_review_checkpoint with these exact arguments:\n"
        f"{arguments}\nFollow its workflow, then use complete_review_checkpoint with the same arguments. "
        "Do not substitute a fresh checkpoint or ask again for review consent.")}


def checkpoint_authorized(project: Path, session: str, token: str) -> bool:
    """Check persisted consent without creating a checkpoint or completing one."""
    _path(project, session)  # Validate the session before opening its state file.
    if not isinstance(token, str) or not re.fullmatch(r"[0-9a-f]{64}", token):
        return False
    state = _read_state(project, session, _load_config(project))
    checkpoints = state.get("file_checkpoints", {})
    checkpoint = checkpoints.get(token) if isinstance(checkpoints, dict) else None
    if not isinstance(checkpoint, dict):
        return False
    approved, files = checkpoint.get("approved_stop"), checkpoint.get("files")
    return (isinstance(approved, dict) and bool(approved) and isinstance(files, dict)
            and set(approved) == set(files) and isinstance(checkpoint.get("groups"), list))


def approved_checkpoint(project: Path, session: str, token: str, *, complete: bool = False) -> dict[str, Any]:
    """Expose only an existing Stop-approved scope, never create approval from a tool call."""
    if not checkpoint_authorized(project, session, token):
        raise ValueError("No Stop-approved checkpoint for this project and session; use audit-files to retry.")
    output, errors = io.StringIO(), io.StringIO()
    with redirect_stdout(output), redirect_stderr(errors):
        result = (_complete if complete else _show_token)(project, session, token)
    if result:
        raise ValueError(errors.getvalue().strip() or "Checkpoint operation failed; files remain pending.")
    payload = json.loads(output.getvalue())
    if not complete:
        workflow = _plugin_root() / "skills" / "audit-files" / "SKILL.md"
        payload["workflow"] = workflow.read_text(encoding="utf-8")
    else:
        payload["meaning"] = "Reviewed revisions were cleared. This is not a clean verdict or proof that findings were fixed."
    return payload


def _review_path(data_dir: Path, review_id: str) -> Path:
    if not isinstance(review_id, str) or not re.fullmatch(REVIEW_ID_PATTERN, review_id):
        raise ValueError("Invalid review_id")
    return data_dir / "reviews" / (review_id + ".json")


def review_binding(data_dir: Path, host: str, review_id: str) -> dict[str, Any]:
    record = _read(_review_path(data_dir, review_id))
    if record.get("host") != host or (host == "codex") != _HOST_IS_CODEX:
        raise ValueError("Unknown review_id for this host")
    project, session = record.get("project"), record.get("session")
    if not isinstance(project, str) or not Path(project).is_absolute() or not isinstance(session, str):
        raise ValueError("Invalid review binding")
    _path(Path(project), session)
    if not isinstance(record.get("checkpoint"), dict) or record["checkpoint"].get("review_id") != review_id:
        raise ValueError("Invalid review scope")
    return record


def _receipt(state: dict[str, Any], review_id: str) -> dict[str, Any] | None:
    receipts = state.get("file_review_receipts", {})
    if not isinstance(receipts, dict):
        raise ValueError("Invalid review receipts")
    receipt = receipts.get(review_id)
    if receipt is None:
        return None
    if (not isinstance(receipt, dict) or receipt.get("review_id") != review_id
            or receipt.get("status") != "completed"
            or any(type(receipt.get(key)) is not int or receipt[key] < 0 for key in ("cleared", "remaining"))):
        raise ValueError("Invalid completion receipt")
    return receipt


def review_authorized(data_dir: Path, host: str, review_id: str, project: Path, session: str) -> bool:
    """Native permission hooks additionally bind the ID to host-provided caller context."""
    record = review_binding(data_dir, host, review_id)
    if record["project"] != str(project.resolve()) or record["session"] != session:
        return False
    state = _read_state(project, session, _load_config(project))
    receipt = _receipt(state, review_id)
    return (isinstance(receipt, dict) or
            (checkpoint_authorized(project, session, record["token"]) and
             state["file_checkpoints"].get(record["token"]) == record["checkpoint"]))


def review_checkpoint(data_dir: Path, host: str, review_id: str, *, complete: bool = False) -> dict[str, Any]:
    path = _review_path(data_dir, review_id)
    with _locked(path):
        record = review_binding(data_dir, host, review_id)
        project, session, token = Path(record["project"]), record["session"], record["token"]
        with _locked(_path(project, session)):
            state = _read_state(project, session, _load_config(project))
            receipt = _receipt(state, review_id)
            if isinstance(receipt, dict):
                return receipt
            if not checkpoint_authorized(project, session, token) or state["file_checkpoints"].get(token) != record["checkpoint"]:
                raise ValueError("Approved review is stale or invalid; request fresh consent")
            if complete:
                output, errors = io.StringIO(), io.StringIO()
                with redirect_stdout(output), redirect_stderr(errors):
                    result = _complete(project, session, token, review_id=review_id)
                if result:
                    raise ValueError(errors.getvalue().strip() or "Review completion could not be saved")
                return json.loads(output.getvalue())
            payload = approved_checkpoint(project, session, token)
            payload.pop("token", None)
            return {"review_id": review_id, "status": "approved", **payload}


def unavailable(project: Path, session: str, host: str) -> dict[str, Any]:
    if not _eligible(project, session, host)["files"]:
        return {}
    return {"systemMessage": "Guard: this host does not support review confirmation forms. "
            "No review was started; files remain pending. Invoke audit-files to review them manually."}


def answer(project_dir: Path, session_id: str, host: str, request_id: str,
           action: str, content: dict[str, Any] | None = None, *, data_dir: Path) -> dict[str, Any]:
    """Only the MCP adapter calls this with an actual elicitation response."""
    project = project_dir.resolve(strict=True)
    if (host == "codex") != _HOST_IS_CODEX or host not in {"claude", "codex"}:
        raise ValueError("Host does not match the loaded Guard configuration")
    path = _path(project, session_id)
    with _locked(path):
        state = _read(path)
        request = state.get("pending")
        if not isinstance(request, dict) or request.get("request_id") != request_id:
            return {}
        if request.get("host") != host:
            raise ValueError("Consent belongs to another host")
        accepted = action == "accept" and isinstance(content, dict) and content.get("review_action") == "review"
        if not accepted:
            _finish(state, request, "cancelled" if action == "cancel" else "declined")
            _write(path, state)
            return {"systemMessage": "Guard: no review started; files remain pending. Use audit-files to review them later."}
        current = _eligible(project, session_id, host)
        unchanged = all(current["fingerprints"].get(name) == digest
                        for name, digest in request["fingerprints"].items())
        expired = time.time() - request["created_at"] >= QUESTION_SECONDS
        if not unchanged or expired:
            _finish(state, request, "stale")
            _write(path, state)
            cause = "the confirmation expired" if expired else "the files or review rules changed while the form was open"
            return {"systemMessage": f"Guard: {cause}. No review was started; files remain pending. "
                    "Invoke audit-files to retry."}
        capture = io.StringIO()
        try:
            with redirect_stdout(capture):
                _show(project, session_id, host, set(request["files"]),
                      approved_fingerprints=request["fingerprints"])
            checkpoint = json.loads(capture.getvalue())
            if checkpoint.get("files") != request["files"] or not _same_groups(checkpoint["groups"], request["groups"]):
                raise ValueError("The approved checkpoint changed")
            saved = _read_state(project, session_id, _load_config(project))
            if checkpoint["token"] not in saved.get("file_checkpoints", {}):
                raise OSError("Could not persist the approved checkpoint")
        except Exception:
            _finish(state, request, "failed")
            _write(path, state)
            raise
        # Reserve under the per-ID lock so a collision cannot replace an approval.
        for _ in range(8):
            review_id = "".join(secrets.choice(string.ascii_letters + string.digits) for _ in range(8))
            record_path = _review_path(data_dir, review_id)
            record_path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
            with _locked(record_path):
                if record_path.exists():
                    continue
                checkpoint_state = saved["file_checkpoints"][checkpoint["token"]]
                checkpoint_state["review_id"] = review_id
                _write_state(project, session_id, saved)
                if _read_state(project, session_id, _load_config(project))["file_checkpoints"].get(checkpoint["token"]) != checkpoint_state:
                    raise OSError("Could not persist review binding")
                _write(record_path, {"host": host, "project": str(project), "session": session_id,
                                    "token": checkpoint["token"], "checkpoint": checkpoint_state})
                break
        else:
            raise RuntimeError("Could not allocate a distinct review ID")
        _finish(state, request, "approved")
        _write(path, state)
    return _dispatch(review_id)


def failure(project_dir: Path, session_id: str, request_id: str) -> None:
    """A failed form never clears the review queue or fabricates user approval."""
    path = _path(project_dir.resolve(strict=True), session_id)
    with _locked(path):
        state = _read(path)
        request = state.get("pending")
        if isinstance(request, dict) and request.get("request_id") == request_id:
            _finish(state, request, "failed")
            _write(path, state)
