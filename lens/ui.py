"""Keyboard and mouse file navigation in a Herdr terminal surface."""
from __future__ import annotations

import curses
from concurrent.futures import Future
import os
from pathlib import Path
import subprocess
from threading import Thread
import unicodedata

from core import Row, apply_status, checked_path, editor_command, preview, read_status, rows, scan
from diff_tool import comparison
from popup_size import PopupSize, PRESETS
from view_state import normalize as normalize_view
import command_line
import settings
import markdown_preview
import diagram_preview
import syntax_preview
import terminal_input
from theme_colors import resolve as resolve_theme, terminal_color


def clean(text: str) -> str:
    # Nerd Font glyphs occupy Unicode's private-use category (Co), which Python
    # excludes from isprintable() even though terminals can render them safely.
    return "".join(char if char.isprintable() or unicodedata.category(char) == "Co" else " "
                   for char in text.expandtabs(4))


def put(screen, y: int, x: int, text: str, width: int, style: int = 0):
    height, columns = screen.getmaxyx()
    if y < 0 or y >= height or x < 0 or x >= columns:
        return
    available = min(width, columns - x - 1)
    clipped = []
    used = 0
    for char in clean(text):
        size = 0 if unicodedata.combining(char) else 2 if unicodedata.east_asian_width(char) in "WF" else 1
        if used + size > available:
            break
        clipped.append(char)
        used += size
    try:
        screen.addstr(y, x, "".join(clipped), style)
    except curses.error:
        pass  # Resizes can race the draw, particularly at the bottom right.


def cells(text: str) -> int:
    return sum(0 if unicodedata.combining(char) else 2 if unicodedata.east_asian_width(char) in "WF" else 1
               for char in text)


def band(screen, y, x, text, width, style=0):
    put(screen, y, x, " " * max(0, width), width, style)
    put(screen, y, x, text, width, style)


# Tree status marks. Nerd Font glyphs need a patched font, so plain text is the default.
ICONS = {
    "plain": {"project": "", "changes": "", "hidden": "", "shown": "+ignored",
              "loading": "Git…", "error": "No Git status"},
    "nerd": {"project": "\U000f0645", "changes": "\uf47f", "hidden": "\U000f0209", "shown": "\U000f0208",
             "loading": "\uf46a Git…", "error": "\uf071 No Git status"},
}


def theme(palette=None, folder_style=None) -> dict[str, int]:
    palette = palette or resolve_theme()
    styles = {"active": curses.A_BOLD, "header": curses.A_REVERSE | curses.A_BOLD,
              "selected": curses.A_REVERSE | curses.A_BOLD, "inactive": curses.A_DIM,
              "muted": curses.A_DIM, "hunk": curses.A_BOLD}
    if not curses.has_colors():
        return styles
    curses.start_color()
    default_supported = True
    try:
        curses.use_default_colors()
    except curses.error:
        default_supported = False
    p = palette
    palettes = {
        "base": (p["text"], p["panel_bg"]), "muted": (p["subtext0"], p["panel_bg"]),
        "active": (p["accent"], p["panel_bg"]), "header": (p["accent"], p["selection_bg"]),
        "inactive": (p["subtext0"], p["active_row_bg"]), "selected": (p["text"], p["selection_bg"]),
        "surface": (p["text"], p["active_row_bg"]), "folder": (p["text"], p["panel_bg"]),
        "hunk": (p["mauve"], p["surface_dim"]), "removed": (p["red"], p["panel_bg"]),
        "added": (p["green"], p["panel_bg"]), "gutter": (p["overlay0"], p["panel_bg"]),
    }
    if folder_style is not None:
        palettes["folder"] = (folder_style.foreground,
                              folder_style.background if folder_style.background >= 0 else p["panel_bg"])
    for number, (name, colors) in enumerate(palettes.items(), 1):
        if number >= curses.COLOR_PAIRS:
            break
        foreground = terminal_color(colors[0], curses.COLORS, default_supported)
        background = terminal_color(colors[1], curses.COLORS, default_supported, background=True)
        curses.init_pair(number, foreground, background)
        styles[name] = curses.color_pair(number)
    if folder_style is not None and "folder" in styles:
        if folder_style.bold:
            styles["folder"] |= curses.A_BOLD
        if folder_style.italic:
            styles["folder"] |= getattr(curses, "A_ITALIC", 0)
        if folder_style.underline:
            styles["folder"] |= curses.A_UNDERLINE
    if p["selection_bg"] == p["panel_bg"]:
        styles["selected"] |= curses.A_REVERSE
        styles["header"] |= curses.A_REVERSE
    return styles


