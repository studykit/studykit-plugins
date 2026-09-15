"""Tests for mechanically detectable Jira wiki-markup hazards."""

from __future__ import annotations

import sys
from pathlib import Path

_PLUGIN_ROOT = Path(__file__).resolve().parent.parent
_SCRIPTS_DIR = _PLUGIN_ROOT / "scripts"
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

from jira_format_check import scan_text  # noqa: E402


def _codes(text: str) -> list[str]:
    return [finding["code"] for finding in scan_text(text)]


def test_reports_markdown_forms_that_jira_renders_as_literal_text() -> None:
    text = """## Context
1. first
- [ ] pending
> quoted
[docs](https://example.test/docs)
**bold** and `code`
| name |
| --- |
```python
print('x')
```
"""

    assert _codes(text) == [
        "markdown-heading",
        "markdown-numbered-list",
        "markdown-task-list",
        "markdown-quote",
        "markdown-link",
        "markdown-bold",
        "markdown-inline-code",
        "markdown-table-separator",
        "markdown-fenced-code",
        "markdown-fenced-code",
    ]


def test_reports_cjk_monospace_spacing_and_strikethrough_hazards() -> None:
    findings = scan_text("한글{{flag}}값\n-max-tries-\n")

    assert [(item["code"], item["severity"], item["line"]) for item in findings] == [
        ("cjk-monospace-spacing", "warning", 1),
        ("jira-strikethrough-risk", "warning", 2),
    ]


def test_ignores_markdown_looking_text_inside_jira_code_blocks() -> None:
    text = """{code:python}
## literal
`literal`
{code}
h2. Valid
"""

    assert scan_text(text) == []
