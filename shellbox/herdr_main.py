#!/usr/bin/env python3
"""Adapt Herdr's pane context to a resumable tmux-backed shell popup."""
from __future__ import annotations

import fcntl
import hashlib
import json
import os
from pathlib import Path
import pwd
import shutil
import socket
import subprocess
import sys
import tomllib


def call(env: dict, method: str, /, **params) -> dict:
    path = env.get("HERDR_SOCKET_PATH")
    if not path:
        raise ValueError("HERDR_SOCKET_PATH is not set")
    with socket.socket(socket.AF_UNIX) as connection:
        connection.settimeout(15)
        connection.connect(path)
        connection.sendall(json.dumps({"id": "shellbox", "method": method,
                                       "params": params}).encode() + b"\n")
        reply = b""
        while not reply.endswith(b"\n"):
            chunk = connection.recv(65536)
            if not chunk:
                break
            reply += chunk
    value = json.loads(reply)
    if value.get("error"):
        error = value["error"]
        raise RuntimeError(f"{error.get('code')}: {error.get('message')}"
                           if isinstance(error, dict) else str(error))
    return value["result"]


def source_pane(env: dict) -> tuple[str, str, Path, str]:
    context = json.loads(env.get("HERDR_PLUGIN_CONTEXT_JSON") or "{}")
    if not isinstance(context, dict):
        raise ValueError("Herdr plugin context must be an object")
    pane_id = context.get("focused_pane_id") or env.get("HERDR_PANE_ID")
    if not pane_id:
        raise ValueError("No focused pane was provided by Herdr")
    pane = call(env, "pane.get", pane_id=pane_id)["pane"]
    cwd = pane.get("foreground_cwd") or pane.get("cwd")
    if not cwd or not Path(cwd).is_absolute() or not Path(cwd).is_dir():
        raise ValueError("The source pane's working directory is unavailable")
    title = pane.get("terminal_title_stripped") or pane.get("agent") or Path(cwd).name
    # Terminal titles are controlled by the source process. Keep them printable
    # and short before placing them in a tmux status option.
    title = " ".join("".join(char if char.isprintable() and char != "#" else " "
                     for char in str(title)).split())[:40]
    label = f"Herdr {pane_id} · {title}" if title else f"Herdr {pane_id}"
    return pane_id, pane["terminal_id"], Path(cwd).resolve(), label


def shell_identity(env: dict, pane_id: str, terminal_id: str) -> tuple[str, str]:
    server = hashlib.sha256(env["HERDR_SOCKET_PATH"].encode()).hexdigest()[:16]
    session = hashlib.sha256(f"{pane_id}\0{terminal_id}".encode()).hexdigest()[:24]
    # Preserve the existing tmux socket name across the plugin rename.
    return f"popup-shell-{server}", session


def open_popup(env: dict) -> None:
    pane_id, terminal_id, cwd, label = source_pane(env)
    server, session = shell_identity(env, pane_id, terminal_id)
    call(env, "plugin.pane.open", plugin_id=env["HERDR_PLUGIN_ID"],
         entrypoint="shell", cwd=str(cwd), focus=True,
         env={"POPUP_SHELL_SERVER": server, "POPUP_SHELL_SESSION": session,
              "SHELLBOX_SOURCE_LABEL": label})


def tmux_config(env: dict) -> Path | None:
    home = Path(env.get("HOME") or Path.home())
    candidates = (home / ".tmux.conf",
                  Path(env.get("XDG_CONFIG_HOME") or home / ".config") / "tmux" / "tmux.conf")
    return next((path for path in candidates if path.is_file()), None)


