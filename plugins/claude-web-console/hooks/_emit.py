#!/usr/bin/env python3
"""Shared helper for claude-web-console hooks.

Each hook is a short-lived process that must never disrupt the conversation, so
every failure here (server down, timeout, malformed JSON) is swallowed silently.
"""
from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request

DEFAULT_PORT = 8477
_POST_TIMEOUT_SECONDS = 0.5


def _port() -> int:
    try:
        return int(os.environ.get("CLAUDE_WEB_CONSOLE_PORT", ""))
    except ValueError:
        return DEFAULT_PORT


def emit(event: dict) -> None:
    """Best-effort POST of one event to the local server; never raises."""
    url = f"http://127.0.0.1:{_port()}/event"
    data = json.dumps(event).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        urllib.request.urlopen(req, timeout=_POST_TIMEOUT_SECONDS).close()
    except (urllib.error.URLError, OSError, ValueError):
        pass


def read_payload() -> dict:
    """Read the hook JSON payload from stdin; return {} on any error."""
    try:
        return json.loads(sys.stdin.read() or "{}")
    except (json.JSONDecodeError, ValueError):
        return {}
