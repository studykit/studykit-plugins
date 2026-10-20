# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Install a named Codex sizer from this plugin into durable user state."""

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
    target = managed / "agents/delegate-sizer.toml"
    state_path = managed / "setup.json"
    source = plugin / "agents/delegate-sizer.toml"
    source_bytes = source.read_bytes()
    definition = tomllib.loads(source_bytes.decode("utf-8"))
    if definition.get("name") != "delegate-sizer" or not definition.get("developer_instructions"):
        raise ValueError("invalid bundled delegate-sizer definition")
    original = config.read_bytes().decode("utf-8") if config.exists() else ""
    role = tomllib.loads(original).get("agents", {}).get("delegate-sizer")
    state = json.loads(state_path.read_text(encoding="utf-8")) if state_path.exists() else None
    current = target.read_bytes() if target.exists() else None
    owned = state is not None and state.get("agent_sha256") == digest(current or b"")
    registered = isinstance(role, dict) and role.get("config_file") == str(target)

    if command == "status":
        return {"configured": bool(owned and registered), "up_to_date": current == source_bytes,
                "agent": str(target), "model": definition.get("model"),
                "effort": definition.get("model_reasoning_effort")}
    if command == "remove":
        if state is None:
            return {"removed": False, "reason": "no managed setup exists"}
        if current is not None and not owned:
            raise ValueError("the installed sizer was edited; preserving it and its registration")
        if role is not None and not registered:
            raise ValueError("the sizer registration points elsewhere; preserving configuration")
        revised, message = update(original, str(target), True)
        if role is not None and revised == original:
            raise ValueError("the role block was edited; preserving configuration and the sizer")
        if revised != original:
            atomic_write(config, revised.encode("utf-8"), original.encode("utf-8"))
        target.unlink(missing_ok=True)
        state_path.unlink()
        return {"removed": True, "history_preserved": True}

    # Validate conflicts before creating files. The state and content hash distinguish
    # our installed snapshot from a user-owned definition at the same path.
    revised, message = update(original, str(target), False)
    if current is not None and not owned:
        raise ValueError("the sizer destination is not an unchanged managed file; preserving it")
    if (config.read_bytes().decode("utf-8") if config.exists() else "") != original:
        raise RuntimeError("Codex config changed during setup; retry")
    version = json.loads((plugin / ".codex-plugin/plugin.json").read_text())["version"]
    atomic_write(target, source_bytes)
    atomic_write(state_path, (json.dumps({"agent_sha256": digest(source_bytes),
                                        "plugin_version": version}) + "\n").encode())
    if revised != original:
        atomic_write(config, revised.encode("utf-8"), original.encode("utf-8"))
    return {"configured": True, "agent": str(target), "model": definition.get("model"),
            "effort": definition.get("model_reasoning_effort"), "restart_required": True}


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
