#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""Host adapter for the explicitly invoked project review-settings skill."""

from __future__ import annotations

import argparse
from contextlib import redirect_stderr
from io import StringIO
import os
from pathlib import Path
import re
import sys


def _plugin_root() -> Path:
    for parent in Path(__file__).resolve().parents:
        if (parent / "scripts" / "guard_core" / "__init__.py").is_file():
            return parent
    raise RuntimeError("Guard plugin root not found")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", choices=("claude", "codex"), required=True)
    parser.add_argument("--project", type=Path, required=True)
    parser.add_argument("--session", required=True)
    parser.add_argument("arguments", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    project = args.project.expanduser().resolve()
    if not project.is_dir():
        parser.error("--project must name an existing project directory")
    if not re.fullmatch(r"[A-Za-z0-9._-]+", args.session) or ".." in args.session:
        parser.error("--session must be the current native session id")
    if not args.arguments or args.arguments[0] not in ("show", "set", "unset"):
        parser.error("use show, set <key> <value>, or unset <key>")
    if args.arguments[0] == "set" and len(args.arguments) != 3:
        parser.error("set needs exactly one key and one value")
    if args.arguments[0] == "unset" and len(args.arguments) != 2:
        parser.error("unset needs exactly one key")
    if args.arguments[0] == "show" and len(args.arguments) != 1:
        parser.error("show takes no positional arguments")

    # Config selects its host paths at import, so normalize every host input first.
    os.environ["GUARD_HOST"] = args.host
    os.environ["GUARD_PROJECT_DIR"] = str(project)
    sys.path.insert(0, str(_plugin_root() / "scripts"))
    from guard_core.cmd_settings import cmd_settings

    sys.argv = [str(_plugin_root() / "scripts" / "guard_hook.py"), "settings",
                *args.arguments, "--session", args.session]
    errors = StringIO()
    with redirect_stderr(errors):
        result = cmd_settings()
    diagnostic = errors.getvalue()
    if diagnostic:
        print(diagnostic, file=sys.stderr, end="")
        return result or 1
    return result


if __name__ == "__main__":
    raise SystemExit(main())
