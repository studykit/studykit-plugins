#!/usr/bin/env -S uv run --no-config --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["rich==15.0.0", "pygments>=2.19,<3"]
# ///
"""Translate Herdr invocation context into explicit navigator inputs."""
from __future__ import annotations

import fcntl
import hashlib
import json
import os
from pathlib import Path
import socket
import subprocess
import sys
import tempfile
import time
import tomllib

from popup_size import PopupSize, load_size, save_size
from layout_mode import MODES, load_layout, save_layout
from ls_colors import directory_style
import diagram_preview
from view_state import load_view, save_view


def host_config(env):
    directory = Path(env.get("XDG_CONFIG_HOME") or Path.home() / ".config") / "herdr"
    path = Path(env.get("HERDR_CONFIG_PATH") or directory / "config.toml")
    try:
        with path.open("rb") as stream:
            return tomllib.load(stream)
    except (OSError, ValueError):
        return {}


def theme_config(env):
    config = host_config(env)
    return {key: config[key] for key in ("theme", "ui") if key in config}


def kitty_graphics(env):
    config = host_config(env)
    for section in ("terminal", "experimental"):
        value = config.get(section, {}).get("kitty_graphics") if isinstance(config.get(section), dict) else None
        if isinstance(value, bool):
            return value
    return True


def chord(spec):
    """One Herdr key chord ("ctrl+s", "alt+x", "shift+a", "a") as curses input."""
    *mods, name = spec.lower().split("+") if spec != "+" else ["+"]
    name = {"space": " ", "tab": "\t", "enter": "\n"}.get(name, name)
    if len(name) != 1 or not set(mods) <= {"ctrl", "alt", "shift"}:
        return None
    if "shift" in mods:
        name = name.upper()
    if "ctrl" in mods:
        if not "a" <= name.lower() <= "z":
            return None
        name = chr(ord(name.lower()) - 96)
    return "\x1b" + name if "alt" in mods else name


def toggle_keys(env):
    """Key sequences bound to the toggle action. A popup receives all input, so
    Lens closes itself on them; Herdr runs the action for an overlay."""
    keys = host_config(env).get("keys", {})
    if not isinstance(keys, dict) or not env.get("HERDR_PLUGIN_ID"):
        return []
    prefix = keys.get("prefix", "ctrl+b")
    found = []
    for binding in keys.get("command", []) if isinstance(keys.get("command"), list) else []:
        if not isinstance(binding, dict) or binding.get("command") != env["HERDR_PLUGIN_ID"] + ".toggle":
            continue
        spec = str(binding.get("key", ""))
        parts = [prefix, spec[len("prefix+"):]] if spec.startswith("prefix+") else [spec]
        sequence = tuple(chord(part) for part in parts if isinstance(part, str))
        # A bare printable key would close Lens while typing a search.
        if sequence and None not in sequence and not (len(sequence) == 1 and sequence[0].isprintable()):
            found.append(sequence)
    return found


def cell_size(env, pane_id):
    # Popups get no pixel size from their pty, but every pane of the attached
    # client shares one cell size, so ask about the source pane instead.
    try:
        with socket.socket(socket.AF_UNIX) as connection:
            connection.settimeout(2)
            connection.connect(env["HERDR_SOCKET_PATH"])
            request = {"id": "lens-cell", "method": "pane.graphics.info", "params": {"pane_id": pane_id}}
            connection.sendall(json.dumps(request).encode() + b"\n")
            reply = b""
            while not reply.endswith(b"\n"):
                chunk = connection.recv(65536)
                if not chunk:
                    break
                reply += chunk
        result = json.loads(reply)["result"]
        size = int(result["cell_width_px"]), int(result["cell_height_px"])
        return size if min(size) > 0 else None
    except (OSError, KeyError, TypeError, ValueError):
        return None


def call(binary: str, *args: str) -> dict:
    result = subprocess.run([binary, *args], capture_output=True, text=True, timeout=15)
    if result.returncode:
        raise RuntimeError(result.stderr.strip() or result.stdout.strip() or "Herdr command failed")
    value = json.loads(result.stdout)
    if value.get("error"):
        raise RuntimeError(str(value["error"]))
    return value["result"]


