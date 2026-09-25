#!/usr/bin/env python3
"""Adapt Herdr's pane context to a resumable tmux-backed shell popup."""
from __future__ import annotations

import fcntl
import hashlib
import json
import os
from pathlib import Path
import pwd
import shlex
import shutil
import socket
import subprocess
import sys
import termios
import tomllib
import tty


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


# Nerd Font's nf-dev-tmux glyph.
DEFAULT_INDICATOR = "\ue94c"


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


def shell_server(env: dict) -> str:
    # Preserve the existing tmux socket name across the plugin rename.
    return "popup-shell-" + hashlib.sha256(env["HERDR_SOCKET_PATH"].encode()).hexdigest()[:16]


def shell_identity(env: dict, pane_id: str, terminal_id: str) -> tuple[str, str]:
    session = hashlib.sha256(f"{pane_id}\0{terminal_id}".encode()).hexdigest()[:24]
    return shell_server(env), session


def open_popup(env: dict) -> None:
    pane_id, terminal_id, cwd, label = source_pane(env)
    server, session = shell_identity(env, pane_id, terminal_id)
    call(env, "plugin.pane.open", plugin_id=env["HERDR_PLUGIN_ID"],
         entrypoint="shell", cwd=str(cwd), focus=True,
         env={"POPUP_SHELL_SERVER": server, "POPUP_SHELL_SESSION": session,
              "SHELLBOX_SOURCE_LABEL": label, "SHELLBOX_SOURCE_PANE": pane_id})


def plugin_config(env: dict) -> dict:
    directory = env.get("HERDR_PLUGIN_CONFIG_DIR")
    path = Path(directory) / "config.toml" if directory else None
    if not path or not path.is_file():
        return {}
    with path.open("rb") as stream:
        return tomllib.load(stream)


def indicator(env: dict) -> str:
    value = plugin_config(env).get("indicator", DEFAULT_INDICATOR)
    if not isinstance(value, str):
        raise ValueError("indicator must be a string")
    return value.strip()


def mark_pane(env: dict, pane_id: str) -> None:
    """Show the indicator on the pane while its shell lives."""
    icon = indicator(env)
    if not icon:
        return
    agent = call(env, "pane.get", pane_id=pane_id)["pane"].get("agent")
    source = env["HERDR_PLUGIN_ID"]
    if agent:
        # A title would hide the agent name on the pane border, so mark the name
        # instead. The agent guard drops it once a different agent takes the pane.
        call(env, "pane.report_metadata", pane_id=pane_id, source=source, agent=agent,
             display_agent=f"{icon} {agent}", clear_title=True)
    else:
        # Without an agent the border shows the metadata title.
        call(env, "pane.report_metadata", pane_id=pane_id, source=source,
             clear_display_agent=True, title=icon)


def unmark_pane(env: dict, pane_id: str) -> None:
    try:
        call(env, "pane.report_metadata", pane_id=pane_id, source=env["HERDR_PLUGIN_ID"],
             clear_display_agent=True, clear_title=True)
    except RuntimeError:
        pass  # The pane may have closed before its shell.


def session_record(env: dict, session: str) -> Path:
    return Path(env["HERDR_PLUGIN_STATE_DIR"]) / f"shell-{session}.pane"


def pane_has_shell(env: dict, pane_id: str) -> bool:
    tmux = shutil.which("tmux")
    if not tmux:
        return False
    terminal_id = call(env, "pane.get", pane_id=pane_id)["pane"]["terminal_id"]
    server, session = shell_identity(env, pane_id, terminal_id)
    return subprocess.run([tmux, "-L", server, "-f", "/dev/null", "has-session", "-t", session],
                          env=env, capture_output=True).returncode == 0


def event_pane(value: object) -> str | None:
    if isinstance(value, dict):
        if isinstance(value.get("pane_id"), str):
            return value["pane_id"]
        values = value.values()
    elif isinstance(value, list):
        values = value
    else:
        return None
    return next((found for item in values if (found := event_pane(item))), None)


def on_agent_detected(env: dict) -> None:
    pane_id = event_pane(json.loads(env.get("HERDR_PLUGIN_EVENT_JSON") or "{}"))
    if pane_id and pane_has_shell(env, pane_id):
        mark_pane(env, pane_id)


