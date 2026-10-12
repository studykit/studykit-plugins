"""Fixtures shared by the SpecTrack test modules."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

_SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "scripts"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from issue.jira import adf  # noqa: E402
from jira_cloud_support import API_TOKEN, EMAIL, adf_doc, adf_text  # noqa: E402


@pytest.fixture
def jira_cloud(monkeypatch: pytest.MonkeyPatch) -> None:
    """Give Jira Cloud requests credentials and a local Markdown<->ADF codec.

    The real codec shells out to Node and to the site's converter endpoint;
    the stand-in keeps a body's text so a test can assert on what was sent.
    """

    monkeypatch.setenv("JIRA_EMAIL", EMAIL)
    monkeypatch.setenv("JIRA_API_TOKEN", API_TOKEN)
    monkeypatch.setattr(adf, "markdown_to_adf", lambda markdown, runner=None: adf_doc(markdown))
    monkeypatch.setattr(adf, "adf_to_markdown", lambda site, document, runner=None: adf_text(document))
