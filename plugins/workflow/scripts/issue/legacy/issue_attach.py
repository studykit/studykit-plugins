#!/usr/bin/env python3
# /// script
# dependencies = ["python-frontmatter", "PyYAML"]
# ///
"""Issue attachment upload dispatcher.

Attachments are a Jira-only capability: the GitHub issue backend has no
equivalent REST surface, so this dispatcher refuses any non-Jira provider
rather than exposing a verb the active backend cannot honor. When the
provider is Jira it resolves the backend and delegates to its
``run_attach`` driver (``add_attach_args`` / ``run_attach`` live on the
Jira backend only, not on the shared ``IssueBackend`` protocol).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import TextIO

from workflow_command import CommandRunner
from workflow_config import WorkflowConfigError, load_workflow_config
from workflow_env import workflow_project_dir_from_env
from issue.backend import IssueBackendError, get_backend


def main(
    argv: list[str] | None = None,
    *,
    stdout: TextIO | None = None,
    stderr: TextIO | None = None,
    runner: CommandRunner | None = None,
) -> int:
    out = stdout or sys.stdout
    err = stderr or sys.stderr

    base_parser = argparse.ArgumentParser(add_help=False)
    base_parser.add_argument(
        "--project",
        type=Path,
        default=workflow_project_dir_from_env(),
    )
    base_known, _ = base_parser.parse_known_args(argv)
    project = base_known.project or workflow_project_dir_from_env()

    try:
        config = load_workflow_config(project)
    except WorkflowConfigError as exc:
        print(f"issue attach error: {exc}", file=err)
        return 2
    if config is None:
        print(
            "issue attach error: .workflow/config.yml was not found "
            "(run `workflow_setup.py build-config` to configure first)",
            file=err,
        )
        return 2

    if config.issues.kind != "jira":
        print(
            "issue attach error: attachments are only supported by the Jira "
            f"issue provider (configured provider: {config.issues.kind})",
            file=err,
        )
        return 2

    try:
        backend = get_backend("jira")
    except IssueBackendError as exc:
        print(f"issue attach error: {exc}", file=err)
        return 2

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--project",
        type=Path,
        default=workflow_project_dir_from_env(),
        help="project path",
    )
    backend.add_attach_args(parser)
    args = parser.parse_args(argv)

    return backend.run_attach(
        args,
        config=config,
        runner=runner,
        stdout=out,
        stderr=err,
    )


if __name__ == "__main__":
    raise SystemExit(main())