def source(env: dict, binary: str) -> tuple[str, Path]:
    context = json.loads(env.get("HERDR_PLUGIN_CONTEXT_JSON") or "{}")
    if not isinstance(context, dict):
        raise ValueError("Herdr plugin context must be an object")
    pane_id = env.get("LENS_SOURCE_PANE") or context.get("focused_pane_id") or env.get("HERDR_PANE_ID")
    if not pane_id:
        raise ValueError("No focused pane was provided by Herdr")
    pane = call(binary, "pane", "get", pane_id)["pane"]
    cwd = pane.get("foreground_cwd") or pane.get("cwd")
    if not cwd or not Path(cwd).is_absolute() or not Path(cwd).is_dir():
        raise ValueError("The source pane's working directory is unavailable")
    return pane_id, Path(cwd).resolve()


def open_panel(env, binary, pane_id, root, changes, size, resume=None, placement="popup"):
    if placement not in MODES:
        raise ValueError("Unknown navigator layout")
    # Herdr 0.9.1 needs a manifest entrypoint for popup placement.
    args = ["plugin", "pane", "open", "--plugin", env["HERDR_PLUGIN_ID"],
            "--entrypoint", "popup" if placement == "popup" else "navigator", "--cwd", str(root),
            "--env", f"LENS_SOURCE_PANE={pane_id}",
            "--env", f"LENS_CHANGES={int(changes)}",
            "--env", f"LENS_WIDTH={size.width}",
            "--env", f"LENS_HEIGHT={size.height}", "--focus"]
    if placement == "popup":
        args.extend(["--width", f"{size.width}%", "--height", f"{size.height}%"])
    if resume:
        args.extend(["--env", f"LENS_RESUME={resume}"])
    if placement != "overlay":
        return call(binary, *args)
    return open_overlay(env, binary, pane_id, args, resume)


def overlay_slot(env, binary, source_pane):
    directory, socket = env.get("HERDR_PLUGIN_STATE_DIR"), env.get("HERDR_SOCKET_PATH")
    if not directory or not socket:
        return None
    context = json.loads(env.get("HERDR_PLUGIN_CONTEXT_JSON") or "{}")
    tab_id = context.get("tab_id") if isinstance(context, dict) else None
    if not tab_id:
        tab_id = call(binary, "pane", "get", source_pane)["pane"]["tab_id"]
    key = hashlib.sha256(json.dumps([socket, tab_id]).encode()).hexdigest()
    return Path(directory) / "overlays" / f"{key}.json", tab_id


def focus_overlay(env, binary, pane_id, tab_id, terminal_id=None):
    try:
        # Pane IDs can be reused after a host restart or moved to another tab.
        # Check the live terminal identity before focusing a recorded pane.
        if terminal_id is not None:
            pane = call(binary, "pane", "get", pane_id)["pane"]
            if pane.get("terminal_id") != terminal_id or pane.get("tab_id") != tab_id:
                return None
        result = call(binary, "plugin", "pane", "focus", pane_id)
    except RuntimeError as error:
        if "pane_not_found" in str(error):
            return None
        raise
    plugin_pane = result["plugin_pane"]
    if (plugin_pane["plugin_id"] != env["HERDR_PLUGIN_ID"]
            or plugin_pane["entrypoint"] != "navigator"):
        return None
    call(binary, "pane", "zoom", pane_id, "--on")
    return result


def open_overlay(env, binary, source_pane, args, resume=None):
    slot = overlay_slot(env, binary, source_pane)
    if slot is None:
        return call(binary, *args)
    path, tab_id = slot
    path.parent.mkdir(parents=True, exist_ok=True)
    # Keep this inode in place: replacing/unlinking a flock file allows two
    # actions to lock different inodes and both create a pane.
    with path.open("a+") as stream:
        fcntl.flock(stream, fcntl.LOCK_EX)
        stream.seek(0)
        try:
            record = json.loads(stream.read(8192))
        except ValueError:
            record = None
        result = None
        if (isinstance(record, dict) and isinstance(record.get("pane_id"), str)
                and isinstance(record.get("terminal_id"), str)):
            result = focus_overlay(env, binary, record["pane_id"], tab_id, record["terminal_id"])
        if result is None:
            # Also adopt a focused navigator launched before instance tracking
            # existed. A regular source pane is rejected by the plugin API.
            result = focus_overlay(env, binary, source_pane, tab_id)
        if result is None:
            result = call(binary, *args)
        elif resume:
            Path(resume).unlink(missing_ok=True)
        pane = result["plugin_pane"]["pane"]
        stream.seek(0)
        stream.truncate()
        json.dump({"pane_id": pane["pane_id"], "terminal_id": pane["terminal_id"]}, stream)
        stream.flush()
        return result


