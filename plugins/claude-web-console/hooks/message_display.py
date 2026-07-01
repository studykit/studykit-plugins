#!/usr/bin/env python3
"""MessageDisplay hook -> stream assistant text deltas to the web console.

Writes nothing to stdout so Claude Code displays the original text unchanged
(this hook is a passive mirror, not a display transformer). Always exits 0.

The payload fields (turn_id, message_id, index, final, delta) are documented at
https://code.claude.com/docs/en/hooks#messagedisplay ; `delta` is incremental
(newly completed lines since the prior batch), and `final` marks the last batch.
"""
from __future__ import annotations

from _emit import emit, read_payload


def main() -> None:
    payload = read_payload()
    emit(
        {
            "type": "assistant_delta",
            "turn_id": payload.get("turn_id"),
            "message_id": payload.get("message_id"),
            "index": payload.get("index"),
            "final": payload.get("final"),
            "delta": payload.get("delta", ""),
        }
    )


if __name__ == "__main__":
    main()
