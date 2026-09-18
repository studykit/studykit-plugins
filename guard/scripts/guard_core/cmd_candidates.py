"""Compatibility notice for the retired built-in reviewer roster."""

import sys


def cmd_candidates() -> int:
    print("guard candidates: retired — use answer_review or turn_review to configure "
          "your reviewer; no built-in roster is available.", file=sys.stderr)
    return 0
