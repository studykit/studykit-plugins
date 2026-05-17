#!/usr/bin/env python3
# /// script
# dependencies = ["python-frontmatter", "PyYAML"]
# ///
"""Jira issue cache write-back entrypoint."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import TextIO

from workflow_command import CommandRunner
from workflow_config import WorkflowConfig, WorkflowConfigError, load_workflow_config
from workflow_env import workflow_project_dir_from_env
from workflow_jira_issue_provider import JiraDataCenterIssueNativeProvider
from workflow_jira_issue_refs import jira_issue_keys_from_references
from workflow_providers import ProviderContext, ProviderRequest


class JiraIssueWritebackError(RuntimeError):
    """Raised when Jira issue cache write-back cannot proceed."""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, default=workflow_project_dir_from_env(), help="project path")
    parser.add_argument("--type", default="task", help="workflow artifact type")
    parser.add_argument("--json", action="store_true", help="emit JSON")
    parser.add_argument("issues", nargs="+", help="Jira issue keys or text containing Jira issue keys")
    return parser


def writeback_cache_payload(
    *,
    project: Path,
    issues: list[str],
    artifact_type: str,
    runner: CommandRunner | None = None,
) -> dict[str, object]:
    """Write cached Jira issue projections back to Jira."""

    config = _load_jira_issue_config(project)
    issue_keys = jira_issue_keys_from_references(issues)
    if not issue_keys:
        raise JiraIssueWritebackError("no Jira issue references were found")

    provider = JiraDataCenterIssueNativeProvider(runner=runner)
    results = []
    for issue in issue_keys:
        response = provider.call(
            ProviderRequest(
                role="issue",
                kind="jira",
                operation="update",
                context=ProviderContext(project=config.root, artifact_type=artifact_type),
                payload={"issue": issue, "from_cache": True},
            )
        )
        results.append(dict(response.payload))

    return {
        "operation": "cache_writeback",
        "role": "issue",
        "kind": "jira",
        "issues": results,
    }


def main(
    argv: list[str] | None = None,
    *,
    stdout: TextIO | None = None,
    stderr: TextIO | None = None,
    runner: CommandRunner | None = None,
) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    output = stdout or sys.stdout
    errors = stderr or sys.stderr

    try:
        payload = writeback_cache_payload(
            project=args.project,
            issues=list(args.issues),
            artifact_type=args.type,
            runner=runner,
        )
    except Exception as exc:
        print(f"Jira issue write-back error: {exc}", file=errors)
        return 2

    if args.json:
        print(json.dumps(payload, indent=2, sort_keys=False), file=output)
        return 0

    for item in payload["issues"]:
        if isinstance(item, dict):
            if item.get("status") == "blocked":
                print(
                    f"{item.get('issue')} blocked: {item.get('reason')} "
                    f"reread_required={item.get('reread_required')}",
                    file=output,
                )
            else:
                print(f"{item.get('issue')} {item.get('operation')} verified={item.get('verified')}", file=output)
    return 0


def _load_jira_issue_config(project: Path) -> WorkflowConfig:
    try:
        config = load_workflow_config(project)
    except WorkflowConfigError as exc:
        raise JiraIssueWritebackError(str(exc)) from exc
    if config is None:
        raise JiraIssueWritebackError(".workflow/config.yml was not found")
    if config.issues.kind != "jira":
        raise JiraIssueWritebackError(
            f"Jira issue write-back requires configured issue provider kind jira, found {config.issues.kind}"
        )
    return config


if __name__ == "__main__":
    raise SystemExit(main())