def navigator_pane(env, binary, pane_id):
    try:
        plugin_pane = call(binary, "plugin", "pane", "focus", pane_id)["plugin_pane"]
    except RuntimeError as error:
        if "not_found" in str(error):
            return False
        raise
    return plugin_pane["plugin_id"] == env["HERDR_PLUGIN_ID"] and plugin_pane["entrypoint"] == "navigator"


def close_navigator(env, binary):
    """Close this tab's Lens overlay if one is open. Returns whether it was."""
    context = json.loads(env.get("HERDR_PLUGIN_CONTEXT_JSON") or "{}")
    focused = context.get("focused_pane_id") if isinstance(context, dict) else None
    candidates = [focused] if focused else []
    slot = overlay_slot(env, binary, focused) if focused else None
    if slot is not None and slot[0].exists():
        try:
            record = json.loads(slot[0].read_text()[:8192])
            pane = call(binary, "pane", "get", record["pane_id"])["pane"]
            if pane.get("terminal_id") == record["terminal_id"] and pane.get("tab_id") == slot[1]:
                candidates.append(record["pane_id"])
        except (OSError, ValueError, KeyError, TypeError, RuntimeError):
            pass
    for pane_id in dict.fromkeys(candidates):
        if navigator_pane(env, binary, pane_id):
            call(binary, "plugin", "pane", "close", pane_id)
            return True
    return False


def resume_path(env, raw):
    path = Path(raw).resolve()
    directory = Path(env["HERDR_PLUGIN_STATE_DIR"]).resolve()
    if path.parent != directory or not path.name.startswith("resize-") or path.suffix != ".json":
        raise ValueError("Invalid navigator resume file")
    return path


def current_layout(env):
    return "overlay" if env.get("HERDR_PANE_ID") else "popup"


def change_layout(env, pane_id, placement, size, view):
    if placement not in MODES:
        raise ValueError("Unknown navigator layout")
    prepare_resize(env, pane_id, size, view, placement)
    return True


def prepare_resize(env, pane_id, size, view, placement="popup"):
    directory = Path(env["HERDR_PLUGIN_STATE_DIR"])
    directory.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix="resize-", suffix=".json", dir=directory)
    path = Path(name)
    try:
        with os.fdopen(fd, "w") as stream:
            json.dump({"pane_id": pane_id, "size": size.as_dict(), "view": view,
                       "placement": placement, "previous_pane": env.get("HERDR_PANE_ID"),
                       "previous_pid": os.getpid()}, stream)
        # The navigator exits after this returns. The helper waits for its surface
        # to close before opening the replacement with the saved view.
        helper_env = dict(env)
        # `pane current` otherwise resolves the now-closed navigator from its env.
        helper_env.pop("HERDR_PANE_ID", None)
        with (directory / "resize.log").open("ab") as log:
            subprocess.Popen([sys.executable, str(Path(__file__).resolve()), "reopen", str(path)],
                             env=helper_env, stdin=subprocess.DEVNULL, stdout=log, stderr=log,
                             start_new_session=True, close_fds=True)
    except BaseException:
        path.unlink(missing_ok=True)
        raise


def reopen(env, raw):
    path = resume_path(env, raw)
    payload = json.loads(path.read_text())
    size = PopupSize(**payload["size"])
    view, pane_id = payload["view"], payload["pane_id"]
    placement = payload.get("placement", "popup")
    previous_pane = payload.get("previous_pane")
    binary = env.get("HERDR_BIN_PATH") or "herdr"
    deadline = time.monotonic() + 5
    try:
        previous_pid = payload.get("previous_pid")
        while previous_pid:
            try:
                os.kill(previous_pid, 0)
            except ProcessLookupError:
                break
            if time.monotonic() >= deadline:
                raise RuntimeError("The previous navigator process did not exit")
            time.sleep(0.05)
        while True:
            if previous_pane:
                try:
                    call(binary, "pane", "get", previous_pane)
                except RuntimeError as error:
                    if "pane_not_found" not in str(error):
                        raise
                    previous_pane = None
                else:
                    if time.monotonic() >= deadline:
                        raise RuntimeError("The previous navigator pane did not close")
                    time.sleep(0.05)
                    continue
            current = call(binary, "pane", "current")["pane"]
            if current["pane_id"] != pane_id:
                raise RuntimeError("Layout change cancelled because focus moved to another source pane")
            try:
                open_panel(env, binary, pane_id, Path(view["root"]), view["changes"], size, path,
                           placement=placement)
                break
            except RuntimeError as error:
                if "ui_busy" not in str(error) or time.monotonic() >= deadline:
                    raise
                time.sleep(0.05)
        if env.get("HERDR_PLUGIN_CONFIG_DIR"):
            save_size(Path(env["HERDR_PLUGIN_CONFIG_DIR"]), size)
            save_layout(Path(env["HERDR_PLUGIN_CONFIG_DIR"]), placement)
    except BaseException:
        path.unlink(missing_ok=True)
        raise
    return 0


