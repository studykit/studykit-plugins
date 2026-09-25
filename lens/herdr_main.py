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
from layout_mode import MODES, SPLITS, load_layout, save_layout
from ls_colors import directory_style
import comments
import diagram_preview
import settings as lens_settings
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


def load_icons(config_dir):
    try:
        value = json.loads((config_dir / "icons.json").read_text())
        return value["icons"] if isinstance(value, dict) and value.get("icons") in ("nerd", "plain") else "plain"
    except (OSError, ValueError, TypeError):
        return "plain"


def save_icons(config_dir, icons):
    save_choice(config_dir, "icons", icons)


def load_tree_width(config_dir):
    """The file tree width dragged with the mouse, or None for the automatic width."""
    try:
        value = json.loads((config_dir / "tree_width.json").read_text())["tree_width"]
        return value if type(value) is int and 10 <= value <= 1000 else None
    except (OSError, ValueError, TypeError, KeyError):
        return None


def save_choice(config_dir, name, value):
    config_dir.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=f".{name}-", dir=config_dir)
    try:
        with os.fdopen(fd, "w") as stream:
            json.dump({name: value}, stream)
            stream.write("\n")
        os.replace(temporary, config_dir / f"{name}.json")
    finally:
        Path(temporary).unlink(missing_ok=True)


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
        sequence = tuple(lens_settings.chord(part) for part in parts if isinstance(part, str))
        # A bare printable key would close Lens while typing a search.
        if sequence and None not in sequence and not (len(sequence) == 1 and len(sequence[0]) == 1
                                                     and sequence[0].isprintable()):
            found.append(sequence)
    return found


def cell_size(env, pane_id):
    # Popups get no pixel size from their pty, but every pane of the attached
    # client shares one cell size, so ask about the source pane instead.
    try:
        result = call(env, "pane.graphics.info", pane_id=pane_id, timeout=2)
        size = int(result["cell_width_px"]), int(result["cell_height_px"])
        return size if min(size) > 0 else None
    except (OSError, KeyError, TypeError, ValueError, RuntimeError):
        return None


def call(env: dict, method: str, /, *, timeout: float = 15, **params) -> dict:
    """One request to the Herdr socket API; an error reply raises "code: message"."""
    path = env.get("HERDR_SOCKET_PATH")
    if not path:
        raise RuntimeError("HERDR_SOCKET_PATH is not set")
    with socket.socket(socket.AF_UNIX) as connection:
        connection.settimeout(timeout)
        connection.connect(path)
        request = {"id": f"lens-{method}", "method": method, "params": params}
        connection.sendall(json.dumps(request).encode() + b"\n")
        reply = b""
        while not reply.endswith(b"\n"):
            chunk = connection.recv(65536)
            if not chunk:
                break
            reply += chunk
    value = json.loads(reply)
    if value.get("error"):
        error = value["error"]
        raise RuntimeError(f"{error.get('code')}: {error.get('message')}" if isinstance(error, dict) else str(error))
    return value["result"]


class AgentHost:
    """The agent panes comments go to, through the Herdr socket API."""

    def __init__(self, env):
        self.env = env

    def pane(self, pane_id):
        return call(self.env, "pane.get", pane_id=pane_id, timeout=5)["pane"]

    def agents(self):
        agents = call(self.env, "agent.list", timeout=5)["agents"]
        workspaces = {item["workspace_id"]: item.get("label", "")
                      for item in call(self.env, "workspace.list", timeout=5)["workspaces"]}
        tabs = {item["tab_id"]: item.get("number") for item in call(self.env, "tab.list", timeout=5)["tabs"]}
        for agent in agents:
            # Where the agent lives, for the picker's wider scopes.
            agent["place"] = f"{workspaces.get(agent.get('workspace_id'), '')} · tab {tabs.get(agent.get('tab_id'), '?')}"
        return agents

    def send(self, pane_id, text):
        # agent.prompt pastes the text as the pane's bracketed-paste mode expects, then presses
        # Enter, and refuses an agent waiting at an approval or question dialog.
        call(self.env, "agent.prompt", target=pane_id, text=text, timeout=15)


def source(env: dict) -> tuple[str, Path]:
    context = json.loads(env.get("HERDR_PLUGIN_CONTEXT_JSON") or "{}")
    if not isinstance(context, dict):
        raise ValueError("Herdr plugin context must be an object")
    pane_id = env.get("LENS_SOURCE_PANE") or context.get("focused_pane_id") or env.get("HERDR_PANE_ID")
    if not pane_id:
        raise ValueError("No focused pane was provided by Herdr")
    pane = call(env, "pane.get", pane_id=pane_id)["pane"]
    cwd = pane.get("foreground_cwd") or pane.get("cwd")
    if not cwd or not Path(cwd).is_absolute() or not Path(cwd).is_dir():
        raise ValueError("The source pane's working directory is unavailable")
    return pane_id, Path(cwd).resolve()


