#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""Claude PermissionRequest adapter: reuse existing consent for checkpoint bookkeeping."""

import json
import os
from pathlib import Path
import sys


TOOLS = {"mcp__plugin_guard_review__get_review_checkpoint",
         "mcp__plugin_guard_review__complete_review_checkpoint"}


def main() -> None:
    try:
        payload = json.load(sys.stdin)
        if not isinstance(payload, dict) or payload.get("hook_event_name") != "PermissionRequest":
            return
        if payload.get("tool_name") not in TOOLS:
            return
        # A user-configured MCP server can mimic a tool name; require host provenance.
        server = payload.get("mcp_server")
        if not isinstance(server, dict) or server.get("source") != "plugin" or server.get("name") != "plugin:guard:review":
            return
        arguments = payload.get("tool_input")
        if not isinstance(arguments, dict) or set(arguments) != {"review_id"}:
            return
        if not all(isinstance(value, str) for value in arguments.values()):
            return
        session = payload.get("session_id")
        root, data = os.environ.get("CLAUDE_PROJECT_DIR"), os.environ.get("CLAUDE_PLUGIN_DATA")
        if not isinstance(session, str) or not root or not data or not Path(root).is_absolute():
            return
        project = Path(root).resolve(strict=True)
        os.environ["GUARD_HOST"] = "claude"
        for parent in Path(__file__).resolve().parents:
            if (parent / "scripts/guard_core/__init__.py").is_file():
                sys.path.insert(0, str(parent / "scripts"))
                break
        from guard_core.stop_review import review_authorized
        if review_authorized(Path(data), "claude", arguments["review_id"], project, session):
            print(json.dumps({"hookSpecificOutput": {"hookEventName": "PermissionRequest",
                              "decision": {"behavior": "allow"}}}))
    except (OSError, ValueError, TypeError, ImportError):
        # No decision means the host retains its ordinary permission flow.
        return


if __name__ == "__main__":
    main()
