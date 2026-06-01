#!/usr/bin/env python3
# /// script
# dependencies = ["python-frontmatter", "PyYAML"]
# ///
"""Issue body-less field mutation dispatcher.

Dispatches to the active issue backend (``github`` or ``jira``).
``--help`` reflects that backend's option surface; backend-exclusive
subcommands from the other provider are hidden. Jira's lifecycle
subcommands are listed below and appear only when the project
configures them.
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
        print(f"issue fields error: {exc}", file=err)
        return 2
    if config is None:
        print(
            "issue fields error: .workflow/config.yml was not found "
            "(run `workflow_setup.py build-config` to configure first)",
            file=err,
        )
        return 2

    try:
        backend = get_backend(config.issues.kind)
    except IssueBackendError as exc:
        print(f"issue fields error: {exc}", file=err)
        return 2

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--project",
        type=Path,
        default=workflow_project_dir_from_env(),
        help="project path",
    )
    # The Jira backend's fields parser accepts dynamic state-transition verbs
    # via a keyword argument; the GitHub backend does not. Pass them only
    # when the active backend opts in, keeping the call generic.
    if getattr(backend, "kind", "") == "jira" and hasattr(backend, "discover_state_verbs"):
        state_verbs = backend.discover_state_verbs(config)  # type: ignore[attr-defined]
        backend.add_fields_args(parser, state_verbs=state_verbs)  # type: ignore[call-arg]
    else:
        backend.add_fields_args(parser)
    args = parser.parse_args(argv)

    return backend.run_fields(
        args,
        config=config,
        runner=runner,
        stdout=out,
        stderr=err,
    )


if __name__ == "__main__":
    raise SystemExit(main())
