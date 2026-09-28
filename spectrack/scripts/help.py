#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["PyYAML"]
# ///
"""Show commands available for the active workflow project."""

from __future__ import annotations

import argparse
from pathlib import Path

from config import WorkflowConfigError, load_workflow_config
from env import workflow_project_dir_from_env
from issue.jira.client import DEPLOYMENT_CLOUD, jira_deployment_from_settings
from issue.jira.refs import JiraProviderError


def cloud_agile_available(project: Path) -> bool:
    try:
        config = load_workflow_config(project)
        return bool(
            config
            and config.issues.kind == "jira"
            and jira_deployment_from_settings(config.issues.settings) == DEPLOYMENT_CLOUD
        )
    except (WorkflowConfigError, JiraProviderError):
        return False


def help_text(project: Path) -> str:
    commands = [
        "  issue            Work with configured issues",
    ]
    if cloud_agile_available(project):
        commands.append("  agile            Manage Jira Cloud boards, sprints, backlogs, epics, and issues")
    commands.extend(
        [
            "  setup            Configure a project",
            "  config           Show the active project configuration",
            "  mustread         Find required authoring guidance",
            "  prd_path         Resolve PRD component paths",
            "  preview_context  Preview injected workflow guidance",
            "  help             Show this list or help for one command",
        ]
    )
    return "\n".join(
        [
            "usage: spectrack <command> [args...]",
            "",
            "Commands:",
            *commands,
            "",
            "Run 'spectrack <command> --help' for command options.",
        ]
    )


def main() -> int:
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--project", type=Path, default=workflow_project_dir_from_env())
    args = parser.parse_args()
    print(help_text(args.project))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
