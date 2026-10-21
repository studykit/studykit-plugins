"""Preserve unrelated TOML while managing the delegation role block."""

import json
import re
import tomllib

DESCRIPTION = "Used only by the `delegate` skill. Do not invoke otherwise."


def block(agent_path: str, name: str = "delegate-sizer") -> str:
    return (
        f"# BEGIN studykit {name}\n[agents.{name}]\n"
        f"description = {json.dumps(DESCRIPTION)}\n"
        f"config_file = {json.dumps(agent_path)}\n# END studykit {name}\n"
    )


def update(text: str, agent_path: str, uninstall: bool, name: str = "delegate-sizer") -> tuple[str, str]:
    data = tomllib.loads(text)
    role = data.get("agents", {}).get(name)
    begin, end = f"# BEGIN studykit {name}", f"# END studykit {name}"
    matches = list(re.finditer(rf"(?m)^{re.escape(begin)}\n[\s\S]*?^{re.escape(end)}\n?", text))
    owned = False
    if len(matches) == 1 and isinstance(role, dict):
        existing_path = role.get("config_file")
        owned = (
            isinstance(existing_path, str)
            and role == {"description": DESCRIPTION, "config_file": existing_path}
            and matches[0].group() == block(existing_path, name)
        )
    if uninstall:
        if not owned:
            return text, f"skipped   {name} registration (not an unchanged managed block)"
        m = matches[0]
        return text[:m.start()] + text[m.end():], f"removed   {name} registration"
    if owned:
        m = matches[0]
        return text[:m.start()] + block(agent_path, name) + text[m.end():], f"ok        {name} registration"
    if role is not None or begin in text or end in text:
        raise ValueError(f"{name} registration exists and is not an unchanged managed block; leave it intact and resolve the conflict manually")
    # A single newline completes an unterminated line without rewriting existing content.
    separator = "" if not text or text.endswith("\n") else "\n"
    return text + separator + block(agent_path, name), f"registered {name}"


