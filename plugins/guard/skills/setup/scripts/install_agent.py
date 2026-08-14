#!/usr/bin/env python3
"""Install guard's project-local Codex evidence auditor agent."""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True, help="Project root that will receive .codex/agents")
    parser.add_argument("--force", action="store_true", help="Replace an existing guard agent file")
    args = parser.parse_args()

    project = Path(args.project).expanduser().resolve()
    if not project.is_dir():
        parser.error(f"project is not a directory: {project}")
    template = Path(__file__).resolve().parents[1] / "templates" / "evidence-auditor.toml"
    target = project / ".codex" / "agents" / "guard_evidence_auditor.toml"
    if target.exists() and not args.force:
        print(f"left existing agent unchanged: {target}")
        return 0

    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(template, target)
    print(f"installed guard evidence auditor: {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
