#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# ///
"""Validate shipped skill/agent names and the remaining static agent references."""

import re
import sys
from pathlib import Path

PLUGIN_ROOT = Path(__file__).resolve().parent.parent


def problems() -> list[str]:
    out = []
    definitions = list((PLUGIN_ROOT / "skills").glob("*/SKILL.md"))
    definitions += list((PLUGIN_ROOT / "agents").glob("*.md"))
    for path in definitions:
        text = path.read_text()
        header = re.match(r"\A---\n(.*?)\n---", text, re.DOTALL)
        if header is None:
            out.append(f"{path}: missing frontmatter")
            continue
        expected = path.parent.name if path.name == "SKILL.md" else path.stem
        name = re.search(r"^name:\s*(\S+)\s*$", header.group(1), re.MULTILINE)
        if name is None or name.group(1) != expected:
            out.append(f"{path}: name must be {expected}")
        agent = re.search(r"^agent:\s*guard:([\w-]+)\s*$", header.group(1), re.MULTILINE)
        if agent and not (PLUGIN_ROOT / "agents" / f"{agent.group(1)}.md").is_file():
            out.append(f"{path}: missing guard:{agent.group(1)}")
    for name in ("korean-translator", "korean-corrector"):
        if not (PLUGIN_ROOT.parent / "global/agents" / f"{name}.md").is_file():
            out.append(f"Missing user-level definition for {name}")
        if (PLUGIN_ROOT / "agents" / f"{name}.md").exists():
            out.append(f"Guard must not shadow user-level {name}")
    return out


def main() -> int:
    errors = problems()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("check-entries: shipped names and static agent references resolve")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