def open_panel(env, pane_id, root, changes, size, resume=None, placement="popup"):
    if placement not in MODES:
        raise ValueError("Unknown navigator layout")
    variables = {"LENS_SOURCE_PANE": pane_id, "LENS_CHANGES": str(int(changes)),
                 "LENS_WIDTH": str(size.width), "LENS_HEIGHT": str(size.height),
                 "LENS_PLACEMENT": placement}
    if resume:
        variables["LENS_RESUME"] = str(resume)
    # Each placement has its own manifest entrypoint; popups need theirs.
    request = {"plugin_id": env["HERDR_PLUGIN_ID"],
               "entrypoint": "popup" if placement == "popup" else "navigator",
               "cwd": str(root), "env": variables, "focus": True}
    if placement == "popup":
        request.update(width=f"{size.width}%", height=f"{size.height}%")
        return call(env, "plugin.pane.open", **request)
    if placement in SPLITS:
        # Herdr only splits to the right or down; a left half swaps afterwards.
        # open_half() adds the pane to split.
        request.update(placement="split", direction="right")
    return open_overlay(env, pane_id, request, resume, placement)


def overlay_slot(env, source_pane):
    directory, socket = env.get("HERDR_PLUGIN_STATE_DIR"), env.get("HERDR_SOCKET_PATH")
    if not directory or not socket:
        return None
    context = json.loads(env.get("HERDR_PLUGIN_CONTEXT_JSON") or "{}")
    tab_id = context.get("tab_id") if isinstance(context, dict) else None
    if not tab_id:
        tab_id = call(env, "pane.get", pane_id=source_pane)["pane"]["tab_id"]
    key = hashlib.sha256(json.dumps([socket, tab_id]).encode()).hexdigest()
    return Path(directory) / "overlays" / f"{key}.json", tab_id


def focus_overlay(env, pane_id, tab_id, terminal_id=None, zoom=True):
    try:
        # Pane IDs can be reused after a host restart or moved to another tab.
        # Check the live terminal identity before focusing a recorded pane.
        if terminal_id is not None:
            pane = call(env, "pane.get", pane_id=pane_id)["pane"]
            if pane.get("terminal_id") != terminal_id or pane.get("tab_id") != tab_id:
                return None
        result = call(env, "plugin.pane.focus", pane_id=pane_id)
    except RuntimeError as error:
        if "pane_not_found" in str(error):
            return None
        raise
    plugin_pane = result["plugin_pane"]
    if (plugin_pane["plugin_id"] != env["HERDR_PLUGIN_ID"]
            or plugin_pane["entrypoint"] != "navigator"):
        return None
    if zoom:
        call(env, "pane.zoom", pane_id=pane_id, mode="on")
    return result


def open_overlay(env, source_pane, request, resume=None, placement="overlay"):
    slot = overlay_slot(env, source_pane)
    if slot is None:
        return open_half(env, source_pane, request, placement) if placement in SPLITS \
            else call(env, "plugin.pane.open", **request)
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
            # Records from before split placements existed are overlays.
            kept = record.get("placement", "overlay")
            result = focus_overlay(env, record["pane_id"], tab_id, record["terminal_id"],
                                   zoom=kept == "overlay")
            if result is not None:
                placement = kept
        if result is None:
            # Also adopt a focused navigator launched before instance tracking
            # existed. A regular source pane is rejected by the plugin API.
            result = focus_overlay(env, source_pane, tab_id, zoom=placement == "overlay")
        if result is None:
            result = open_half(env, source_pane, request, placement) if placement in SPLITS \
                else call(env, "plugin.pane.open", **request)
        elif resume:
            Path(resume).unlink(missing_ok=True)
        pane = result["plugin_pane"]["pane"]
        stream.seek(0)
        stream.truncate()
        json.dump({"pane_id": pane["pane_id"], "terminal_id": pane["terminal_id"],
                   "placement": placement}, stream)
        stream.flush()
        return result


def leaves(node):
    """Pane IDs of a layout.export tree, first to last."""
    if node["type"] == "pane":
        return [node["pane_id"]]
    return leaves(node["first"]) + leaves(node["second"])


def rebuild(env, node, tab_id):
    """Move panes back into the slot held by the tree's first pane, recreating its splits."""
    if node["type"] == "pane":
        return
    call(env, "pane.move", pane_id=leaves(node["second"])[0],
         destination={"type": "tab", "tab_id": tab_id, "split": node["direction"],
                      "target_pane_id": leaves(node["first"])[0], "ratio": node["ratio"]})
    rebuild(env, node["first"], tab_id)
    rebuild(env, node["second"], tab_id)