class Navigator:
    def __init__(self, root: Path, pane_id: str, changes: bool, editor: str,
                 size: PopupSize = PopupSize(), on_resize=None, theme_loader=None,
                 folder_style=None, on_state=None, layout_loader=None, on_layout=None,
                 initial_state=None, defer_status=False, diagram_tools=None, graphics=None,
                 cell_size=None, alignment="center", on_alignment=None, close_keys=(),
                 icons="plain", on_icons=None, settings_loader=None, settings_file=None):
        initial_state = normalize_view(initial_state, root)
        self.root, self.pane_id, self.editor = root, pane_id, editor
        self.environment_editor = editor
        self.settings_loader, self.settings_file = settings_loader, settings_file
        self.bindings = {}  # From config.toml [keys]: key -> action name or ":command".
        self.settings_errors = ""
        self.changes = changes
        self.include_ignored = initial_state["include_ignored"] if initial_state else False
        self.query = ""
        self.searching = False
        self.search_before = ""
        self.root_draft = None
        self.root_cursor = 0
        self.root_error = ""
        self.expanded: set[str] = set()
        self.selected = self.scroll = self.preview_scroll = self.horizontal = 0
        self.preview_focus = False
        self.active = ""
        self.content = ["Select a file and press Enter, or click it, to open it here."]
        self.source_text = ""
        self.previewable = False
        self.markdown = False
        self.rendered = None
        self.syntax = None
        self.language = ""
        self.render_width = None
        self.restore_horizontal = False
        self.color_pairs = {}
        self.theme_loader = theme_loader
        self.folder_style = folder_style
        self.theme_config = {}
        self.appearance = "dark"
        self.palette = resolve_theme()
        self.styles = {}
        self.body = self.tree_body = 10
        self.content_top = 7
        self.divider = 26
        self.narrow = False
        self.size = size
        self.size_draft = None
        self.on_resize = on_resize
        self.layout_loader = layout_loader
        self.on_layout = on_layout
        self.layout = "popup"
        self.layout_dialog = False
        self.on_state = on_state
        self.saved_state = None
        self.defer_status = defer_status
        self.status_job = None
        self.pending_selection = ""
        self.pending_scroll = 0
        self.message = ""
        # Diagrams need their renderer commands and a Kitty graphics writer.
        self.diagram_tools = diagram_tools or {}
        self.diagram_languages = diagram_preview.available(self.diagram_tools) if graphics else set()
        self.graphics = graphics
        self.cell_size = cell_size
        self.diagrams = {}  # (language, source) -> ("ok", image ID, PNG) or ("error", message)
        self.diagram_list, self.diagram_queue, self.diagram_job = [], [], None
        self.diagram_source = False
        self.zooms = {}  # (language, source) -> zoom, kept while the navigator stays open.
        self.chosen_diagram = None  # The Markdown diagram that zoom keys adjust.
        self.zoom_version = 0
        self.alignment = alignment if alignment in diagram_preview.ALIGNMENTS else "center"
        self.on_alignment = on_alignment
        self.icons = icons if icons in ICONS else "plain"
        self.on_icons = on_icons
        self.diagram_extent = None  # Zoomed (cols, rows) of a diagram file's image.
        self.markdown_diagrams = []
        self.render_body = None
        self.image_id = 0
        self.placements = []
        self.images_sent, self.images_stale = set(), set()
        self.image_placed = self.cell = None
        self.screen_size = None
        # Find in preview: typed text, matches as (line, start, end) over clean(line).
        self.finding = False
        self.find_query = self.find_before = ""
        self.find_matches, self.find_content, self.find_for = [], None, None
        self.find_index = -1
        self.find_origin = (0, 0)
        self.text_width = 60
        # Command line (":" or Alt+X): the draft while open, else None.
        self.command = None
        self.command_history, self.command_recall = [], 0
        # Key sequences that close Lens, such as the host's toggle binding.
        self.close_keys, self.close_typed = [tuple(keys) for keys in close_keys], ()
        self.index = None
        self.items = []
        self.apply_settings()
        self.refresh()
        if initial_state is not None:
            self.restore_state(initial_state)
        if self.settings_errors:
            self.message = self.settings_errors  # Config mistakes outrank the restore note.

    def apply_settings(self):
        if self.settings_loader is None:
            return
        chosen = self.settings_loader()
        self.editor = chosen.editor or self.environment_editor
        if chosen.icons:
            self.icons = chosen.icons
        if chosen.align:
            self.alignment = chosen.align
        self.bindings = chosen.keys
        self.message = self.settings_errors = "; ".join(chosen.errors)

    def edit_settings(self, screen):
        if self.settings_file is None:
            self.message = "Settings need Herdr's plugin config directory"
            return
        try:
            path = self.settings_file()
            result = self.run_terminal(screen, editor_command(self.editor, path), path.parent)
        except (OSError, ValueError, subprocess.SubprocessError) as error:
            self.message = str(error)
            return
        self.apply_settings()
        if not self.message:
            self.message = "Settings reloaded" if result.returncode == 0 else f"Editor exited with status {result.returncode}"

    def export_state(self):
        return {"root": str(self.root), "changes": self.changes, "query": self.query,
                "include_ignored": self.include_ignored,
                "expanded": sorted(self.expanded), "active": self.active,
                "selected": self.pending_selection or (self.items[self.selected].path if self.items else ""),
                "scroll": self.pending_scroll if self.pending_selection else self.scroll,
                "preview_scroll": self.preview_scroll,
                "horizontal": self.horizontal, "preview_focus": self.preview_focus}

    def checkpoint(self):
        if self.on_state is None or self.index is None:
            return
        state = self.export_state()
        if state == self.saved_state:
            return
        try:
            self.on_state(state)
            self.saved_state = state
        except (OSError, ValueError, RuntimeError) as error:
            self.message = f"Could not save navigator state: {error}"

    def change_root(self, raw):
        try:
            if not str(raw):
                raise ValueError("Enter a directory path")
            target = Path(raw).expanduser()
            if not target.is_absolute():
                target = self.root / target
            target = target.resolve(strict=True)
            # os.walk reports unreadable roots as an empty listing; reject them
            # before replacing a usable tree with a misleading empty project.
            with os.scandir(target) as entries:
                next(entries, None)
            index = self.scan_index(target, self.include_ignored)
        except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as error:
            self.root_error = self.message = f"Could not change root: {error}"
            return False
        previous = self.root
        self.checkpoint()
        self.root, self.index = index.root, index
        self.pending_selection = ""
        self.query = self.search_before = ""
        self.searching = self.preview_focus = False
        self.expanded.clear()
        self.selected = self.scroll = self.preview_scroll = self.horizontal = 0
        self.clear_preview()
        self.root_draft = None
        self.root_error = ""
        self.rebuild()
        if previous.parent == self.root:
            self.selected = next((i for i, row in enumerate(self.items)
                                  if row.path == previous.name and row.directory), 0)
        self.message = index.note or f"Root changed to {self.root}"
        return True

    def clear_preview(self):
        self.active = self.source_text = self.language = ""
        self.content = ["Select a file and press Enter, or click it, to open it here."]
        self.previewable = self.markdown = self.preview_focus = False
        self.rendered = self.syntax = self.render_width = None
        self.restore_horizontal = False
        self.preview_scroll = self.horizontal = 0
        self.markdown_diagrams = []
        self.start_diagrams()

    def toggle_ignored(self):
        enabled = not self.include_ignored
        try:
            index = self.scan_index(self.root, enabled)
        except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as error:
            self.message = f"Could not change ignored-file visibility: {error}"
            return
        selected = self.items[self.selected].path if self.items else ""
        self.index, self.include_ignored = index, enabled
        self.pending_selection = ""
        if enabled:
            self.changes = False
        if self.active and self.active not in self.index.files:
            self.clear_preview()
        self.rebuild()
        self.selected = next((i for i, row in enumerate(self.items) if row.path == selected), 0)
        self.scroll = 0
        self.message = ("Ignored files shown" if enabled else "Ignored files hidden")
        if index.note:
            self.message += " · " + index.note

    def parent_root(self):
        if self.root.parent == self.root:
            self.message = "Already at the filesystem root"
        else:
            self.change_root(self.root.parent)

    def repository_root(self):
        if self.index and self.index.repository:
            self.change_root(self.index.repository)
        else:
            self.message = "The current root is not inside a Git repository"

    def begin_root(self):
        target = self.root
        if not self.preview_focus and self.items:
            row = self.items[self.selected]
            if row.directory:
                target = self.root / row.path
        self.root_draft = str(target)
        self.root_cursor = len(self.root_draft)
        self.root_error = ""

    def root_key(self, key):
        if key == "\x1b":
            self.root_draft = None
        elif key in ("\n", "\r", curses.KEY_ENTER):
            self.change_root(self.root_draft)
        elif key == "\x15":
            self.root_draft, self.root_cursor = "", 0
        elif key in ("\b", "\x7f", curses.KEY_BACKSPACE):
            if self.root_cursor:
                self.root_draft = self.root_draft[:self.root_cursor - 1] + self.root_draft[self.root_cursor:]
                self.root_cursor -= 1
        elif key == curses.KEY_DC:
            self.root_draft = self.root_draft[:self.root_cursor] + self.root_draft[self.root_cursor + 1:]
        elif key in (curses.KEY_LEFT, curses.KEY_RIGHT):
            self.root_cursor = max(0, min(len(self.root_draft), self.root_cursor + (-1 if key == curses.KEY_LEFT else 1)))
        elif key in (curses.KEY_HOME, "\x01"):
            self.root_cursor = 0
        elif key in (curses.KEY_END, "\x05"):
            self.root_cursor = len(self.root_draft)
        elif isinstance(key, str) and key.isprintable() and len(self.root_draft) < 4096:
            self.root_draft = self.root_draft[:self.root_cursor] + key + self.root_draft[self.root_cursor:]
            self.root_cursor += len(key)
        return True

    def draw_root(self, screen):
        height, width = screen.getmaxyx()
        box_width = min(88, width - 2)
        x, top = (width - box_width) // 2, max(0, (height - 9) // 2)
        for y in range(top, min(height, top + 9)):
            band(screen, y, x, "", box_width, self.style("surface"))
        band(screen, top, x, "  CHANGE ROOT", box_width, self.style("header") | curses.A_BOLD)
        put(screen, top + 1, x + 2, "Absolute path, ~, or a path relative to the current root", box_width - 4, self.style("muted"))
        # Reserve two cells per character so wide paths cannot hide the cursor.
        visible = max(1, (box_width - 8) // 2)
        start = max(0, self.root_cursor - visible)
        field = self.root_draft[start:self.root_cursor] + "▏" + self.root_draft[self.root_cursor:]
        band(screen, top + 3, x + 2, ("…" if start else "") + field, box_width - 4, self.style("selected"))
        put(screen, top + 5, x + 2, "Enter Apply  Esc Cancel  ^U Clear  ←/→ Edit", box_width - 4, self.style("active"))
        put(screen, top + 6, x + 2, "Only this navigator changes; the source pane stays put.", box_width - 4, self.style("muted"))
        put(screen, top + 7, x + 2, self.root_error, box_width - 4, self.style("removed"))

    def restore_state(self, state):
        state = normalize_view(state, self.root)
        if state is None or self.index is None:
            return False
        include_ignored = state["include_ignored"]
        if include_ignored != self.include_ignored:
            try:
                self.index = self.scan_index(self.root, include_ignored)
            except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as error:
                self.message = f"Could not restore navigator state: {error}"
                return False
            self.include_ignored = include_ignored
        self.changes = state["changes"]
        self.query = state["query"]
        directories = set(self.index.directories)
        for name in self.index.files:
            parent = name.rpartition("/")[0]
            while parent:
                directories.add(parent)
                parent = parent.rpartition("/")[0]
        self.expanded = set(state["expanded"]) & directories
        self.searching = False
        self.clear_preview()
        self.rebuild()
        self.selected = next((i for i, row in enumerate(self.items) if row.path == state["selected"]), 0)
        self.pending_selection = (state["selected"] if self.index.status_pending
                                  and not any(row.path == state["selected"] for row in self.items) else "")
        self.pending_scroll = state["scroll"]
        if state["active"] in self.index.files:
            self.load(state["active"])
            if not self.previewable:
                self.clear_preview()
        self.scroll = min(state["scroll"], self.selected)
        if self.previewable:
            # Markdown offsets are rendered-line offsets; clamp on the first
            # draw, after rendering at the actual new surface width.
            self.preview_scroll = state["preview_scroll"]
            self.horizontal = state["horizontal"]
            self.restore_horizontal = True
            self.preview_focus = state["preview_focus"]
        self.message = self.index.note or "Restored previous view"
        return True

    def begin_layout(self):
        try:
            if self.layout_loader:
                self.layout = self.layout_loader()
            self.layout_dialog = True
        except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as error:
            self.message = f"Could not read layout: {error}"

    def layout_key(self, key):
        if key == "\x1b":
            self.layout_dialog = False
        elif key in ("1", "2"):
            chosen = {"1": "popup", "2": "overlay"}[key]
            self.layout_dialog = False
            if chosen == self.layout:
                return True
            if self.on_layout is None:
                self.message = "Layout switching requires Herdr"
            else:
                try:
                    if self.on_layout(chosen, self.size, self.export_state()):
                        return False
                    self.layout = chosen
                    self.message = f"Layout: {chosen.title()}"
                except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as error:
                    self.message = f"Could not switch layout: {error}"
        return True

    def draw_layout(self, screen):
        height, width = screen.getmaxyx()
        box_width = min(62, width - 2)
        x, top = (width - box_width) // 2, max(0, (height - 8) // 2)
        for y in range(top, min(height, top + 8)):
            band(screen, y, x, "", box_width, self.style("surface"))
        band(screen, top, x, "  LAYOUT", box_width, self.style("header") | curses.A_BOLD)
        lines = [f"  Current: {self.layout.title()}", "",
                 "  1 Popup    Open a floating window",
                 "  2 Overlay  Expand the navigator", "  Esc Cancel"]
        for offset, line in enumerate(lines, 1):
            put(screen, top + offset, x, line, box_width, self.style("base"))

    def size_key(self, key):
        if key == "\x1b":
            self.size_draft = None
        elif key in ("\n", "\r", curses.KEY_ENTER):
            if self.size_draft == self.size:
                self.size_draft = None
            elif self.on_resize is None:
                self.message = "Resize is available when opened as a Herdr popup"
                self.size_draft = None
            else:
                try:
                    self.on_resize(self.size_draft, self.export_state())
                    return False
                except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as error:
                    self.message = f"Could not resize: {error}"
                    self.size_draft = None
        elif key in (curses.KEY_LEFT, curses.KEY_RIGHT):
            self.size_draft = self.size_draft.adjust(width=-5 if key == curses.KEY_LEFT else 5)
        elif key in (curses.KEY_UP, curses.KEY_DOWN):
            self.size_draft = self.size_draft.adjust(height=5 if key == curses.KEY_UP else -5)
        elif key in ("1", "2", "3", "4"):
            self.size_draft = PRESETS[int(key) - 1]
        return True

    def draw_size(self, screen):
        height, width = screen.getmaxyx()
        box_width = min(62, width - 2)
        x, top = (width - box_width) // 2, max(0, (height - 11) // 2)
        for y in range(top, min(height, top + 11)):
            band(screen, y, x, "", box_width, self.style("surface"))
        band(screen, top, x, "  POPUP SIZE", box_width, self.style("header") | curses.A_BOLD)
        lines = [
            "", f"  Width   {self.size_draft.width:3}%    ← / →",
            f"  Height  {self.size_draft.height:3}%    ↓ / ↑", "",
            "  1 Small   2 Medium   3 Large   4 Maximum",
            "  Enter Apply & remember   Esc Cancel", "",
            "  Reopens at the new size, keeping your place.",
        ]
        for offset, line in enumerate(lines, 1):
            put(screen, top + offset, x, line, box_width, self.style("base"))

    def refresh(self):
        self.image_placed = None
        if self.theme_loader:
            self.theme_config = self.theme_loader()
            self.update_theme()
        try:
            selected = self.pending_selection or (self.items[self.selected].path if self.items else "")
            scroll = self.pending_scroll if self.pending_selection else self.scroll
            self.index = self.scan_index(self.root, self.include_ignored)
            self.pending_selection = ""
            self.message = self.index.note or "Refreshed"
            self.rebuild()
            match = next((i for i, row in enumerate(self.items) if row.path == selected), None)
            if match is not None:
                self.selected = match
            elif self.index.status_pending:
                self.pending_selection, self.pending_scroll = selected, scroll
            if self.active:
                self.load(self.active)
        except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as error:
            self.message = str(error)

    def scan_index(self, root, include_ignored):
        if self.defer_status:
            return scan(root, include_ignored=include_ignored, include_status=False)
        return scan(root, include_ignored=include_ignored)

    def start_status(self):
        if self.status_job is not None or self.index is None or not self.index.status_pending:
            return
        index, result = self.index, Future()
        self.status_job = (index, result)

        def work():
            try:
                result.set_result(read_status(index.root, index.repository))
            except Exception as error:
                result.set_exception(error)

        # Only one query runs at a time. Leaving the UI never joins a slow Git
        # process; its normal subprocess timeout still bounds the query.
        Thread(target=work, name="lens-status", daemon=True).start()

    def poll_status(self):
        if self.status_job is None or not self.status_job[1].done():
            return
        index, result = self.status_job
        self.status_job = None
        if index is not self.index:
            return  # Root changes and refreshes invalidate in-flight results.
        selected = self.pending_selection or (self.items[self.selected].path if self.items else "")
        try:
            previous_files = index.files
            apply_status(index, result.result())
            if self.changes or index.files != previous_files:
                self.rebuild()
                self.selected = next((i for i, row in enumerate(self.items) if row.path == selected), self.selected)
                if self.pending_selection:
                    self.scroll = min(self.pending_scroll, self.selected)
        except Exception as error:
            index.status_pending = False
            index.status_error = str(error)
            self.message = f"Could not load Git status: {error}"
        self.pending_selection = ""

    def update_theme(self):
        palette = resolve_theme(self.theme_config, self.appearance)
        if palette != self.palette:
            self.palette = palette
            self.render_width = None

    def rebuild(self):
        if self.index is None:
            self.items = []
            return
        names = [name for name in self.index.files if not self.changes or name in self.index.status]
        self.items = rows(names, self.expanded, self.query,
                          directories=self.index.directories if not self.changes else ())
        if not self.query:
            self.items.insert(0, Row("..", directory=True))
        self.selected = min(self.selected, max(0, len(self.items) - 1))

    def load(self, name: str):
        self.active = name
        self.preview_scroll = self.horizontal = 0
        self.rendered = self.render_width = None
        self.syntax = None
        self.language = ""
        self.source_text = ""
        self.previewable = False
        self.markdown = False
        try:
            self.source_text = preview(self.index, name)
            self.content = self.source_text.splitlines() or ["(Empty file)"]
            self.previewable = True
            self.markdown = Path(name).suffix.lower() in (".md", ".markdown")
        except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as error:
            self.content = [str(error)]
        self.start_diagrams()

    def diagram_file(self):
        """A standalone diagram file, shown as one image filling the panel."""
        return bool(self.diagram_list) and not self.markdown

    def diagram_sources(self):
        if not self.previewable or not self.diagram_languages:
            return []
        language = diagram_preview.file_language(self.active)
        if language:
            return [(language, self.source_text)] if language in self.diagram_languages else []
        if self.markdown:
            try:
                blocks = markdown_preview.diagram_blocks(self.source_text)
            except Exception:
                return []  # Markdown parsing failures fall back in prepare_preview.
            return list(dict.fromkeys(key for key in blocks if key[0] in self.diagram_languages))
        return []

    def start_diagrams(self):
        self.diagram_list = self.diagram_sources()
        # Refreshing unchanged sources keeps their images; others are freed.
        for source in [source for source in self.diagrams if source not in self.diagram_list]:
            entry = self.diagrams.pop(source)
            if entry[0] == "ok":
                self.images_stale.add(entry[1])
        self.diagram_queue = [source for source in self.diagram_list if source not in self.diagrams]
        self.next_diagram()

    def next_diagram(self):
        running = self.diagram_job[0] if self.diagram_job else None
        if running in self.diagram_queue:
            self.diagram_queue.remove(running)
        if self.diagram_job is not None or not self.diagram_queue:
            return
        # One renderer at a time: JVM and headless-browser starts are heavy.
        key = self.diagram_queue.pop(0)
        cwd, tools, result = (self.root / self.active).parent, self.diagram_tools, Future()
        self.diagram_job = (key, result)

        def work():
            try:
                result.set_result(diagram_preview.render(*key, cwd, tools))
            except Exception as error:
                result.set_exception(error)

        Thread(target=work, name="lens-diagram", daemon=True).start()

    def poll_diagram(self):
        if self.diagram_job is None or not self.diagram_job[1].done():
            return
        source, result = self.diagram_job
        self.diagram_job = None
        if source in self.diagram_list:
            try:
                png = result.result()
                diagram_preview.image_size(png)
                self.image_id += 1
                self.diagrams[source] = ("ok", self.image_id, png)
            except Exception as error:
                title = diagram_preview.LANGUAGES[source[0]].title
                self.diagrams[source] = ("error", f"Could not render {title}: {error}")
                if self.markdown:
                    self.message = self.diagrams[source][1]
            self.render_width = None  # Markdown reserves rows for the new image.
        self.next_diagram()

    def diagram_view(self):
        return self.diagram_file() and not self.diagram_source

    def cell_pixels(self):
        if self.cell is None:
            self.cell = (self.cell_size() if self.cell_size else None) or (10, 20)
        return self.cell

    def draw_diagram(self, screen, x, width):
        key = self.diagram_list[0]
        entry = self.diagrams.get(key)
        if entry is None or entry[0] == "error":
            waiting = f"Rendering {diagram_preview.LANGUAGES[key[0]].title}…"
            put(screen, self.content_top, x + 2, entry[1] if entry else waiting, width - 4,
                self.style("removed" if entry else "muted"))
            return
        # A zoomed image larger than the panel is panned with the scroll offsets.
        (full_cols, full_rows), (width_px, height_px) = self.diagram_extent, diagram_preview.image_size(entry[2])
        left, top = self.horizontal, self.preview_scroll
        cols, rows = min(width - 4, full_cols - left), min(self.body, full_rows - top)
        crop = None
        if (left, top, cols, rows) != (0, 0, full_cols, full_rows):
            x0, x1 = round(left * width_px / full_cols), round((left + cols) * width_px / full_cols)
            y0, y1 = round(top * height_px / full_rows), round((top + rows) * height_px / full_rows)
            crop = (x0, y0, max(1, x1 - x0), max(1, y1 - y0))
        left_edge = x + 2 + diagram_preview.offset(self.alignment, width - 4, cols)
        self.placements.append((entry[1], 1, self.content_top, left_edge, cols, rows, crop))

    def measure_diagram(self, cols):
        self.diagram_extent = None
        entry = self.diagrams.get(self.diagram_list[0]) if self.diagram_view() else None
        if entry and entry[0] == "ok":
            self.diagram_extent = diagram_preview.scaled(diagram_preview.image_size(entry[2]), cols,
                                                         self.body, self.cell_pixels(),
                                                         self.zoom_of(self.diagram_list[0]))
            self.horizontal = min(self.horizontal, max(0, self.diagram_extent[0] - cols))

    def zoom_of(self, key):
        return self.zooms.get(key, 1.0)

    def visible_diagrams(self):
        return [key for line, key, (_, rows) in self.markdown_diagrams
                if line < self.preview_scroll + self.body and line + rows > self.preview_scroll]

    def current_diagram(self):
        """The diagram zoom keys adjust: a file's only diagram, or in Markdown the
        chosen one while it is on screen, else the first one on screen."""
        if not self.markdown:
            return self.diagram_list[0] if self.diagram_list else None
        visible = self.visible_diagrams()
        if self.chosen_diagram in visible:
            return self.chosen_diagram
        return visible[0] if visible else None

    def zoom_diagram(self, key):
        target = self.current_diagram()
        if target is None:
            self.message = "Scroll a diagram into view to zoom it"
            return
        zooms = diagram_preview.ZOOMS
        index = zooms.index(self.zoom_of(target))
        zoom = 1.0 if key == "0" else zooms[max(0, min(len(zooms) - 1, index + (-1 if key == "-" else 1)))]
        self.zooms[target] = zoom
        self.chosen_diagram = target
        if not self.markdown:
            self.preview_scroll = self.horizontal = 0
        self.zoom_version += 1
        self.render_width = None  # Markdown reserves rows for the new size.
        title = diagram_preview.LANGUAGES[target[0]].title
        self.message = f"{title} zoom {round(zoom * 100)}%" + (" (fit)" if zoom == 1 else "")

    def align_diagrams(self):
        alignments = diagram_preview.ALIGNMENTS
        self.alignment = alignments[(alignments.index(self.alignment) + 1) % len(alignments)]
        self.message = f"Diagram alignment: {self.alignment.title()}"
        if self.on_alignment is not None:
            try:
                self.on_alignment(self.alignment)
            except (OSError, ValueError) as error:
                self.message += f" (not saved: {error})"

    def choose_diagram(self, step):
        keys = [key for _, key, _ in self.markdown_diagrams]
        if not keys:
            return
        current = self.current_diagram()
        index = keys.index(current) + step if current in keys else (0 if step > 0 else len(keys) - 1)
        index = max(0, min(len(keys) - 1, index))
        self.chosen_diagram = keys[index]
        line = self.markdown_diagrams[index][0]
        self.preview_scroll = max(0, min(line - 1, max(0, self.preview_length() - self.body)))
        self.message = f"Diagram {index + 1}/{len(keys)} · {round(self.zoom_of(keys[index]) * 100)}%"

    def markdown_rows(self, width):
        rows = {}
        if self.diagram_source:
            return rows
        for source in self.diagram_list:
            entry = self.diagrams.get(source)
            if entry and entry[0] == "ok":
                size = diagram_preview.image_size(entry[2])
                rows[source] = diagram_preview.scaled(size, width, self.body, self.cell_pixels(),
                                                      self.zoom_of(source), max_cols=width)
        return rows

    def place_markdown(self, screen, x):
        # Images partly scrolled out of the panel are cropped to their visible rows.
        current = self.current_diagram() if len(self.markdown_diagrams) > 1 else None
        for number, (line, source, (cols, rows)) in enumerate(self.markdown_diagrams, 1):
            top, bottom = max(line, self.preview_scroll), min(line + rows, self.preview_scroll + self.body)
            entry = self.diagrams.get(source)
            if top >= bottom or not entry or entry[0] != "ok":
                continue
            crop = None
            if top > line or bottom < line + rows:
                width, height = diagram_preview.image_size(entry[2])
                start, stop = round((top - line) * height / rows), round((bottom - line) * height / rows)
                crop = (0, start, width, max(1, stop - start))
            left_edge = x + diagram_preview.offset(self.alignment, self.render_width, cols)
            self.placements.append((entry[1], number, self.content_top + top - self.preview_scroll,
                                    left_edge, cols, bottom - top, crop))
            if source == current:
                # Mark which of several diagrams the zoom keys will change.
                for row in range(top, bottom):
                    put(screen, self.content_top + row - self.preview_scroll, x - 1, "▌", 1, self.style("active"))

    def sync_image(self):
        if self.graphics is None:
            return
        wanted = ()
        if self.root_draft is None and not self.size_draft and not self.layout_dialog:
            wanted = tuple(self.placements)
        data = b""
        for image_id in sorted(self.images_stale & self.images_sent):
            data += diagram_preview.delete(image_id)
        self.images_sent -= self.images_stale
        self.images_stale.clear()
        if wanted != self.image_placed:
            if self.image_placed is None:
                # Unknown screen state: drop every placement before redrawing.
                previous = ()
                data += b"".join(diagram_preview.hide(image_id) for image_id in sorted(self.images_sent))
            else:
                previous = self.image_placed
            keep = {placement[:2] for placement in wanted}
            for placement in previous:
                if placement[:2] not in keep and placement[0] in self.images_sent:
                    data += diagram_preview.hide(*placement[:2])
            images = {entry[1]: entry[2] for entry in self.diagrams.values() if entry[0] == "ok"}
            for placement in wanted:
                if placement[0] not in self.images_sent:
                    data += diagram_preview.transmit(placement[0], images[placement[0]])
                    self.images_sent.add(placement[0])
                if placement not in previous:
                    # The same image and placement ID replaces its old position.
                    data += diagram_preview.place(*placement)
            self.image_placed = wanted
        if data:
            self.graphics(data)

    def track_size(self, size):
        # A resize makes curses clear the screen, which also drops Kitty placements;
        # send the images again after the redraw instead of trusting the old state.
        if size != self.screen_size:
            if self.screen_size is not None:
                self.release_image()
            self.screen_size = size

    def release_image(self):
        if self.graphics is not None and self.images_sent:
            self.graphics(b"".join(diagram_preview.delete(image_id) for image_id in sorted(self.images_sent)))
        self.images_sent.clear()
        self.images_stale.clear()
        self.image_placed = None

    def prepare_preview(self, width):
        # Diagram rows depend on the panel height as well as its width.
        body = (self.body, self.zoom_version) if self.markdown and self.diagram_list else None
        if not self.previewable or (self.render_width == width and self.render_body == body):
            return
        self.render_width, self.render_body = width, body
        self.markdown_diagrams = []
        try:
            if self.markdown:
                sizes = self.markdown_rows(width)
                if sizes:
                    self.rendered, found = markdown_preview.render_diagrams(
                        self.source_text, width, self.palette, {source: rows for source, (_, rows) in sizes.items()})
                    self.markdown_diagrams = [(line, source, sizes[source]) for line, source, _ in found]
                else:
                    self.rendered = markdown_preview.render(self.source_text, width, self.palette)
                self.content = ["".join(span.text for span in line) for line in self.rendered]
            else:
                highlighted = syntax_preview.render(self.source_text, self.active, self.palette)
                if highlighted is not None:
                    self.language, self.syntax = highlighted
                    self.content = ["".join(span.text for span in line) for line in self.syntax]
        except Exception:
            # Preview rendering must never make the file browser unusable.
            self.rendered = None
            self.syntax = None
            self.language = ""
            self.markdown_diagrams = []
            self.content = self.source_text.splitlines() or ["(Empty file)"]
            self.message = "Preview styling unavailable; showing source"

    def span_style(self, style):
        attributes = (curses.A_BOLD if style.bold else 0) | (curses.A_UNDERLINE if style.underline else 0)
        if style.italic:
            attributes |= getattr(curses, "A_ITALIC", 0)
        if not curses.has_colors():
            return attributes
        foreground = style.foreground if style.foreground >= 0 else self.palette["text"]
        background = style.background if style.background >= 0 else self.palette["panel_bg"]
        colors = (terminal_color(foreground, curses.COLORS), terminal_color(background, curses.COLORS, background=True))
        if colors not in self.color_pairs:
            number = 16 + len(self.color_pairs)
            if number >= min(curses.COLOR_PAIRS, 256):
                return self.style("base") | attributes
            try:
                curses.init_pair(number, *colors)
            except curses.error:
                return self.style("base") | attributes
            self.color_pairs[colors] = curses.color_pair(number)
        return self.color_pairs[colors] | attributes

    def draw_styled_line(self, screen, y, x, width, spans):
        column = 0
        for span in spans:
            visible, start = [], None
            for char in span.text:
                size = 0 if unicodedata.combining(char) else 2 if unicodedata.east_asian_width(char) in "WF" else 1
                if self.horizontal <= column and column + size <= self.horizontal + width:
                    if start is None:
                        start = column - self.horizontal
                    visible.append(char)
                column += size
            if visible:
                put(screen, y, x + start, "".join(visible), width - start, self.span_style(span.style))

    def activate(self, screen=None):
        if not self.items:
            return
        row = self.items[self.selected]
        if row.path == "..":
            self.parent_root()
        elif row.directory:
            if row.path in self.expanded:
                self.expanded.remove(row.path)
            else:
                self.expanded.add(row.path)
            self.rebuild()
        else:
            self.preview_selected()
            if self.changes:
                self.show_diff(screen)

    def preview_selected(self, *, focus=True):
        if not self.items or self.items[self.selected].directory:
            return
        self.load(self.items[self.selected].path)
        if focus:
            self.preview_focus = True

    def current_file(self):
        if self.preview_focus:
            return self.active
        if self.items and not self.items[self.selected].directory:
            return self.items[self.selected].path
        return ""

    def edit(self, screen):
        name = self.current_file()
        if not name:
            return
        try:
            path = checked_path(self.root, name)
            if not path.is_file():
                raise ValueError("File no longer exists; use diff to inspect deletions")
            # Code and plain text previews show source lines; start the editor there.
            line = self.preview_scroll + 1 if self.preview_focus and name == self.active and self.rendered is None else 1
            command = editor_command(self.editor, path, line)
            result = self.run_terminal(screen, command, self.root)
            self.refresh()
            self.message = f"Editor exited with status {result.returncode}"
        except (OSError, ValueError, subprocess.SubprocessError) as error:
            self.message = str(error)

    def run_terminal(self, screen, command, cwd):
        self.release_image()
        terminal_input.disable()
        curses.def_prog_mode()
        curses.endwin()
        try:
            return subprocess.run(command, cwd=cwd)
        finally:
            curses.reset_prog_mode()
            try:
                curses.curs_set(0)
            except curses.error:
                pass
            terminal_input.enable(screen)
            screen.clear()

    def show_diff(self, screen):
        name = self.current_file()
        if not name:
            self.message = "Select a file to compare with HEAD"
            return
        try:
            with comparison(self.index, name) as (command, cwd):
                result = self.run_terminal(screen, command, cwd)
            self.message = "Returned from vimdiff" if result.returncode == 0 else f"vimdiff exited with status {result.returncode}"
        except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as error:
            self.message = str(error)

    def style(self, name):
        return self.styles.get(name, 0)

    def panel(self, screen, x, width, bottom, focused):
        border = self.style("active" if focused else "gutter")
        corner = ("╔", "═", "╗", "║", "╚", "╝") if focused else ("┌", "─", "┐", "│", "└", "┘")
        a, horizontal, b, vertical, c, d = corner
        put(screen, 4, x, a + horizontal * (width - 2) + b, width, border)
        put(screen, bottom, x, c + horizontal * (width - 2) + d, width, border)
        for y in range(5, bottom):
            put(screen, y, x, vertical, 1, border)
            put(screen, y, x + width - 1, vertical, 1, border)

    def draw_tree(self, screen, x, width, bottom):
        focused = not self.preview_focus and not self.searching
        self.panel(screen, x, width, bottom, focused)
        header = self.style("header" if focused else "surface")
        icons = ICONS[self.icons]
        icon = icons["changes" if self.changes else "project"]
        title = "CHANGED FILES" if self.changes else "PROJECT FILES"
        band(screen, 5, x + 1, f" {icon} {title}" if icon else f" {title}", width - 2, header)
        flag = icons["shown" if self.include_ignored else "hidden"]  # Ctrl+H toggles.
        if flag:
            put(screen, 5, x + width - 2 - cells(flag), flag, cells(flag), header)
        git = (icons["loading"] if self.index and self.index.status_pending
               else icons["error"] if self.index and self.index.status_error else "Space preview")
        put(screen, 6, x + 2, f"{len(self.items)} rows · {git}", width - 4, self.style("muted"))
        if not self.items:
            empty = "Loading Git status…" if self.index and self.index.status_pending else "Git status unavailable" if self.index and self.index.status_error else "No matching files"
            put(screen, self.content_top, x + 2, empty, width - 4, self.style("muted"))
        for offset, row in enumerate(self.items[self.scroll:self.scroll + self.tree_body]):
            selected = self.selected == self.scroll + offset
            style = self.style("folder" if row.directory else "base")
            if selected:
                style = self.style("inactive" if self.preview_focus else "selected")
            marker = ("▾  " if row.path in self.expanded else "▸  ") if row.directory else "    "
            if row.path == "..":
                marker = "↑  "
            label = row.path if self.query else row.path.rsplit("/", 1)[-1]
            status = self.index.status.get(row.path, "  ")
            text = f"{'›' if selected else ' '} {status} {'  ' * row.depth}{marker}{label}"
            band(screen, self.content_top + offset, x + 1, text, width - 2, style)

    def draw_content(self, screen, x, width, bottom):
        self.panel(screen, x, width, bottom, self.preview_focus)
        band(screen, 5, x + 1, " " + (self.active or "No file selected"), width - 2,
             self.style("header" if self.preview_focus else "surface"))
        label = "MARKDOWN" if self.rendered is not None else "FILE PREVIEW · ^D vimdiff"
        if self.syntax is not None:
            label = self.language
        if self.diagram_file():
            title = diagram_preview.LANGUAGES[self.diagram_list[0][0]].title.upper()
            label = (f"{title} · {round(self.zoom_of(self.diagram_list[0]) * 100)}% · v Source" if not self.diagram_source
                     else f"{label} · v Diagram")
        elif self.markdown and self.diagram_list and self.rendered is not None:
            current = self.current_diagram()
            keys = [key for _, key, _ in self.markdown_diagrams]
            if self.diagram_source or current not in keys:
                label += " · v Diagrams" if self.diagram_source else " · v Diagram source"
            else:
                label += (f" · Diagram {keys.index(current) + 1}/{len(keys)} "
                          f"{round(self.zoom_of(current) * 100)}% · v Diagram source")
        put(screen, 6, x + 2, label if self.active else "OPEN A FILE TO BEGIN", width - 4, self.style("muted"))
        if self.diagram_view():
            self.draw_diagram(screen, x, width)
            return
        self.text_width = width - (4 if self.rendered is not None else 10)
        highlight = bool(self.find_query) and bool(self.matches())
        for offset, line in enumerate(self.content[self.preview_scroll:self.preview_scroll + self.body]):
            y = self.content_top + offset
            if self.rendered is not None:
                self.draw_styled_line(screen, y, x + 2, width - 4, self.rendered[self.preview_scroll + offset])
            elif self.active:
                put(screen, y, x + 1, f"{self.preview_scroll + offset + 1:5} │", 7, self.style("gutter"))
                if self.syntax is not None:
                    self.draw_styled_line(screen, y, x + 8, width - 10, self.syntax[self.preview_scroll + offset])
                else:
                    put(screen, y, x + 8, clean(line)[self.horizontal:], width - 10, self.style("base"))
            else:
                put(screen, y + 1, x + 3, line, width - 6, self.style("muted"))
            if highlight and self.active:
                # Drawn over the line so the highlight wins.
                left = x + 2 if self.rendered is not None else x + 8
                self.draw_matches(screen, y, left, self.text_width, self.preview_scroll + offset)
        if self.rendered is not None and self.markdown_diagrams:
            self.place_markdown(screen, x + 2)

    def preview_length(self):
        if self.diagram_view():
            return self.diagram_extent[1] if self.diagram_extent else 1
        return len(self.content)

    def draw(self, screen):
        screen.bkgd(" ", self.style("base"))
        screen.erase()
        self.placements = []
        height, width = screen.getmaxyx()
        if height < 15 or width < 36:
            put(screen, 0, 0, "^W Layout (36 × 15 minimum)", width, curses.A_BOLD)
            if self.layout_dialog:
                self.draw_layout(screen)
            if self.size_draft:
                self.draw_size(screen)
            if self.root_draft is not None:
                self.draw_root(screen)
            screen.refresh()
            return
        bottom = height - 4
        self.content_top = 7
        self.body = self.tree_body = bottom - self.content_top
        self.divider = max(26, min(width // 4, 38))
        self.narrow = width < 90
        content_width = width - 1 if self.narrow else width - self.divider - 2
        self.prepare_preview(content_width - 4)
        self.measure_diagram(content_width - 4)
        if self.restore_horizontal:
            longest = max((sum(0 if unicodedata.combining(char) else
                               2 if unicodedata.east_asian_width(char) in "WF" else 1
                               for char in clean(line)) for line in self.content), default=0)
            available = content_width - (4 if self.rendered is not None else 10)
            self.horizontal = min(self.horizontal, max(0, longest - available))
            self.restore_horizontal = False
        self.scroll = max(0, min(self.scroll, self.selected))
        if self.selected >= self.scroll + self.tree_body:
            self.scroll = self.selected - self.tree_body + 1
        self.preview_scroll = min(self.preview_scroll, max(0, self.preview_length() - self.body))
        focus = ("ROOT" if self.root_draft is not None else "COMMAND" if self.command is not None
                 else "SEARCH" if self.searching else "FIND" if self.finding
                 else "CONTENT" if self.preview_focus else "FILES")
        band(screen, 0, 0, "  LENS", width - 1, self.style("surface") | curses.A_BOLD)
        badge = f" FOCUS: {focus} "
        band(screen, 0, max(19, width - len(badge) - 2), badge, len(badge), self.style("header") | curses.A_BOLD)
        put(screen, 1, 2, "[..]", 4, self.style("active"))
        put(screen, 1, 8, str(self.root), width - 10, self.style("muted"))
        if self.command is not None:
            band(screen, 2, 1, f" :{self.command}▏", width - 3, self.style("selected"))
        elif self.finding or (self.preview_focus and self.find_query and not self.searching):
            text = f" ⌕  Find in preview: {self.find_query}" + (" ▏" if self.finding else "  ·  n N Next/Prev")
            band(screen, 2, 1, text, width - 3, self.style("selected" if self.finding else "surface"))
        else:
            hint = "Type filename…  Enter Apply · Esc Cancel" if self.searching else "/ to search files"
            band(screen, 2, 1, f" ⌕  {self.query or hint}" + (" ▏" if self.searching and self.query else ""), width - 3,
                 self.style("selected" if self.searching else "surface"))
        if self.narrow:
            if self.preview_focus:
                self.draw_content(screen, 0, width - 1, bottom)
            else:
                self.draw_tree(screen, 0, width - 1, bottom)
        else:
            self.draw_tree(screen, 0, self.divider, bottom)
            self.draw_content(screen, self.divider + 1, width - self.divider - 2, bottom)
        position = f"{self.preview_scroll + 1}/{self.preview_length()}" if self.preview_focus else f"{self.selected + 1 if self.items else 0}/{len(self.items)}"
        band(screen, height - 3, 0, f" {focus}  {position}  ·  {self.message}", width - 1, self.style("surface"))
        enter_hint = "Enter Scroll" if self.preview_focus else "Enter Open"
        put(screen, height - 2, 1, f"^W Layout  Tab Focus  {enter_hint}  ^Y Popup size  ^D Vimdiff  ^E Edit  Esc Back", width - 2, self.style("active"))
        help_text = "SEARCH: Type filter  ^U Clear  Enter Apply  Esc Cancel" if self.searching else "^N/P Preview line  ^F/B Preview page  h/j/k/l Move  Space Preview  / Search  : Command  ^O Root  Backspace Up"
        if self.preview_focus and not self.searching:
            help_text = "j/k Line  Space/f/b Page  d/u Half  g/G Top/End  / Find  n N Next/Prev  : Command  ^O Root"
            if self.diagram_list:
                # "/" opens search, so these key pairs are not joined with a slash.
                help_text = ("+ - Zoom  0 Fit  a Align  " + ("[ ] Prev/Next diagram  " if self.markdown else "")
                             + "v Diagram/Source  " + help_text)
        if self.command is not None:
            help_text = "COMMAND: Tab Complete  ↑/↓ History  Enter Run  Esc Cancel  ·  help Lists commands"
        elif self.finding:
            help_text = "FIND: Type text (lowercase ignores case)  ^U Clear  Enter Keep  Esc Cancel"
        put(screen, height - 1, 1, help_text, width - 2, self.style("muted"))
        if self.size_draft:
            self.draw_size(screen)
        if self.layout_dialog:
            self.draw_layout(screen)
        if self.root_draft is not None:
            self.draw_root(screen)
        screen.refresh()

    def command_key(self, key, screen):
        if key == "\x1b":
            self.command = None
        elif key in ("\n", "\r", curses.KEY_ENTER):
            text, self.command = self.command.strip(), None
            if text:
                if text in self.command_history:
                    self.command_history.remove(text)
                self.command_history.append(text)
                del self.command_history[:-50]
                return self.run_command(text, screen)
        elif key == "\t":
            self.command, options = command_line.complete(self.command, self.root, self.index.files if self.index else [])
            self.message = "  ".join(options) if len(options) > 1 else "" if options else "No completions"
        elif key in (curses.KEY_UP, curses.KEY_DOWN, "\x10", "\x0e"):
            step = -1 if key in (curses.KEY_UP, "\x10") else 1
            self.command_recall = max(0, min(len(self.command_history), self.command_recall + step))
            self.command = (self.command_history[self.command_recall]
                            if self.command_recall < len(self.command_history) else "")
        elif key == "\x15":
            self.command = ""
        elif key in ("\b", "\x7f", curses.KEY_BACKSPACE):
            # Backspace on an empty line closes it, as in Vim.
            self.command = self.command[:-1] if self.command else None
        elif isinstance(key, str) and key.isprintable():
            self.command += key
        return True

    def run_command(self, text, screen):
        """Run one command line. Returns False when it closes Lens."""
        word, _, argument = text.partition(" ")
        argument = argument.strip()
        if word.isdigit() or (word.startswith(":") and word[1:].isdigit()):
            word, argument = "goto", word.lstrip(":")
        command = command_line.lookup(word)
        if command is None:
            self.message = f"Unknown command: {word}  ·  :help lists commands"
            return True
        name = command.name
        # Fixed arguments may be abbreviated too: ":align l".
        chosen = [choice for choice in command.choices if choice.startswith(argument)]
        if argument and argument not in command.choices and len(chosen) == 1:
            argument = chosen[0]
        needs = {"open": "a file", "goto": "a line number", "find": "text", "cd": "a directory",
                 "zoom": "in, out, fit or a percent", "align": "left, center or right",
                 "layout": "popup or overlay", "icons": "nerd or plain"}
        if name in needs and not argument:
            self.message = f":{command.usage} needs {needs[name]}"
            return True
        if name == "quit":
            return False
        if name == "help":
            self.message = command_line.describe(argument)
        elif name == "open":
            self.open_file(argument)
        elif name in ("goto", "top", "bottom"):
            if not self.active:
                self.message = "Open a file first"
                return True
            if name == "goto":
                try:
                    line = int(argument)
                except ValueError:
                    self.message = f"Not a line number: {argument}"
                    return True
            else:
                line = 1 if name == "top" else self.preview_length()
            self.preview_focus = True
            self.preview_scroll = max(0, min(line - 1, max(0, self.preview_length() - self.body)))
            self.message = f"Line {max(1, min(line, self.preview_length()))}/{self.preview_length()}"
        elif name == "find":
            if not self.active:
                self.message = "Open a file first"
                return True
            self.preview_focus = True
            self.find_query, self.find_index = argument, -1
            self.find_next(1, origin=self.preview_scroll)
        elif name == "cd":
            self.change_root(argument)
        elif name == "icons":
            if argument not in ICONS:
                self.message = f":{command.usage}"
                return True
            self.icons = argument
            self.message = f"Icons: {argument}"
            if self.on_icons is not None:
                try:
                    self.on_icons(argument)
                except (OSError, ValueError) as error:
                    self.message += f" (not saved: {error})"
        elif name in ("zoom", "align", "source", "diagram"):
            self.diagram_command(name, argument)
        elif name in ("changes", "project"):
            want = name == "changes"
            if self.changes != want:
                self.changes = want
                self.preview_focus = False
                self.selected = self.scroll = 0
                self.rebuild()
            self.message = "Changed files only" if want else "All project files"
        elif name == "ignored":
            if argument not in ("", "on", "off"):
                self.message = f":{command.usage}"
            elif argument == "" or (argument == "on") != self.include_ignored:
                self.toggle_ignored()
        elif name == "refresh":
            self.refresh()
            self.message = "Refreshed"
        elif name == "config":
            self.edit_settings(screen)
        elif name == "editor":
            self.edit(screen)
        elif name == "diff":
            self.show_diff(screen)
        elif name == "layout":
            if argument not in ("popup", "overlay"):
                self.message = f":{command.usage}"
                return True
            self.begin_layout()
            if self.layout_dialog:
                return self.layout_key("1" if argument == "popup" else "2")
        return True

    def open_file(self, argument):
        target = Path(argument).expanduser()
        if target.is_absolute():
            try:
                argument = target.resolve().relative_to(self.root.resolve()).as_posix()
            except (OSError, ValueError):
                self.message = f"Outside the current root: {argument}"
                return
        name = argument.strip("/")
        if not self.index or name not in self.index.files:
            self.message = f"No such file in the tree: {argument}"
            return
        # Reveal the file in the tree so the selection follows the preview.
        parent = name.rpartition("/")[0]
        while parent:
            self.expanded.add(parent)
            parent = parent.rpartition("/")[0]
        self.rebuild()
        self.selected = next((i for i, row in enumerate(self.items) if row.path == name), self.selected)
        self.load(name)
        self.preview_focus = True
        self.message = f"Opened {name}"

    def diagram_command(self, name, argument):
        if not self.diagram_list:
            self.message = "No diagram in this preview"
            return
        if name in ("source", "diagram"):
            if self.diagram_source != (name == "source"):
                self.preview_key("v")
            self.message = "Diagram source" if self.diagram_source else "Diagram images"
            return
        if self.diagram_source:
            self.preview_key("v")
        if name == "align":
            if argument not in diagram_preview.ALIGNMENTS:
                self.message = "Use :align left, center or right"
                return
            alignments = diagram_preview.ALIGNMENTS
            # align_diagrams steps forward and saves; start one before the target.
            self.alignment = alignments[alignments.index(argument) - 1]
            self.align_diagrams()
            return
        keys = {"in": "+", "out": "-", "fit": "0"}
        if argument in keys:
            self.zoom_diagram(keys[argument])
            return
        try:
            zoom = float(argument.rstrip("%")) / 100
        except ValueError:
            zoom = None
        if zoom not in diagram_preview.ZOOMS:
            self.message = "Zoom steps: " + " ".join(f"{round(z * 100)}" for z in diagram_preview.ZOOMS)
            return
        target = self.current_diagram()
        if target is None:
            self.message = "Scroll a diagram into view to zoom it"
            return
        # zoom_diagram("0") resets to fit and rescales; then apply the exact step.
        self.zoom_diagram("0")
        self.zooms[target] = zoom
        self.message = f"{diagram_preview.LANGUAGES[target[0]].title} zoom {round(zoom * 100)}%"

    def matches(self):
        if self.find_content is not self.content or self.find_for != self.find_query:
            self.find_content, self.find_for, self.find_matches = self.content, self.find_query, []
            self.find_index = -1
            needle = self.find_query
            # Smart case: an all-lowercase query ignores case.
            fold = needle == needle.lower()
            if needle and not self.diagram_view():
                needle = needle.lower() if fold else needle
                for number, line in enumerate(self.content):
                    text = clean(line)
                    haystack = text.lower() if fold and len(text.lower()) == len(text) else text
                    start = haystack.find(needle)
                    while start >= 0:
                        self.find_matches.append((number, start, start + len(needle)))
                        start = haystack.find(needle, start + len(needle))
        return self.find_matches

    def begin_find(self):
        self.finding = True
        self.find_before, self.find_query = self.find_query, ""
        self.find_origin = (self.preview_scroll, self.horizontal)

    def find_key(self, key, screen):
        if key == "\x1b":
            self.finding = False
            self.find_query = self.find_before
            self.preview_scroll, self.horizontal = self.find_origin
            return True
        if key in ("\n", "\r", curses.KEY_ENTER):
            self.finding = False
            if not self.find_query and self.find_before:
                self.find_query = self.find_before  # Enter alone repeats the last search.
                self.find_next(1, origin=self.find_origin[0])
            elif self.find_query and not self.matches():
                self.message = f"Not found: {self.find_query}"
            return True
        if key == "\x15":
            self.find_query = ""
        elif key in ("\b", "\x7f", curses.KEY_BACKSPACE):
            self.find_query = self.find_query[:-1]
        elif isinstance(key, str) and key.isprintable():
            self.find_query += key
        elif isinstance(key, terminal_input.Mouse):
            if key.action in ("up", "down"):
                self.handle_mouse(key, screen)
            return True
        else:
            return True
        # Incremental: show the first match at or below where the search began.
        self.preview_scroll, self.horizontal = self.find_origin
        if self.find_query:
            self.find_next(1, origin=self.find_origin[0])
        else:
            self.message = ""
        return True

    def find_next(self, step, origin=None):
        matches = self.matches()
        if not matches:
            self.message = (f"Not found: {self.find_query}" if not self.diagram_view()
                            else "Press v to search the diagram source")
            return
        wrapped = False
        if origin is not None:
            index = next((i for i, match in enumerate(matches) if match[0] >= origin), None)
            if index is None:
                index, wrapped = 0, True
        elif self.find_index < 0:
            top = self.preview_scroll
            index = next((i for i, match in enumerate(matches) if match[0] >= top), 0)
            if step < 0:
                index = next((i for i in range(len(matches) - 1, -1, -1) if matches[i][0] < top), len(matches) - 1)
        else:
            index = self.find_index + step
            wrapped = not 0 <= index < len(matches)
            index %= len(matches)
        self.find_index = index
        self.reveal(matches[index])
        self.message = f"Match {index + 1}/{len(matches)}" + (" (wrapped)" if wrapped else "")

    def reveal(self, match):
        line, start, end = match
        if not self.preview_scroll <= line < self.preview_scroll + self.body:
            self.preview_scroll = max(0, min(line - self.body // 3, max(0, len(self.content) - self.body)))
        if self.rendered is None:
            # Code and plain text do not wrap: bring the match into the visible columns.
            text = clean(self.content[line])
            if self.syntax is not None:
                first, last = cells(text[:start]), cells(text[:end])
            else:
                first, last = start, end  # Plain text scrolls by characters.
            if first < self.horizontal or last > self.horizontal + self.text_width:
                self.horizontal = max(0, first - self.text_width // 3)

    def draw_matches(self, screen, y, x, width, number):
        line = clean(self.content[number])
        for index, (row, start, end) in enumerate(self.find_matches):
            if row != number:
                continue
            if self.rendered is not None or self.syntax is not None:
                column = cells(line[:start]) - self.horizontal
            else:
                if start < self.horizontal:
                    continue
                column = cells(line[self.horizontal:start])
            if column < 0 or column >= width:
                continue
            style = self.style("header" if index == self.find_index else "selected") | curses.A_BOLD
            put(screen, y, x + column, line[start:end], width - column, style)

    def move(self, amount: int):
        if self.preview_focus:
            self.scroll_preview(amount)
        else:
            self.selected = max(0, min(len(self.items) - 1, self.selected + amount))

    def scroll_preview(self, amount: int):
        self.preview_scroll = max(0, min(max(0, self.preview_length() - self.body), self.preview_scroll + amount))

    def preview_key(self, key):
        page = max(1, self.body)
        shared = {"\x0e": 1, "\x10": -1, "\x06": page, "\x02": -page}
        if key in shared:
            self.scroll_preview(shared[key])
            return True
        if key in ("+", "=", "-", "0") and self.diagram_list and not self.diagram_source:
            self.zoom_diagram(key)
            return True
        if key == "a" and self.diagram_list and not self.diagram_source:
            self.align_diagrams()
            return True
        if key in ("[", "]") and self.markdown and self.markdown_diagrams:
            self.choose_diagram(-1 if key == "[" else 1)
            return True
        if key == "v" and self.diagram_list:
            self.diagram_source = not self.diagram_source
            self.preview_scroll = self.horizontal = 0
            self.render_width = None
            return True
        if not self.preview_focus:
            return False
        if key in ("n", "N") and self.find_query:
            self.find_next(1 if key == "n" else -1)
            return True
        half = max(1, page // 2)
        movements = {
            "j": 1, "e": 1, "\n": 1, "\r": 1, curses.KEY_ENTER: 1,
            "k": -1, "y": -1,
            " ": page, "f": page,
            "b": -page,
            "d": half, "u": -half, "\x15": -half,
            "g": -self.preview_length(), "<": -self.preview_length(),
            "G": self.preview_length(), ">": self.preview_length(),
        }
        if key not in movements:
            return False
        self.move(movements[key])
        return True

    def mouse(self, screen=None):
        try:
            _, x, y, _, state = curses.getmouse()
        except curses.error:
            return
        pressed = state & (curses.BUTTON1_CLICKED | curses.BUTTON1_DOUBLE_CLICKED | curses.BUTTON1_PRESSED)
        if state & getattr(curses, "BUTTON4_PRESSED", 0):
            self.handle_mouse(terminal_input.Mouse(x, y, "up"), screen)
        elif state & getattr(curses, "BUTTON5_PRESSED", 0):
            self.handle_mouse(terminal_input.Mouse(x, y, "down"), screen)
        elif pressed:
            self.handle_mouse(terminal_input.Mouse(x, y, "click"), screen)

    def handle_mouse(self, event, screen=None):
        if self.root_draft is not None or self.size_draft or self.layout_dialog:
            return
        x, y = event.x, event.y
        if y == 1 and event.action == "click" and not self.searching:
            if 2 <= x < 6:
                self.parent_root()
            elif x >= 8:
                self.begin_root()
            return
        if y < 4 or y > self.content_top + self.body or x < 0:
            return
        if event.action in ("up", "down"):
            amount = -3 if event.action == "up" else 3
            over_preview = self.preview_focus if self.narrow else x > self.divider
            if over_preview:
                self.scroll_preview(amount)
            else:
                self.selected = max(0, min(len(self.items) - 1, self.selected + amount))
            return
        self.searching = False
        if not self.narrow:
            self.preview_focus = x > self.divider
        if event.action == "click":
            if not self.preview_focus and self.content_top <= y < self.content_top + self.tree_body:
                index = self.scroll + y - self.content_top
                if index < len(self.items):
                    self.selected = index
                    self.activate(screen)

    def key(self, key, screen) -> bool:
        if isinstance(key, terminal_input.Appearance):
            self.appearance = key.mode
            self.update_theme()
            return True
        typing = (self.layout_dialog or self.size_draft or self.root_draft is not None
                  or self.finding or self.searching or self.command is not None)
        if key in self.bindings and not typing:
            target = self.bindings[key]
            if target.startswith(":"):
                return self.run_command(target[1:].strip(), screen)
            key = settings.ACTIONS[target]
        if key == "\x03":
            return False
        if self.close_keys:
            typed = self.close_typed + (key,)
            if typed in self.close_keys:
                return False
            if any(keys[:len(typed)] == typed for keys in self.close_keys):
                self.close_typed = typed  # Wait for the rest of the binding.
                return True
            self.close_typed = ()
        if self.layout_dialog:
            return self.layout_key(key)
        if self.size_draft:
            return self.size_key(key)
        if self.root_draft is not None:
            return self.root_key(key)
        if self.finding:
            return self.find_key(key, screen)
        if self.command is not None:
            return self.command_key(key, screen)
        if (key == ":" or key == "\x1bx") and not self.searching:
            self.command, self.command_recall = "", len(self.command_history)
            return True
        if key == "/" and self.preview_focus and not self.searching and self.active:
            self.begin_find()
            return True
        if not self.preview_focus and not self.searching:
            key = {"h": curses.KEY_LEFT, "j": curses.KEY_DOWN,
                   "k": curses.KEY_UP, "l": curses.KEY_RIGHT}.get(key, key)
        navigation = (curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT,
                      curses.KEY_PPAGE, curses.KEY_NPAGE, curses.KEY_HOME, curses.KEY_END)
        if (self.searching or key in ("/", "\x07") or isinstance(key, terminal_input.Mouse)
                or (not self.preview_focus and key in navigation)):
            self.pending_selection = ""
        if key == "/" and not self.searching:
            if not self.searching:
                self.search_before = self.query
            self.searching = True
            self.preview_focus = False
        elif self.searching:
            if key == "\x1b":
                self.query = self.search_before
                self.searching = False
            elif key in ("\n", "\r", curses.KEY_ENTER):
                self.searching = False
            elif key in ("\x15", "\b", "\x7f", curses.KEY_BACKSPACE):
                self.query = "" if key == "\x15" else self.query[:-1]
            elif isinstance(key, str) and key.isprintable():
                self.query += key
            elif isinstance(key, terminal_input.Mouse):
                self.handle_mouse(key, screen)
                return True
            self.selected = self.scroll = 0
            self.rebuild()
        elif isinstance(key, terminal_input.Mouse):
            self.handle_mouse(key, screen)
        elif key == "\x0f":
            self.begin_root()
        elif key == "\x14":
            self.repository_root()
        elif key == "\x08":
            self.toggle_ignored()
        elif key in ("\x7f", curses.KEY_BACKSPACE) and not self.preview_focus and not self.query:
            self.parent_root()
        elif self.preview_key(key):
            pass
        elif key == " " and not self.preview_focus:
            self.preview_selected(focus=False)
        elif key == "\x17":
            self.begin_layout()
        elif key == "\x19":
            try:
                if self.layout_loader:
                    self.layout = self.layout_loader()
                if self.layout == "popup":
                    self.size_draft = self.size
                else:
                    self.message = "Choose Popup with Ctrl+W, then Ctrl+Y to set its size"
            except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as error:
                self.message = f"Could not read layout: {error}"
        elif key == "\x1b":
            if self.preview_focus:
                self.preview_focus = False
            elif self.query:
                self.query = ""
                self.selected = self.scroll = 0
                self.rebuild()
            else:
                return False
        elif key in ("\n", "\r", curses.KEY_ENTER):
            if not self.preview_focus:
                self.activate(screen)
        elif key in ("\t", curses.KEY_BTAB):
            self.preview_focus = not self.preview_focus
        elif key == "\x04":
            self.show_diff(screen)
        elif key == "\x05":
            self.edit(screen)
        elif key == "\x07":
            self.changes = not self.changes
            self.preview_focus = False
            self.selected = self.scroll = 0
            self.rebuild()
        elif key == "\x12":
            self.refresh()
        elif key in (curses.KEY_UP, curses.KEY_DOWN, curses.KEY_PPAGE, curses.KEY_NPAGE):
            self.move({curses.KEY_UP: -1, curses.KEY_DOWN: 1, curses.KEY_PPAGE: -self.body, curses.KEY_NPAGE: self.body}[key])
        elif key in (curses.KEY_HOME, curses.KEY_END):
            self.move(-1000000 if key == curses.KEY_HOME else 1000000)
        elif key in (curses.KEY_LEFT, curses.KEY_RIGHT):
            if self.preview_focus:
                self.horizontal = max(0, self.horizontal + (-8 if key == curses.KEY_LEFT else 8))
            elif self.items and not self.query:
                row = self.items[self.selected]
                if row.path == "..":
                    self.parent_root()
                elif key == curses.KEY_RIGHT and row.directory:
                    if row.path in self.expanded:
                        if self.selected + 1 < len(self.items) and self.items[self.selected + 1].path.startswith(row.path + "/"):
                            self.selected += 1
                    else:
                        self.expanded.add(row.path)
                elif key == curses.KEY_LEFT:
                    if row.directory and row.path in self.expanded:
                        self.expanded.remove(row.path)
                    else:
                        parent = row.path.rpartition("/")[0]
                        self.selected = next((i for i, entry in enumerate(self.items) if entry.path == parent), self.selected)
                self.rebuild()
        elif key == curses.KEY_MOUSE:
            self.mouse(screen)
        return True

    def run(self, screen):
        try:
            curses.curs_set(0)
        except curses.error:
            pass
        applied_palette = None
        terminal_input.enable(screen)
        try:
            while True:
                self.poll_status()
                self.poll_diagram()
                terminal_input.sync_size(screen)
                self.track_size(screen.getmaxyx())
                if applied_palette != self.palette:
                    self.styles = theme(self.palette, self.folder_style)
                    self.color_pairs.clear()
                    applied_palette = self.palette
                self.draw(screen)
                self.sync_image()
                self.start_status()
                # Checkpoint the last displayed view before blocking for input;
                # host-driven closure may terminate without a Python exit.
                self.checkpoint()
                try:
                    busy = self.status_job is not None or self.diagram_job is not None
                    screen.timeout(50 if busy else 250)
                    key = terminal_input.read(screen)
                except curses.error:
                    continue
                if not self.key(key, screen):
                    break
        finally:
            self.release_image()
            self.checkpoint()
            terminal_input.disable()
