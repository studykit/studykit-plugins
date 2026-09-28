#!/usr/bin/env python3
"""Jira Cloud body conversion between Markdown and ADF.

Jira Cloud stores issue descriptions and comments as Atlassian Document Format
(ADF), while the cache and every authored draft stay Markdown. Writes go
through Atlassian's own editor transformer (a bundled Node script); reads go
through the site's Confluence content-body converter, which renders ADF as
Markdown. That converter's ``markdown`` representation is not in Atlassian's
published API reference, so a site without Confluence, or a future change to
that endpoint, surfaces here as a conversion error rather than a silent
mis-render.
"""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import tempfile
from collections.abc import Mapping
from pathlib import Path
from typing import Any

from command import CommandRunner, WorkflowCommandError, run_command
from issue.jira.client import JiraDataCenterSite, jira_send_json
from issue.jira.refs import JiraProviderError

_PACKAGE_DIR = Path(__file__).resolve().parent / "md_to_adf"
_PACKAGE_FILES = ("package.json", "package-lock.json", "md_to_adf.cjs")
_CONVERT_TO_MARKDOWN_PATH = "/wiki/rest/api/contentbody/convert/markdown"


def is_adf_document(value: Any) -> bool:
    return isinstance(value, Mapping) and value.get("type") == "doc"


def adf_to_markdown(
    site: JiraDataCenterSite,
    document: Mapping[str, Any],
    *,
    runner: CommandRunner | None = None,
) -> str:
    """Render one ADF document as Markdown through the site's converter."""

    if not document.get("content"):
        return ""
    result = jira_send_json(
        site,
        "POST",
        _CONVERT_TO_MARKDOWN_PATH,
        {"value": json.dumps(document, ensure_ascii=False), "representation": "atlas_doc_format"},
        runner=runner,
    )
    value = result.get("value") if isinstance(result, Mapping) else None
    if not isinstance(value, str):
        raise JiraProviderError("Jira Cloud ADF-to-Markdown conversion returned no value")
    return value


def markdown_to_adf(markdown: str, *, runner: CommandRunner | None = None) -> dict[str, Any]:
    """Convert Markdown to an ADF document with Atlassian's editor transformer."""

    package_dir = ensure_converter_installed(runner=runner)
    try:
        completed = run_command(
            ("node", str(package_dir / "md_to_adf.cjs")),
            input_text=markdown,
            runner=runner,
        )
    except WorkflowCommandError as exc:
        raise JiraProviderError(f"Markdown-to-ADF conversion failed: {exc}") from exc
    try:
        document = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        raise JiraProviderError(f"Markdown-to-ADF converter returned invalid JSON: {exc}") from exc
    if not is_adf_document(document):
        raise JiraProviderError("Markdown-to-ADF converter did not return an ADF document")
    return document


def ensure_converter_installed(*, runner: CommandRunner | None = None) -> Path:
    """Install the Node converter once per package revision and return its directory.

    The install lives in the user cache rather than the plugin tree: the plugin
    directory may be a read-only versioned install, and keying the directory on
    the package files' hash lets a plugin upgrade pick up new pins without
    clobbering a concurrent session still using the old ones.
    """

    target = converter_cache_root() / _package_digest()
    if (target / "node_modules" / "@atlaskit" / "editor-markdown-transformer").is_dir():
        return target
    if shutil.which("node") is None or shutil.which("npm") is None:
        raise JiraProviderError("Jira Cloud Markdown-to-ADF conversion requires Node.js and npm on PATH")
    target.parent.mkdir(parents=True, exist_ok=True)
    staging = Path(tempfile.mkdtemp(prefix=f".{target.name}-", dir=target.parent))
    try:
        for name in _PACKAGE_FILES:
            shutil.copy2(_PACKAGE_DIR / name, staging / name)
        try:
            run_command(
                ("npm", "ci", "--omit=dev", "--no-audit", "--no-fund", "--silent"),
                cwd=staging,
                runner=runner,
            )
        except WorkflowCommandError as exc:
            raise JiraProviderError(f"could not install the Markdown-to-ADF converter: {exc}") from exc
        try:
            staging.rename(target)
        except OSError:
            # Another session finished the same install first.
            if not target.is_dir():
                raise
    finally:
        if staging.exists():
            shutil.rmtree(staging, ignore_errors=True)
    return target


def converter_cache_root() -> Path:
    base = os.environ.get("XDG_CACHE_HOME") or str(Path.home() / ".cache")
    return Path(base).expanduser() / "spectrack" / "md-to-adf"


def _package_digest() -> str:
    digest = hashlib.sha256()
    for name in _PACKAGE_FILES:
        digest.update(name.encode())
        digest.update((_PACKAGE_DIR / name).read_bytes())
    return digest.hexdigest()[:16]