def open_half(env, source_pane, request, placement):
    """Open the navigator over the left or right half of the whole tab.

    Herdr splits single panes only, and layout.apply restarts every process. To
    split the tab itself, every pane but one waits in a temporary tab, the
    navigator splits the one left, and the others return with their original
    splits and ratios beside it. Closing the navigator then removes that outer
    split and restores the tab by itself."""
    layout = call(env, "layout.export", pane_id=source_pane)["layout"]
    if layout.get("zoomed"):
        # Herdr refuses to move panes out of a zoomed tab.
        call(env, "pane.zoom", pane_id=source_pane, mode="off")
    tree = layout["root"]
    anchor, *waiting = leaves(tree)
    temporary = None
    try:
        for pane in waiting:
            if temporary is None:
                moved = call(env, "pane.move", pane_id=pane,
                             destination={"type": "new_tab", "workspace_id": layout["workspace_id"]})
                temporary, parked = moved["move_result"]["pane"]["tab_id"], pane
            else:
                call(env, "pane.move", pane_id=pane, destination={
                    "type": "tab", "tab_id": temporary, "split": "right", "target_pane_id": parked})
        result = call(env, "plugin.pane.open", **request, target_pane_id=anchor)
        created = result["plugin_pane"]["pane"]["pane_id"]
        if placement == "left":
            call(env, "pane.swap", source_pane_id=created, target_pane_id=anchor)
    finally:
        # Also on failure: the panes must never stay in the temporary tab.
        if waiting:
            rebuild(env, tree, layout["tab_id"])
    call(env, "plugin.pane.focus", pane_id=created)
    return result


def navigator_pane(env, pane_id):
    try:
        plugin_pane = call(env, "plugin.pane.focus", pane_id=pane_id)["plugin_pane"]
    except RuntimeError as error:
        if "not_found" in str(error):
            return False
        raise
    return plugin_pane["plugin_id"] == env["HERDR_PLUGIN_ID"] and plugin_pane["entrypoint"] == "navigator"


def close_navigator(env):
    """Close this tab's Lens overlay if one is open. Returns whether it was."""
    context = json.loads(env.get("HERDR_PLUGIN_CONTEXT_JSON") or "{}")
    focused = context.get("focused_pane_id") if isinstance(context, dict) else None
    candidates = [focused] if focused else []
    slot = overlay_slot(env, focused) if focused else None
    if slot is not None and slot[0].exists():
        try:
            record = json.loads(slot[0].read_text()[:8192])
            pane = call(env, "pane.get", pane_id=record["pane_id"])["pane"]
            if pane.get("terminal_id") == record["terminal_id"] and pane.get("tab_id") == slot[1]:
                candidates.append(record["pane_id"])
        except (OSError, ValueError, KeyError, TypeError, RuntimeError):
            pass
    for pane_id in dict.fromkeys(candidates):
        if navigator_pane(env, pane_id):
            call(env, "plugin.pane.close", pane_id=pane_id)
            return True
    return False


def resume_path(env, raw):
    path = Path(raw).resolve()
    directory = Path(env["HERDR_PLUGIN_STATE_DIR"]).resolve()
    if path.parent != directory or not path.name.startswith("resize-") or path.suffix != ".json":
        raise ValueError("Invalid navigator resume file")
    return path


def current_layout(env):
    if not env.get("HERDR_PANE_ID"):
        return "popup"  # Popups have no pane ID.
    placement = env.get("LENS_PLACEMENT")
    return placement if placement in MODES and placement != "popup" else "overlay"


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
        # The helper must not act as the navigator that is about to close.
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
                    call(env, "pane.get", pane_id=previous_pane)
                except RuntimeError as error:
                    if "pane_not_found" not in str(error):
                        raise
                    previous_pane = None
                else:
                    if time.monotonic() >= deadline:
                        raise RuntimeError("The previous navigator pane did not close")
                    time.sleep(0.05)
                    continue
            current = call(env, "pane.current")["pane"]
            if current["pane_id"] != pane_id:
                raise RuntimeError("Layout change cancelled because focus moved to another source pane")
            try:
                open_panel(env, pane_id, Path(view["root"]), view["changes"], size, path,
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
    if operation == "toggle":
        if close_navigator(env):
            return 0
        operation = "browse"
    pane_id, root = source(env)
    if operation in ("browse", "changes"):
        config_dir = Path(env["HERDR_PLUGIN_CONFIG_DIR"]) if env.get("HERDR_PLUGIN_CONFIG_DIR") else None
        open_panel(env, pane_id, root, operation == "changes", load_size(config_dir),
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
        environment_editor = env.get("VISUAL") or env.get("EDITOR") or ""
        host = AgentHost(env)
        try:
            source_terminal = host.pane(pane_id).get("terminal_id", "")
        except (OSError, ValueError, KeyError, RuntimeError):
            source_terminal = ""
        navigator = Navigator(root, pane_id, env.get("LENS_CHANGES") == "1",
                              environment_editor, size, on_resize,
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
                              icons=load_icons(config_dir) if config_dir else "plain",
                              on_icons=(lambda chosen: save_icons(config_dir, chosen)) if config_dir else None,
                              tree_width=load_tree_width(config_dir) if config_dir else None,
                              on_tree_width=(lambda chosen: save_choice(config_dir, "tree_width", chosen))
                                  if config_dir else None,
                              settings_loader=lambda: lens_settings.load(lens_settings.location(env)),
                              settings_file=lambda: lens_settings.ensure(lens_settings.location(env)),
                              on_alignment=(lambda chosen: diagram_preview.save_alignment(config_dir, chosen))
                                  if config_dir else None,
                              comment_store=comments.Store(state_dir) if state_dir else None,
                              agent_host=host, source_terminal=source_terminal)
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
