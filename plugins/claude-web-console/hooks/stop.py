#!/usr/bin/env python3
"""Stop hook -> tell the web console the assistant turn ended.

The viewer uses this to finalize rendering of the last message. Writes nothing
to stdout and always exits 0.
"""
from __future__ import annotations

from _emit import emit, read_payload


def main() -> None:
    payload = read_payload()
    emit({"type": "turn_end", "turn_id": payload.get("turn_id")})


if __name__ == "__main__":
    main()