def tmux_key(spec: str) -> str:
    parts = spec.lower().split("+")
    key = parts.pop()
    if not key or any(part not in ("ctrl", "alt", "shift") for part in parts):
        raise ValueError(f"Unsupported Herdr shortcut key: {spec}")
    named = {"escape": "Escape", "space": "Space", "enter": "Enter",
             "backspace": "BSpace", "tab": "Tab"}
    if len(key) != 1 and key not in named:
        raise ValueError(f"Unsupported Herdr shortcut key: {spec}")
    value = named.get(key, key.upper() if "shift" in parts else key)
    if "ctrl" in parts:
        value = "C-" + value
    if "alt" in parts:
        value = "M-" + value
    return value


def toggle_chord(env: dict) -> tuple[str, ...] | None:
    home = Path(env.get("HOME") or Path.home())
    config_dir = Path(env.get("XDG_CONFIG_HOME") or home / ".config") / "herdr"
    path = Path(env.get("HERDR_CONFIG_PATH") or config_dir / "config.toml")
    if not path.is_file():
        return None
    with path.open("rb") as stream:
        host = tomllib.load(stream)
    keys = host.get("keys", {})
    if not isinstance(keys, dict):
        return None
    bindings = keys.get("command", [])
    if not isinstance(bindings, list):
        return None
    command = env["HERDR_PLUGIN_ID"] + ".open"
    for binding in bindings:
        if not isinstance(binding, dict) or binding.get("command") != command:
            continue
        spec = binding.get("key")
        if not isinstance(spec, str):
            continue
        if spec.startswith("prefix+"):
            return tmux_key(keys.get("prefix", "ctrl+b")), tmux_key(spec[7:])
        return (tmux_key(spec),)
    return None


def apply_toggle_binding(command: list[str], env: dict) -> None:
    wanted = toggle_chord(env)
    raw = subprocess.run([*command, "show-option", "-gqv", "@popup_shell_toggle_binding"],
                         env=env, capture_output=True, check=True).stdout.decode().strip()
    try:
        previous = tuple(json.loads(raw)) if raw else None
    except (TypeError, ValueError):
        previous = None
    if previous and previous != wanted:
        subprocess.run([*command, "unbind-key", "-q", "-T", "root", previous[0]],
                       env=env, check=True)
        if len(previous) == 2:
            subprocess.run([*command, "unbind-key", "-q", "-T", "popup-shell-toggle", previous[1]],
                           env=env, check=True)
    if wanted:
        action = ["detach-client"] if len(wanted) == 1 else ["switch-client", "-T", "popup-shell-toggle"]
        subprocess.run([*command, "bind-key", "-T", "root", wanted[0], *action],
                       env=env, check=True)
        if len(wanted) == 2:
            subprocess.run([*command, "bind-key", "-T", "popup-shell-toggle", wanted[1],
                            "detach-client"], env=env, check=True)
    subprocess.run([*command, "set-option", "-g", "@popup_shell_toggle_binding",
                    json.dumps(wanted)], env=env, check=True)


def close_binding(env: dict) -> tuple[str, str] | None:
    directory = env.get("HERDR_PLUGIN_CONFIG_DIR")
    path = Path(directory) / "config.toml" if directory else None
    if path and path.is_file():
        with path.open("rb") as stream:
            configured = tomllib.load(stream).get("close_key", "C-q")
    else:
        configured = "C-q"
    if not isinstance(configured, str):
        raise ValueError("close_key must be a tmux key string")
    if configured.lower() == "none":
        return None
    table, key = ("prefix", configured[7:]) if configured.startswith("prefix+") else ("root", configured)
    if not key or key.startswith("-") or any(character.isspace() for character in key) or len(key) > 64:
        raise ValueError("close_key must be a valid tmux key, such as C-q or prefix+q")
    return table, key


