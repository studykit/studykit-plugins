"""Keyboard and mouse file navigation in a Herdr terminal surface."""
from __future__ import annotations

import curses
import os
from pathlib import Path
import subprocess
import unicodedata

from core import Row, checked_path, editor_command, preview, rows, scan
from diff_tool import comparison
from popup_size import PopupSize, PRESETS
from view_state import normalize as normalize_view
import markdown_preview
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


def band(screen, y, x, text, width, style=0):
    put(screen, y, x, " " * max(0, width), width, style)
    put(screen, y, x, text, width, style)


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
                 folder_style=None, on_state=None):
        self.root, self.pane_id, self.editor = root, pane_id, editor
        self.changes = changes
        self.include_ignored = False
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
        self.content_top = 8
        self.divider = 26
        self.narrow = False
        self.size = size
        self.size_draft = None
        self.on_resize = on_resize
        self.on_state = on_state
        self.saved_state = None
        self.message = ""
        self.index = None
        self.items = []
        self.refresh()

    def export_state(self):
        return {"root": str(self.root), "changes": self.changes, "query": self.query,
                "include_ignored": self.include_ignored,
                "expanded": sorted(self.expanded), "active": self.active,
                "selected": self.items[self.selected].path if self.items else "",
                "scroll": self.scroll, "preview_scroll": self.preview_scroll,
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
            index = scan(target, include_ignored=self.include_ignored)
        except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as error:
            self.root_error = self.message = f"Could not change root: {error}"
            return False
        previous = self.root
        self.checkpoint()
        self.root, self.index = index.root, index
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

    def toggle_ignored(self):
        enabled = not self.include_ignored
        try:
            index = scan(self.root, include_ignored=enabled)
        except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as error:
            self.message = f"Could not change ignored-file visibility: {error}"
            return
        selected = self.items[self.selected].path if self.items else ""
        self.index, self.include_ignored = index, enabled
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
                self.index = scan(self.root, include_ignored=include_ignored)
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
        if state["active"] in self.index.files:
            self.load(state["active"])
            if not self.previewable:
                self.clear_preview()
        self.scroll = min(state["scroll"], self.selected)
        if self.previewable:
            # Markdown offsets are rendered-line offsets; clamp on the first
            # draw, after rendering at the actual new popup width.
            self.preview_scroll = state["preview_scroll"]
            self.horizontal = state["horizontal"]
            self.restore_horizontal = True
            self.preview_focus = state["preview_focus"]
        self.message = self.index.note or "Restored previous view"
        return True

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
        if self.theme_loader:
            self.theme_config = self.theme_loader()
            self.update_theme()
        try:
            self.index = scan(self.root, include_ignored=self.include_ignored)
            self.message = self.index.note or "Refreshed"
            self.rebuild()
            if self.active:
                self.load(self.active)
        except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as error:
            self.message = str(error)

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

    def prepare_preview(self, width):
        if not self.previewable or self.render_width == width:
            return
        self.render_width = width
        try:
            if self.markdown:
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
            command = editor_command(self.editor, path)
            result = self.run_terminal(screen, command, self.root)
            self.refresh()
            self.message = f"Editor exited with status {result.returncode}"
        except (OSError, ValueError, subprocess.SubprocessError) as error:
            self.message = str(error)

    def run_terminal(self, screen, command, cwd):
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

    def panel(self, screen, x, width, bottom, title, focused):
        border = self.style("active" if focused else "gutter")
        corner = ("╔", "═", "╗", "║", "╚", "╝") if focused else ("┌", "─", "┐", "│", "└", "┘")
        a, horizontal, b, vertical, c, d = corner
        put(screen, 4, x, a + horizontal * (width - 2) + b, width, border)
        put(screen, bottom, x, c + horizontal * (width - 2) + d, width, border)
        for y in range(5, bottom):
            put(screen, y, x, vertical, 1, border)
            put(screen, y, x + width - 1, vertical, 1, border)
        label = f" {'●' if focused else '○'} {title}" + (" · ACTIVE" if focused else "")
        band(screen, 5, x + 1, label, width - 2,
             self.style("header" if focused else "inactive") | curses.A_BOLD)

    def draw_tree(self, screen, x, width, bottom):
        self.panel(screen, x, width, bottom, "FILES", not self.preview_focus and not self.searching)
        band(screen, 6, x + 1, " CHANGED FILES" if self.changes else " PROJECT FILES", width - 2, self.style("surface"))
        put(screen, 7, x + 2, f"{len(self.items)} rows · Space preview", width - 4, self.style("muted"))
        if not self.items:
            put(screen, self.content_top, x + 2, "No matching files", width - 4, self.style("muted"))
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
        self.panel(screen, x, width, bottom, "CONTENT", self.preview_focus)
        band(screen, 6, x + 1, " " + (self.active or "No file selected"), width - 2, self.style("surface"))
        label = "MARKDOWN · Rich" if self.rendered is not None else "FILE PREVIEW · ^D vimdiff"
        if self.syntax is not None:
            label = f"{self.language} · Pygments"
        put(screen, 7, x + 2, label if self.active else "OPEN A FILE TO BEGIN", width - 4, self.style("muted"))
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

    def preview_length(self):
        return len(self.content)

    def draw(self, screen):
        screen.bkgd(" ", self.style("base"))
        screen.erase()
        height, width = screen.getmaxyx()
        if height < 15 or width < 36:
            put(screen, 0, 0, "Enlarge terminal (36 × 15 minimum)", width, curses.A_BOLD)
            if self.size_draft:
                self.draw_size(screen)
            if self.root_draft is not None:
                self.draw_root(screen)
            screen.refresh()
            return
        bottom = height - 4
        self.content_top = 8
        self.body = self.tree_body = bottom - self.content_top
        self.divider = max(26, min(width // 4, 38))
        self.narrow = width < 90
        content_width = width - 1 if self.narrow else width - self.divider - 2
        self.prepare_preview(content_width - 4)
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
        focus = "ROOT" if self.root_draft is not None else "SEARCH" if self.searching else "CONTENT" if self.preview_focus else "FILES"
        band(screen, 0, 0, "  FILE NAVIGATOR", width - 1, self.style("surface") | curses.A_BOLD)
        badge = f" FOCUS: {focus} "
        band(screen, 0, max(19, width - len(badge) - 2), badge, len(badge), self.style("header") | curses.A_BOLD)
        put(screen, 1, 2, "[..]", 4, self.style("active"))
        put(screen, 1, 8, str(self.root), width - 10, self.style("muted"))
        hint = "Type filename…  Enter Apply · Esc Cancel" if self.searching else "Ctrl+S to search files"
        band(screen, 2, 1, f" ⌕  {self.query or hint}" + (" ▏" if self.searching and self.query else ""), width - 3,
             self.style("selected" if self.searching else "surface"))
        mode = "CHANGES" if self.changes else "PROJECT"
        visibility = "shown" if self.include_ignored else "hidden"
        put(screen, 3, 2, f"{mode} · Ignored: {visibility} (^V)", width - 4, self.style("active"))
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
        put(screen, height - 2, 1, f"Tab Focus  ^W Size  {enter_hint}  ^D Vimdiff  ^E Edit  Esc Back", width - 2, self.style("active"))
        help_text = "SEARCH: Type filter  ^U Clear  Enter Apply  Esc Cancel" if self.searching else "^N/P Preview line  ^F/B Preview page  h/j/k/l Move  Space Preview  ^S Search  ^O Root  Backspace Up"
        if self.preview_focus and not self.searching:
            help_text = "j/k Line  Space/f/b Page  d/u Half  g/G Top/End  ^S Search  ^O Root  ^T Git root"
        put(screen, height - 1, 1, help_text, width - 2, self.style("muted"))
        if self.size_draft:
            self.draw_size(screen)
        if self.root_draft is not None:
            self.draw_root(screen)
        screen.refresh()

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
        if not self.preview_focus:
            return False
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
        if self.root_draft is not None or self.size_draft:
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
        if key == "\x03":
            return False
        if self.size_draft:
            return self.size_key(key)
        if self.root_draft is not None:
            return self.root_key(key)
        if not self.preview_focus and not self.searching:
            key = {"h": curses.KEY_LEFT, "j": curses.KEY_DOWN,
                   "k": curses.KEY_UP, "l": curses.KEY_RIGHT}.get(key, key)
        if key == "\x13":
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
        elif key == "\x16":
            self.toggle_ignored()
        elif key in ("\b", "\x7f", curses.KEY_BACKSPACE) and not self.preview_focus and not self.query:
            self.parent_root()
        elif self.preview_key(key):
            pass
        elif key == " " and not self.preview_focus:
            self.preview_selected(focus=False)
        elif key == "\x17":
            self.size_draft = self.size
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
                if applied_palette != self.palette:
                    self.styles = theme(self.palette, self.folder_style)
                    self.color_pairs.clear()
                    applied_palette = self.palette
                self.draw(screen)
                # Checkpoint the last displayed view before blocking for input;
                # host-driven popup closure may terminate without a Python exit.
                self.checkpoint()
                try:
                    key = terminal_input.read(screen)
                except curses.error:
                    continue
                if not self.key(key, screen):
                    break
        finally:
            self.checkpoint()
            terminal_input.disable()