def main(env: dict, operation: str) -> int:
    if env.get("HERDR_ENV") != "1":
        raise ValueError("Run Lens from inside Herdr")
    binary = env.get("HERDR_BIN_PATH") or "herdr"
    if operation == "toggle":
        if close_navigator(env, binary):
            return 0
        operation = "browse"
    pane_id, root = source(env, binary)
    if operation in ("browse", "changes"):
        config_dir = Path(env["HERDR_PLUGIN_CONFIG_DIR"]) if env.get("HERDR_PLUGIN_CONFIG_DIR") else None
        open_panel(env, binary, pane_id, root, operation == "changes", load_size(config_dir),
                   placement=load_layout(config_dir))
    elif operation == "panel":
        import curses
        from ui import Navigator
        state_dir = Path(env["HERDR_PLUGIN_STATE_DIR"]) if env.get("HERDR_PLUGIN_STATE_DIR") else None
        config_dir = Path(env["HERDR_PLUGIN_CONFIG_DIR"]) if env.get("HERDR_PLUGIN_CONFIG_DIR") else None
        restored = None
        if env.get("LENS_RESUME"):
            path = resume_path(env, env["LENS_RESUME"])
            restored = json.loads(path.read_text())["view"]
            root = Path(restored["root"]).resolve(strict=True)
            path.unlink()
        else:
            restored = load_view(state_dir, root)
            # An explicit changes action must still open the changes view.
            if restored is not None and env.get("LENS_CHANGES") == "1":
                restored["changes"] = True
        size = PopupSize(int(env.get("LENS_WIDTH", 96)), int(env.get("LENS_HEIGHT", 92)))
        on_resize = None
        if env.get("HERDR_PLUGIN_STATE_DIR") and env.get("HERDR_PLUGIN_CONFIG_DIR"):
            on_resize = lambda chosen, view: prepare_resize(env, pane_id, chosen, view)
        navigator = Navigator(root, pane_id, env.get("LENS_CHANGES") == "1",
                              env.get("VISUAL") or env.get("EDITOR") or "", size, on_resize,
                              theme_loader=lambda: theme_config(env),
                              folder_style=directory_style(env, sys.platform),
                              on_state=(lambda view: save_view(state_dir, view)) if state_dir else None,
                              layout_loader=lambda: current_layout(env),
                              on_layout=lambda placement, chosen, view:
                                  change_layout(env, pane_id, placement, chosen, view),
                              initial_state=restored, defer_status=True,
                              diagram_tools=diagram_preview.tools(env),
                              graphics=diagram_preview.write if kitty_graphics(env) else None,
                              cell_size=lambda: cell_size(env, pane_id),
                              alignment=diagram_preview.load_alignment(config_dir),
                              close_keys=toggle_keys(env),
                              on_alignment=(lambda chosen: diagram_preview.save_alignment(config_dir, chosen))
                                  if config_dir else None)
        if restored is not None and env.get("LENS_RESUME"):
            navigator.message = "Restored view after layout change"
        try:
            curses.wrapper(navigator.run)
        finally:
            navigator.checkpoint()
    else:
        raise ValueError(f"Unknown operation: {operation}")
    return 0


if __name__ == "__main__":
    try:
        operation = sys.argv[1] if len(sys.argv) > 1 else "browse"
        env = dict(os.environ)
        if operation == "reopen" and env.get("HERDR_ENV") == "1":
            sys.exit(reopen(env, sys.argv[2]))
        sys.exit(main(env, operation))
    except (OSError, ValueError, KeyError, RuntimeError, subprocess.SubprocessError) as error:
        print(f"Lens: {error}", file=sys.stderr)
        sys.exit(1)