def on_pane_closed(env: dict) -> None:
    """Ask whether to end the shells a closed pane leaves running in tmux."""
    pane_id = event_pane(json.loads(env.get("HERDR_PLUGIN_EVENT_JSON") or "{}"))
    state = Path(env["HERDR_PLUGIN_STATE_DIR"])
    tmux = shutil.which("tmux")
    if not pane_id or not tmux or not state.is_dir():
        return
    server = shell_server(env)
    for record in state.glob("shell-*.pane"):
        try:
            if record.read_text().strip() != pane_id:
                continue
        except FileNotFoundError:
            continue
        # Closing a pane and its process exiting can both report the same pane;
        # whichever hook removes the record first asks.
        try:
            record.unlink()
        except FileNotFoundError:
            continue
        session = record.name[len("shell-"):-len(".pane")]
        if subprocess.run([tmux, "-L", server, "-f", "/dev/null", "has-session",
                           "-t", f"={session}"], env=env, capture_output=True).returncode:
            continue
        call(env, "plugin.pane.open", plugin_id=env["HERDR_PLUGIN_ID"], entrypoint="confirm",
             focus=True, env={"POPUP_SHELL_SERVER": server, "POPUP_SHELL_SESSION": session,
                              "SHELLBOX_SOURCE_PANE": pane_id})


def read_key() -> str:
    descriptor = sys.stdin.fileno()
    saved = termios.tcgetattr(descriptor)
    try:
        tty.setraw(descriptor, termios.TCSANOW)  # Keep a key typed before the prompt.
        return os.read(descriptor, 1).decode(errors="replace")
    finally:
        termios.tcsetattr(descriptor, termios.TCSADRAIN, saved)


def run_confirm(env: dict) -> None:
    server, session = env["POPUP_SHELL_SERVER"], env["POPUP_SHELL_SESSION"]
    if not server.startswith("popup-shell-") or not session.isalnum():
        raise ValueError("Invalid shell session")
    tmux = shutil.which("tmux")
    if not tmux:
        raise ValueError("tmux is required for persistent shell popups")
    command = [tmux, "-L", server, "-f", "/dev/null"]
    running = subprocess.run([*command, "display-message", "-p", "-t", f"={session}:",
                              "#{pane_current_command}"],
                             env=env, capture_output=True).stdout.decode().strip()
    attach = shlex.join(["tmux", "-L", server, "attach-session", "-t", session])
    print(f"Pane {env.get('SHELLBOX_SOURCE_PANE', '')} closed, but its shellbox shell"
          f" is still running{f' ({running})' if running else ''}.\n")
    print("  y    end the shell")
    print("  n    keep it; attach later with:")
    print(f"       {attach}\n")
    print("End the shell? [y/N] ", end="", flush=True)
    answer = read_key().lower()
    print(answer if answer.isprintable() else "")
    if answer == "y":
        subprocess.run([*command, "kill-session", "-t", f"={session}"], env=env, check=True)


def on_session_closed(env: dict, session: str) -> None:
    if not session.isalnum():
        raise ValueError("Invalid shell session")
    record = session_record(env, session)
    try:
        pane_id = record.read_text().strip()
    except FileNotFoundError:
        return
    record.unlink(missing_ok=True)
    unmark_pane(env, pane_id)


def watch_session_close(command: list[str], env: dict) -> None:
    # The server's global environment belongs to whichever popup started it, so
    # the hook names this plugin's context itself. A high hook index leaves the
    # user's own session-closed hooks in place.
    context = [f"{name}={env[name]}" for name in
               ("HERDR_ENV", "HERDR_SOCKET_PATH", "HERDR_PLUGIN_ID", "HERDR_PLUGIN_STATE_DIR")]
    script = shlex.join(["env", *context, sys.executable, str(Path(__file__).resolve()),
                         "closed"]).replace("#", "##")
    subprocess.run([*command, "set-hook", "-g", "session-closed[73]",
                    f"run-shell {shlex.quote(script + ' #{hook_session_name}')}"],
                   env=env, check=True)


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
    configured = plugin_config(env).get("close_key", "C-q")
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
        source = env.get("SHELLBOX_SOURCE_PANE")
        if source:
            watch_session_close(command, shell_env)
            session_record(env, session).write_text(source)
            try:
                mark_pane(env, source)
            except (OSError, RuntimeError) as error:
                print(f"shellbox: indicator unavailable: {error}", file=sys.stderr)
    os.execvpe(tmux, [*command, "attach-session", "-t", session], shell_env)


def main(env: dict, operation: str, *args: str) -> int:
    if env.get("HERDR_ENV") != "1":
        raise ValueError("Run shellbox from inside Herdr")
    if operation == "open":
        open_popup(env)
    elif operation == "panel":
        run_panel(env)
    elif operation == "confirm":
        run_confirm(env)
    elif operation == "pane-closed":
        on_pane_closed(env)
    elif operation == "agent-detected":
        on_agent_detected(env)
    elif operation == "closed" and len(args) == 1:
        on_session_closed(env, args[0])
    else:
        raise ValueError(f"Unknown operation: {operation}")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main(dict(os.environ), *(sys.argv[1:] or ["open"])))
    except (OSError, ValueError, KeyError, RuntimeError, subprocess.SubprocessError) as error:
        print(f"shellbox: {error}", file=sys.stderr)
        sys.exit(1)
