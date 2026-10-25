#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""Stdio MCP adapter for native Stop-hook file-review consent.

The protocol adapter requests the host's form UI; it never calls a model. The
shared workflow receives concrete project/session values and only an actual
elicitation response can be handed to its answer function.
"""

from __future__ import annotations

import argparse
import asyncio
from contextlib import redirect_stdout
import importlib
import io
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import threading
from typing import Any


MAX_LINE = 1024 * 1024
MAX_CALLS = 4
SUPPORTED_PROTOCOLS = {"2024-11-05", "2025-03-26", "2025-06-18", "2025-11-25"}
SESSION_ID = re.compile(r"[A-Za-z0-9._-]{1,160}\Z")
TOOL = "confirm_file_review"
ARGUMENTS = {"cwd", "session_id", "stop_hook_active", "transcript_path", "turn_id", "prompt_id"}


def plugin_root() -> Path:
    for parent in Path(__file__).resolve().parents:
        if (parent / "scripts" / "guard_core" / "__init__.py").is_file():
            return parent
    raise RuntimeError("Guard plugin root not found")


def load_core(host: str) -> Any:
    # Configuration selects host-specific paths at import, not once per call.
    os.environ["GUARD_HOST"] = host
    sys.path.insert(0, str(plugin_root() / "scripts"))
    return importlib.import_module("guard_core.stop_review")


def identity(value: Any) -> tuple[type, str | int] | None:
    if isinstance(value, bool) or not isinstance(value, (str, int)):
        return None
    return type(value), value


def project_dir(cwd: str, host: str) -> Path:
    path = Path(cwd).expanduser()
    if not path.is_absolute() or not path.is_dir():
        raise ValueError("cwd must be an existing absolute directory")
    if host == "claude" and os.environ.get("CLAUDE_PROJECT_DIR"):
        project = Path(os.environ["CLAUDE_PROJECT_DIR"]).expanduser()
        if project.is_absolute() and project.is_dir():
            return project.resolve()
    try:
        result = subprocess.run(["git", "-C", str(path), "rev-parse", "--show-toplevel"],
                                capture_output=True, text=True, timeout=5)
        if result.returncode == 0 and result.stdout.strip():
            return Path(result.stdout.strip()).resolve()
    except (OSError, subprocess.SubprocessError):
        pass
    return path.resolve()


def normalized_arguments(value: Any, host: str) -> tuple[Path, str, bool]:
    if not isinstance(value, dict) or set(value) - ARGUMENTS:
        raise ValueError("Only documented Stop-hook context arguments are accepted")
    cwd, session = value.get("cwd"), value.get("session_id")
    if not isinstance(cwd, str) or not isinstance(session, str):
        raise ValueError("cwd and session_id are required")
    if not SESSION_ID.fullmatch(session) or ".." in session:
        raise ValueError("session_id is invalid")
    active = value.get("stop_hook_active", False)
    if isinstance(active, str) and active in {"true", "false"}:
        active = active == "true"
    if not isinstance(active, bool):
        raise ValueError("stop_hook_active must be a boolean")
    for key in ("transcript_path", "turn_id", "prompt_id"):
        if key in value and value[key] is not None and not isinstance(value[key], str):
            raise ValueError(f"{key} must be a string")
    return project_dir(cwd, host), session, active


class Server:
    def __init__(self, core: Any, host: str, timeout: float = 300) -> None:
        self.core, self.host, self.timeout = core, host, timeout
        self.form_supported = False
        self.initialized = False
        self.closing = False
        self.sequence = 0
        self.pending: dict[tuple[type, str | int], asyncio.Future] = {}
        self.calls: dict[tuple[type, str | int], asyncio.Task] = {}
        self.output = sys.stdout

    def send(self, message: dict[str, Any]) -> None:
        if not self.closing:
            self.output.write(json.dumps({"jsonrpc": "2.0", **message}, ensure_ascii=False) + "\n")
            self.output.flush()

    def error(self, request: Any, code: int, message: str) -> None:
        self.send({"id": request, "error": {"code": code, "message": message}})

    def tool_result(self, request: str | int, output: dict[str, Any], *, failed: bool = False) -> None:
        self.send({"id": request, "result": {"content": [{"type": "text", "text": json.dumps(output, ensure_ascii=False)}],
                                            **({"isError": True} if failed else {})}})

    def invoke(self, function: str, *args: Any, **kwargs: Any) -> Any:
        # Existing checkpoint helpers use stdout. It must never become an MCP frame.
        with redirect_stdout(io.StringIO()):
            return getattr(self.core, function)(*args, **kwargs)

    async def call(self, request: str | int, arguments: Any) -> None:
        prepared_id = None
        project = None
        session = None
        settled = False
        elicitation_key = None
        try:
            project, session, active = normalized_arguments(arguments, self.host)
            if not self.form_supported:
                self.tool_result(request, {})
                return
            prepared = self.invoke("prepare", project, session, self.host, stop_hook_active=active)
            if prepared.get("status") != "ask":
                self.tool_result(request, prepared.get("output", {}))
                return
            prepared_id = prepared["request_id"]
            self.sequence += 1
            elicitation_id = f"guard-elicitation-{self.sequence}"
            elicitation_key = identity(elicitation_id)
            future = asyncio.get_running_loop().create_future()
            self.pending[elicitation_key] = future
            self.send({"id": elicitation_id, "method": "elicitation/create", "params": {
                "mode": "form", "message": prepared["message"], "requestedSchema": prepared["requested_schema"]}})
            response = await asyncio.wait_for(future, self.timeout)
            result = response.get("result")
            if "error" in response or not isinstance(result, dict):
                raise ValueError("Elicitation failed")
            action, content = result.get("action"), result.get("content")
            if action not in {"accept", "decline", "cancel"} or (content is not None and not isinstance(content, dict)):
                raise ValueError("Malformed elicitation result")
            output = self.invoke("answer", project, session, self.host, prepared_id, action, content)
            settled = True
            self.tool_result(request, output)
        except asyncio.CancelledError:
            if prepared_id is not None:
                try:
                    self.invoke("failure", project, session, prepared_id)
                    settled = True
                except Exception:
                    pass
            self.tool_result(request, {"systemMessage": "Guard file-review question was cancelled; files remain unreviewed."}, failed=True)
        except Exception as error:
            if prepared_id is not None:
                try:
                    self.invoke("failure", project, session, prepared_id)
                    settled = True
                except Exception:
                    pass
            self.tool_result(request, {"systemMessage": "Guard could not obtain file-review consent; files remain unreviewed.",
                                       "error": type(error).__name__}, failed=True)
        finally:
            if elicitation_key is not None:
                self.pending.pop(elicitation_key, None)
            if prepared_id is not None and not settled:
                try:
                    self.invoke("failure", project, session, prepared_id)
                except Exception:
                    pass
            self.calls.pop(identity(request), None)

    def receive(self, message: Any) -> None:
        if not isinstance(message, dict) or message.get("jsonrpc") != "2.0":
            self.error(None, -32600, "Invalid JSON-RPC message")
            return
        request = message.get("id")
        key = identity(request)
        method = message.get("method")
        if method is None:
            future = self.pending.get(key)
            if future is not None and not future.done():
                future.set_result(message)
            return
        if method == "notifications/cancelled":
            params = message.get("params")
            task = self.calls.get(identity(params.get("requestId"))) if isinstance(params, dict) else None
            if task is not None:
                task.cancel()
            return
        if key is None:
            # MCP notifications do not have a response.
            if "id" in message:
                self.error(None, -32600, "Invalid request id")
            return
        if method == "initialize":
            params = message.get("params", {})
            if self.initialized or not isinstance(params, dict):
                self.error(request, -32600, "Invalid initialize request")
                return
            self.initialized = True
            capabilities = params.get("capabilities", {})
            elicitation = capabilities.get("elicitation") if isinstance(capabilities, dict) else None
            self.form_supported = isinstance(elicitation, dict) and isinstance(elicitation.get("form"), dict)
            protocol = params.get("protocolVersion")
            self.send({"id": request, "result": {"protocolVersion": protocol if isinstance(protocol, str) and protocol in SUPPORTED_PROTOCOLS else "2025-11-25",
                       "capabilities": {"tools": {}}, "serverInfo": {"name": "guard-review-consent", "version": "0.163.0"},
                       "instructions": "Guard collects user consent for project-configured file reviews. Review criteria and reviewers belong to the project."}})
        elif method == "ping":
            self.send({"id": request, "result": {}})
        elif method == "tools/list" and self.initialized:
            self.send({"id": request, "result": {"tools": [{"name": TOOL,
                "description": "Guard Stop-hook entry point. Ask the user whether to review opted-in pending file revisions; return a continuation only after the host supplies their accepted form response. This tool does not run reviewers itself.",
                "inputSchema": {"type": "object", "properties": {
                    "cwd": {"type": "string"}, "session_id": {"type": "string"},
                    "stop_hook_active": {"oneOf": [{"type": "boolean"}, {"type": "string", "enum": ["true", "false"]}]},
                    "transcript_path": {"type": ["string", "null"]}, "turn_id": {"type": ["string", "null"]}, "prompt_id": {"type": ["string", "null"]}},
                    "required": ["cwd", "session_id"], "additionalProperties": False},
                "annotations": {"readOnlyHint": False, "destructiveHint": False, "openWorldHint": False}}]}})
        elif method == "tools/call" and self.initialized:
            params = message.get("params")
            if not isinstance(params, dict) or params.get("name") != TOOL:
                self.error(request, -32602, "Unknown Guard tool")
            elif key in self.calls or len(self.calls) >= MAX_CALLS:
                self.error(request, -32600, "Guard request already running or call limit reached")
            else:
                self.calls[key] = asyncio.create_task(self.call(request, params.get("arguments")))
        else:
            self.error(request, -32601, "Method not found")

    async def run(self) -> None:
        queue: asyncio.Queue = asyncio.Queue(maxsize=64)
        loop = asyncio.get_running_loop()

        def reader() -> None:
            while True:
                line = sys.stdin.buffer.readline(MAX_LINE + 1)
                future = asyncio.run_coroutine_threadsafe(queue.put(line), loop)
                try:
                    future.result()
                except Exception:
                    return
                if not line or len(line) > MAX_LINE:
                    return

        threading.Thread(target=reader, daemon=True).start()
        try:
            while True:
                line = await queue.get()
                if not line:
                    break
                if len(line) > MAX_LINE:
                    self.error(None, -32600, "MCP message exceeds size limit")
                    break
                try:
                    message = json.loads(line)
                except (ValueError, UnicodeDecodeError):
                    self.error(None, -32700, "Invalid JSON")
                    continue
                self.receive(message)
        finally:
            self.closing = True
            tasks = list(self.calls.values())
            for task in tasks:
                task.cancel()
            await asyncio.gather(*tasks, return_exceptions=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", choices=("claude", "codex"), required=True)
    parser.add_argument("--elicitation-timeout", type=float, default=300)
    arguments = parser.parse_args()
    if not 0 < arguments.elicitation_timeout <= 300:
        parser.error("elicitation timeout must be greater than zero and at most 300 seconds")
    asyncio.run(Server(load_core(arguments.host), arguments.host, arguments.elicitation_timeout).run())


if __name__ == "__main__":
    main()
