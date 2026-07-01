#!/usr/bin/env python3
"""UserPromptSubmit hook -> mirror the user's prompt to the web console.

Writes nothing to stdout (UserPromptSubmit stdout is injected into the
conversation as context) and always exits 0.
"""
from __future__ import annotations

from _emit import emit, read_payload


def main() -> None:
    payload = read_payload()
    text = payload.get("prompt", "")
    if text:
        emit({"type": "user", "text": text})


if __name__ == "__main__":
    main()
