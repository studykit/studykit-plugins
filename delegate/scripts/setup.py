# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Install named Codex delegation agents into durable user state."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import stat
import tempfile
import tomllib

from role_registration import update

AGENTS = ("delegate-sizer", "delegate-verifier")


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def atomic_write(path: Path, data: bytes, expected: bytes | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    mode = stat.S_IMODE(path.stat().st_mode) if path.exists() else 0o600
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        temporary.chmod(mode)
        if expected is not None and (path.read_bytes() if path.exists() else b"") != expected:
            raise RuntimeError("Codex config changed during setup; retry")
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def configure(home: Path, plugin: Path, data_dir: Path, command: str) -> dict:
    home = home.resolve()
    config = (home / "config.toml").resolve()
    managed = data_dir.resolve()
    state_path = managed / "setup.json"
    original = config.read_bytes().decode("utf-8") if config.exists() else ""
    roles = tomllib.loads(original).get("agents", {})
    state = json.loads(state_path.read_text(encoding="utf-8")) if state_path.exists() else None
    hashes = dict(state.get("agents", {})) if state else {}
    # Upgrade the original single-role setup without taking ownership of another file.
    if state and "agent_sha256" in state:
        hashes.setdefault("delegate-sizer", state["agent_sha256"])
    agents = {}
    for name in AGENTS:
        target = managed / "agents" / f"{name}.toml"
        source_bytes = (plugin / "agents" / f"{name}.toml").read_bytes()
        definition = tomllib.loads(source_bytes.decode("utf-8"))
        if definition.get("name") != name or not definition.get("developer_instructions"):
            raise ValueError(f"invalid bundled {name} definition")
        current = target.read_bytes() if target.exists() else None
        owned = current is not None and hashes.get(name) == digest(current)
        # Checking removal validates the whole marked block, not just its destination.
        without_role, _ = update(original, str(target), True, name)
        registered = (without_role != original and
                      roles.get(name, {}).get("config_file") == str(target))
        agents[name] = dict(target=target, source=source_bytes, current=current,
                            owned=owned, registered=registered, definition=definition)

    details = {name: {"agent": str(item["target"]),
                      "configured": bool(item["owned"] and item["registered"]),
                      "up_to_date": item["current"] == item["source"],
                      "model": item["definition"].get("model"),
                      "effort": item["definition"].get("model_reasoning_effort")}
               for name, item in agents.items()}
    summary = {"agents": details, **{key: details["delegate-sizer"][key]
                                    for key in ("agent", "model", "effort")}}

    if command == "status":
        return {**summary, "configured": all(d["configured"] for d in details.values()),
                "up_to_date": all(d["up_to_date"] for d in details.values())}
    if command == "remove":
        if state is None:
            return {"removed": False, "reason": "no managed setup exists"}
        revised = original
        removals = []
        for name, item in agents.items():
            if name not in hashes:
                continue
            if item["current"] is not None and not item["owned"]:
                raise ValueError(f"the installed {name} was edited; preserving it and its registration")
            present = (roles.get(name) is not None or f"# BEGIN studykit {name}" in original
                       or f"# END studykit {name}" in original)
            if present and not item["registered"]:
                raise ValueError(f"the {name} role block was edited or points elsewhere; preserving configuration")
            revised, _ = update(revised, str(item["target"]), True, name)
            removals.append(item["target"])
        if revised != original:
            atomic_write(config, revised.encode("utf-8"), original.encode("utf-8"))
        for target in removals:
            target.unlink(missing_ok=True)
        state_path.unlink()
        return {"removed": True, "history_preserved": True}

    # Validate conflicts before creating files. The state and content hash distinguish
    # our installed snapshot from a user-owned definition at the same path.
    revised = original
    for name, item in agents.items():
        revised, _ = update(revised, str(item["target"]), False, name)
        if item["current"] is not None and not item["owned"]:
            raise ValueError(f"the {name} destination is not an unchanged managed file; preserving it")
    if (config.read_bytes().decode("utf-8") if config.exists() else "") != original:
        raise RuntimeError("Codex config changed during setup; retry")
    version = json.loads((plugin / ".codex-plugin/plugin.json").read_text())["version"]
    for item in agents.values():
        atomic_write(item["target"], item["source"])
    atomic_write(state_path, (json.dumps({"agents": {name: digest(item["source"])
                                                    for name, item in agents.items()},
                                        "plugin_version": version}) + "\n").encode())
    if revised != original:
        atomic_write(config, revised.encode("utf-8"), original.encode("utf-8"))
    for detail in details.values():
        detail.update(configured=True, up_to_date=True)
    return {**summary, "configured": True, "restart_required": True}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", nargs="?", choices=("install", "status", "remove"), default="install")
    parser.add_argument("--data-dir", type=Path, default=os.environ.get("PLUGIN_DATA"),
                        help="native plugin data path provided by the SessionStart hook")
    args = parser.parse_args()
    home = Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex")
    if args.data_dir is None:
        parser.error("--data-dir is required; enable the Delegate SessionStart hook and start a new session")
    try:
        result = configure(home, Path(__file__).resolve().parents[1], args.data_dir, args.command)
    except (OSError, ValueError, TypeError, AttributeError, RuntimeError) as error:
        parser.exit(1, f"delegate setup: {error}\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
