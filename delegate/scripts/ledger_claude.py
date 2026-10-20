# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Claude Code path and model adapter for the bundled delegation ledger."""

import argparse
import os
from pathlib import Path
import sys

from ledger_core import main


if __name__ == "__main__":
    # The skill substitutes ${CLAUDE_PLUGIN_DATA} into this argument; Bash-launched
    # processes are not guaranteed to inherit it as an environment variable.
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--data-dir", type=Path)
    args, remaining = parser.parse_known_args()
    if args.data_dir is None:
        parser.error("--data-dir is required; pass the plugin data directory the skill names")
    path = Path(os.environ.get("DELEGATE_LEDGER") or args.data_dir / "ledger.jsonl")
    sys.argv = [sys.argv[0], *remaining]
    main(path, ("haiku", "sonnet", "opus", "fable"))
