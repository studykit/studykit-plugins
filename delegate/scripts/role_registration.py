"""Preserve unrelated TOML while managing the delegation role block."""

import json
import re
import tomllib

DESCRIPTION = "Used only by the `delegate` skill. Do not invoke otherwise."
BEGIN = "# BEGIN studykit delegate-sizer"
END = "# END studykit delegate-sizer"


def block(agent_path: str) -> str:
    return (
        f"{BEGIN}\n[agents.delegate-sizer]\n"
        f"description = {json.dumps(DESCRIPTION)}\n"
        f"config_file = {json.dumps(agent_path)}\n{END}\n"
    )


def update(text: str, agent_path: str, uninstall: bool) -> tuple[str, str]:
    data = tomllib.loads(text)
    role = data.get("agents", {}).get("delegate-sizer")
    matches = list(re.finditer(rf"(?m)^{re.escape(BEGIN)}\n[\s\S]*?^{re.escape(END)}\n?", text))
    owned = False
    if len(matches) == 1 and isinstance(role, dict):
        existing_path = role.get("config_file")
        owned = (
            isinstance(existing_path, str)
            and role == {"description": DESCRIPTION, "config_file": existing_path}
            and matches[0].group() == block(existing_path)
        )
    if uninstall:
        if not owned:
            return text, "skipped   sizer registration (not an unchanged managed block)"
        m = matches[0]
        return text[:m.start()] + text[m.end():], "removed   sizer registration"
    if owned:
        m = matches[0]
        return text[:m.start()] + block(agent_path) + text[m.end():], "ok        sizer registration"
    if role is not None or matches:
        raise ValueError("delegate-sizer registration exists and is not an unchanged managed block; leave it intact and resolve the conflict manually")
    # A single newline completes an unterminated line without rewriting existing content.
    separator = "" if not text or text.endswith("\n") else "\n"
    return text + separator + block(agent_path), "registered delegate-sizer"