def apply_close_binding(command: list[str], env: dict) -> None:
    wanted = close_binding(env)
    saved = subprocess.run([*command, "show-option", "-gqv", "@popup_shell_close_binding"],
                           env=env, capture_output=True, check=True).stdout.decode().strip()
    if saved in ("", "none"):
        previous = None  # An unset marker may belong to a user-configured tmux server.
    else:
        table, _, key = saved.partition(":")
        previous = (table, key) if table in ("root", "prefix") and key else None
    if previous and previous != wanted:
        subprocess.run([*command, "unbind-key", "-q", "-T", *previous], env=env, check=True)
    if wanted:
        subprocess.run([*command, "bind-key", "-T", *wanted, "detach-client"],
                       env=env, check=True)
    marker = f"{wanted[0]}:{wanted[1]}" if wanted else "none"
    subprocess.run([*command, "set-option", "-g", "@popup_shell_close_binding", marker],
                   env=env, check=True)


def show_source_label(command: list[str], env: dict, session: str) -> None:
    label = env.get("SHELLBOX_SOURCE_LABEL")
    if not label:
        return
    subprocess.run([*command, "set-option", "-t", session, "@shellbox_source_label", label],
                   env=env, check=True)
    subprocess.run([*command, "set-option", "-t", session, "status-left",
                    "#{@shellbox_source_label} "], env=env, check=True)
    subprocess.run([*command, "set-option", "-t", session, "status-left-length", "70"],
                   env=env, check=True)


def run_panel(env: dict) -> None:
    server, session = env["POPUP_SHELL_SERVER"], env["POPUP_SHELL_SESSION"]
    if not server.startswith("popup-shell-") or not session.isalnum():
        raise ValueError("Invalid shell session")
    tmux = shutil.which("tmux")
    if not tmux:
        raise ValueError("tmux is required for persistent shell popups")
    candidate = env.get("SHELL") or pwd.getpwuid(os.getuid()).pw_shell or "/bin/sh"
    shell = shutil.which(candidate)
    if not shell or not os.access(shell, os.X_OK):
        raise ValueError(f"Shell is not executable: {candidate}")
    command = [tmux, "-L", server, "-f", "/dev/null"]
    shell_env = dict(env)
    shell_env.pop("TMUX", None)
    shell_env.pop("TMUX_PANE", None)
    shell_env["PWD"] = os.getcwd()
    state = Path(env["HERDR_PLUGIN_STATE_DIR"])
    state.mkdir(parents=True, exist_ok=True)
    with (state / f"shell-{session}.lock").open("a+") as stream:
        fcntl.flock(stream, fcntl.LOCK_EX)
        exists = subprocess.run([*command, "has-session", "-t", session],
                                env=shell_env, capture_output=True).returncode == 0
        if not exists:
            subprocess.run([*command, "new-session", "-d", "-s", session,
                            "-c", os.getcwd(), shell, "-i"], env=shell_env, check=True)
        config = tmux_config(env)
        if config:
            revision = f"{config.resolve()}:{config.stat().st_mtime_ns}"
            loaded = subprocess.run([*command, "show-option", "-gqv", "@popup_shell_config"],
                                    env=shell_env, capture_output=True, check=True)
            if loaded.stdout.decode().strip() != revision:
                subprocess.run([*command, "source-file", str(config)], env=shell_env, check=True)
                subprocess.run([*command, "set-option", "-g", "@popup_shell_config", revision],
                               env=shell_env, check=True)
        apply_close_binding(command, shell_env)
        apply_toggle_binding(command, shell_env)
        show_source_label(command, shell_env, session)
    os.execvpe(tmux, [*command, "attach-session", "-t", session], shell_env)


def main(env: dict, operation: str) -> int:
    if env.get("HERDR_ENV") != "1":
        raise ValueError("Run shellbox from inside Herdr")
    if operation == "open":
        open_popup(env)
    elif operation == "panel":
        run_panel(env)
    else:
        raise ValueError(f"Unknown operation: {operation}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(dict(os.environ), sys.argv[1] if len(sys.argv) > 1 else "open"))
    except (OSError, ValueError, KeyError, RuntimeError, subprocess.SubprocessError) as error:
        print(f"shellbox: {error}", file=sys.stderr)
        sys.exit(1)
