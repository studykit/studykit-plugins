# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Normalize the native hook-only data path for explicit skill commands."""

import json
import os
from pathlib import Path
import sys


def main() -> None:
    payload = json.load(sys.stdin)
    if payload.get("hook_event_name") != "SessionStart":
        return
    raw = os.environ.get("PLUGIN_DATA")
    if not raw:
        return
    data = Path(raw).resolve()
    context = (
        f"Delegate plugin storage from native PLUGIN_DATA: {json.dumps(str(data))}. "
        "Pass this absolute path as --data-dir to this plugin's setup.py and ledger.py commands; "
        "the hook environment is not inherited by skill shell commands. "
        f"The sizer's only persistent lessons file is {json.dumps(str(data / 'sizer-lessons.md'))}. "
        "Give that path to delegate-sizer when dispatching it."
    )
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "SessionStart", "additionalContext": context}}))


if __name__ == "__main__":
    main()
