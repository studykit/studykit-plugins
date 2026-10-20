# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Codex path and model adapter for the bundled delegation ledger."""

import os
import argparse
from pathlib import Path
import sys

from ledger_core import main


if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--data-dir", type=Path, default=os.environ.get("PLUGIN_DATA"))
    args, remaining = parser.parse_known_args()
    if args.data_dir is None:
        parser.error("--data-dir is required; use the native path from the Delegate SessionStart hook")
    path = Path(os.environ.get("DELEGATE_LEDGER") or args.data_dir / "ledger.jsonl")
    sys.argv = [sys.argv[0], *remaining]
    main(path, ("gpt-6-luna", "gpt-6.1-sol", "gpt-6-astra"))
