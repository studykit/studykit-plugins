#!/usr/bin/env python3
# /// script
# dependencies = ["PyYAML"]
# ///
"""Resolve PRD component page paths for workflow knowledge providers.

The component-to-path map is the single source of truth for where PRD
pages live; the prose convention document has been retired in favour of
this script.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path

from config import (
    WorkflowConfigError,
    load_workflow_config,
)
from env import workflow_project_dir_from_env


KNOWLEDGE_PROVIDERS_WITH_PRD = {"github"}

COMPONENT_PATHS = {
    "actors": "usecases/actors.md",
    "context": "context.md",
    "usecase": "usecases/",
    "spec": "specs/",
    "nfr": "nfr/",
    "domain": "domain/",
}


class PrdPathError(ValueError):
    """Raised when a PRD path cannot be resolved."""


def normalize_prd_path(value: str | None) -> str:
    """Validate and return a normalized prd_path setting.

    Empty / missing is allowed and returns ``""`` (PRD pages sit at the
    knowledge folder root). Absolute paths and ``..`` segments are
    rejected to keep the resolved PRD base inside the knowledge folder.
    """

    if value is None:
        return ""
    stripped = value.strip()
    if not stripped:
        return ""
    candidate = Path(stripped)
    if candidate.is_absolute():
        raise PrdPathError(
            "prd_path must be a relative path under the knowledge folder; "
            f"got: {value}"
        )
    if ".." in candidate.parts:
        raise PrdPathError(
            "prd_path must not escape the knowledge folder with '..'; "
            f"got: {value}"
        )
    return stripped


@dataclass(frozen=True)
class PrdPathResolution:
    component: str
    base: Path
    relative: str

    def to_markdown(self) -> str:
        return (
            f'<prd_path component="{self.component}">\n'
            f"Base: {self.base}\n"
            f"- {self.relative}\n"
            f"</prd_path>\n"
        )


@dataclass(frozen=True)
class PrdPathListing:
    base: Path
    entries: list[tuple[str, str]]

    def to_markdown(self) -> str:
        lines = ["<prd_path>", f"Base: {self.base}"]
        for component, relative in self.entries:
            lines.append(f"- {component}: {relative}")
        lines.append("</prd_path>")
        return "\n".join(lines) + "\n"


def _resolve_base(project: Path | None = None) -> Path:
    project_dir = (project or Path.cwd()).expanduser().resolve()

    try:
        config = load_workflow_config(project_dir)
    except WorkflowConfigError as exc:
        raise PrdPathError(str(exc)) from exc

    if config is None:
        raise PrdPathError(
            f".spec-track/config.yml was not found for {project_dir}"
        )

    knowledge_kind = config.knowledge.kind
    if knowledge_kind not in KNOWLEDGE_PROVIDERS_WITH_PRD:
        choices = ", ".join(sorted(KNOWLEDGE_PROVIDERS_WITH_PRD))
        raise PrdPathError(
            f"PRD paths are not defined for knowledge provider "
            f"'{knowledge_kind}'. Supported: {choices}"
        )

    knowledge_path = config.knowledge.settings.get("path")
    if not knowledge_path:
        raise PrdPathError(
            "providers.knowledge.path is required for PRD-path resolution"
        )

    prd_subdir = normalize_prd_path(config.knowledge.settings.get("prd_path"))
    base_path = config.root / knowledge_path
    if prd_subdir:
        base_path = base_path / prd_subdir
    return base_path.resolve()


def resolve_prd_path(
    component: str,
    *,
    project: Path | None = None,
) -> PrdPathResolution:
    normalized_component = component.strip().lower()
    if normalized_component not in COMPONENT_PATHS:
        choices = ", ".join(sorted(COMPONENT_PATHS))
        raise PrdPathError(
            f"unknown PRD component: {component}. Choose one of: {choices}"
        )

    base = _resolve_base(project)
    relative = COMPONENT_PATHS[normalized_component]
    return PrdPathResolution(
        component=normalized_component,
        base=base,
        relative=relative,
    )


def resolve_all_prd_paths(
    *,
    project: Path | None = None,
) -> PrdPathListing:
    base = _resolve_base(project)
    entries = [(name, COMPONENT_PATHS[name]) for name in sorted(COMPONENT_PATHS)]
    return PrdPathListing(base=base, entries=entries)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "component",
        nargs="?",
        help="PRD component name: actors, context, usecase, spec, nfr, or domain",
    )
    parser.add_argument(
        "--list",
        dest="list_all",
        action="store_true",
        help="enumerate all components with their resolved paths",
    )
    parser.add_argument(
        "--project",
        type=Path,
        default=workflow_project_dir_from_env(),
        help="project path used to find .spec-track/config.yml",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.list_all and args.component:
        parser.error("--list cannot be combined with a component argument")
    if not args.list_all and not args.component:
        parser.error("provide a component name or pass --list")

    try:
        if args.list_all:
            output = resolve_all_prd_paths(project=args.project).to_markdown()
        else:
            output = resolve_prd_path(
                args.component,
                project=args.project,
            ).to_markdown()
    except PrdPathError as exc:
        print(f"prd_path error: {exc}", file=sys.stderr)
        return 2

    print(output, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
