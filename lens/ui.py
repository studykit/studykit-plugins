"""Keyboard and mouse file navigation in a Herdr terminal surface."""
from __future__ import annotations

import curses
from concurrent.futures import Future
import os
from pathlib import Path
import re
import subprocess
from threading import Thread
import unicodedata

from core import Row, apply_status, application_command, checked_path, editor_command, highlights, opener_command, preview, read_status, rows, scan
from diff_tool import comparison
import git_history
from popup_size import PopupSize, PRESETS
from view_state import normalize as normalize_view
import command_line
import comments
import settings
import markdown_preview
import obsidian_embeds
import diagram_preview
import syntax_preview
import terminal_input
from theme_colors import resolve as resolve_theme, terminal_color


OPENING = {")": "(", "]": "[", ">": "<"}
MAX_LINK_HISTORY = 50


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


AGENT_SCOPES = ("tab", "workspace", "session")
# A reference in the comment message: path, then line, column, last line, last column.
REFERENCE = re.compile(r"(.+?)(?::(\d+)(?::(\d+))?(?:-(\d+)(?::(\d+))?)?)?")
REFERENCE_SHAPE = re.compile(r"\S+:\d+(?::\d+)?(?:-\d+(?::\d+)?)?")


def key_label(key):
    """How a chord from settings.chord reads in a hint: ^S, M-s."""
    if isinstance(key, str) and len(key) == 1 and ord(key) < 32:
        return "^" + chr(ord(key) + 64)
    if isinstance(key, str) and key.startswith("\x1b") and len(key) == 2:
        return "M-" + key[1]
    return str(key)


def wrap_rows(text, width):
    """Text split into screen rows of at most width cells: (index of the row's first character, row)."""
    rows, position = [], 0
    for line in text.split("\n"):
        start, used = 0, 0
        for index, char in enumerate(line):
            size = cells(char)
            if used + size > width and index > start:
                rows.append((position + start, line[start:index]))
                start, used = index, 0
            used += size
        rows.append((position + start, line[start:]))
        position += len(line) + 1
    return rows


# The two boxes start right under the root line; the filename filter and the
# preview find take the last row of their box while in use.
LAYOUT_KEYS = {"1": "popup", "2": "overlay", "3": "left", "4": "right"}
LAYOUT_NAMES = {"popup": "Popup", "overlay": "Overlay", "left": "Left half", "right": "Right half"}
ROOT_ROW, BOX_TOP = 0, 1

# Tree status marks. Nerd Font glyphs need a patched font, so plain text is the default.
ICONS = {
    "plain": {"project": "", "changes": "", "hidden": "", "shown": "+ignored",
              "loading": "Git…", "error": "No Git status", "comment": "💬"},
    "nerd": {"project": "\U000f0645", "changes": "\uf47f", "hidden": "\U000f0209", "shown": "\U000f0208",
             "loading": "\uf46a Git…", "error": "\uf071 No Git status", "comment": "\uf075"},
}


def human_size(size):
    """A byte count as Emacs's mode line shows it: 512, 2.0k, 1.3M."""
    for unit in ("", "k", "M", "G"):
        if size < 1024 or unit == "G":
            return f"{size}" if not unit else f"{size:.1f}{unit}"
        size /= 1024


def theme(palette=None, folder_style=None) -> dict[str, int]:
    palette = palette or resolve_theme()
    styles = {"active": curses.A_BOLD, "header": curses.A_REVERSE | curses.A_BOLD, "modeline": curses.A_REVERSE, "modeline_dim": curses.A_REVERSE | curses.A_DIM,
              "selected": curses.A_REVERSE | curses.A_BOLD, "inactive": curses.A_DIM,
              "muted": curses.A_DIM, "hunk": curses.A_BOLD, "key": curses.A_REVERSE}
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
        "key": (p["accent"], p["selection_bg"]), "modeline": (p["text"], p["active_row_bg"]),
        "modeline_dim": (p["subtext0"], p["active_row_bg"]),
        # Comments have colours of their own: peach marks what is commented, teal what links back.
        "comment": (p["peach"], p["panel_bg"]), "badge": (p["panel_bg"], p["peach"]),
        "reference": (p["teal"], p["active_row_bg"]), "hint": (p["green"], p["active_row_bg"]),
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
    if "key" in styles:
        styles["key"] |= curses.A_BOLD
    if p["selection_bg"] == p["panel_bg"]:
        styles["selected"] |= curses.A_REVERSE
        styles["header"] |= curses.A_REVERSE
        styles["key"] |= curses.A_REVERSE
    return styles


# Every key, by where it applies, for the ? popup.
KEY_GROUPS = (
    ("General", (("Tab", "Switch focus"), (":", "Command line"), ("?", "This list"), ("⌃E e", "Edit file or folder"),
                 ("⌃D", "Diff with HEAD"), ("o / O", "Open / open with"), ("c", "Changed files only"),
                 ("⌃H", "Ignored files"), ("⌃R", "Refresh"), ("⌃O", "Change root"), ("t", "Repository root"),
                 ("⌃W", "Layout"), ("⌃Y", "Popup size"), ("Esc", "Back / close"), ("⌃G", "Cancel, never close"), ("⌃Q", "Quit"))),
    ("Files", (("j k", "Move"), ("h l", "Fold / unfold"), ("=", "Fold / unfold all under"), ("Enter", "Open / enter folder"), ("Space", "Preview / fold"),
               ("H", "File history"),
               ("/", "Filter names"), ("⌃N ⌃P", "Scroll preview"),
               ("⌃F ⌃B", "Page preview"))),
    ("Preview", (("j k", "Cursor line"), ("Space b", "Page"), ("d u", "Half page"), ("g G", "Top / end"),
                 ("/", "Find"), ("n N", "Next / previous"), ("← →", "Scroll sideways"),
                 ("⌃click", "Open or follow link"), ("⌫ H", "Back from a followed link"), ("L", "Forward again"))),
    ("Diagrams", (("s", "Image / source"), ("+ -", "Zoom"), ("0", "Fit"), ("a", "Align"),
                  ("[ ]", "Previous / next"))),
)


class Navigator:
    def __init__(self, root: Path, pane_id: str, changes: bool, editor: str,
                 size: PopupSize = PopupSize(), on_resize=None, theme_loader=None,
                 folder_style=None, on_state=None, layout_loader=None, on_layout=None,
                 initial_state=None, defer_status=False, diagram_tools=None, graphics=None,
                 cell_size=None, alignment="center", on_alignment=None, close_keys=(),
                 icons="plain", on_icons=None, settings_loader=None, settings_file=None,
                 tree_width=None, on_tree_width=None, comment_store=None, agent_host=None,
                 source_terminal="", sidebar_open=True, on_sidebar=None):
        initial_state = normalize_view(initial_state, root)
        self.root, self.pane_id, self.editor = root, pane_id, editor
        self.environment_editor = editor
        self.settings_loader, self.settings_file = settings_loader, settings_file
        self.bindings = {}  # From config.toml [keys]: key -> action name or ":command".
        self.binding_rules = []  # Ordered [[keybindings]] conditions.
        self.settings_errors = ""
        self.diff_command, self.diff_pause = "", False
        self.opener = ""
        self.app_picker = None  # O: {"target", "query", "selected", "scroll", "apps"} while choosing.
        self.recent_apps = []
        self.history_mode = ""  # Project or file history, separate from the saved file view.
        self.history_path = ""
        self.history_branch = ""
        self.history_commits = []
        self.history_more = False
        self.history_selected = self.history_scroll = 0
        self.history_files = []
        self.history_file_selected = 0
        self.history_patch = False
        self.history_right_focus = False
        self.history_right_scroll = 0
        self.history_file_jump = False
        self.history_horizontal = 0
        self.history_error = ""
        self.history_patch_text = None
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
        self.preview_cursor = 0  # The preview line the cursor is on, in shown lines.
        self.selection_anchor = None  # The line where V or v started a selection, or None.
        self.selection_kind = "line"  # V selects whole lines; v selects characters.
        # The cursor's character in a source line, where v starts; want_column is where
        # j and k try to return to, as Vim's cursor does across shorter lines.
        self.anchor_column = self.preview_column = self.want_column = 0
        self.preview_focus = False
        self.active = ""
        self.content = ["Select a file and press Enter, or click it, to open it here."]
        self.source_text = ""
        self.previewable = False
        self.markdown = False
        self.vault = None  # Where a Markdown preview resolves Obsidian embeds and links.
        self.pending_anchor = None  # A followed link's #heading or #^block, found once rendered.
        self.link_history = []  # (file, preview scroll, sideways scroll) each followed link left.
        self.link_future = []  # Positions Back left, for Forward; following a new link clears it.
        self.rendered = None
        self.syntax = None
        self.language = ""
        self.active_size = None
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
        self.content_top = BOX_TOP + 1
        self.divider, self.screen_width = 26, 120
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
        # The divider dragged with the mouse: the tree's width, or None for the automatic one.
        self.tree_width, self.on_tree_width, self.dragging = tree_width, on_tree_width, False
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
        self.text_left = 0
        # Command line (":" or Alt+X): the draft while open, else None.
        self.command = None
        self.command_history, self.command_recall = [], 0
        self.command_menu = None  # Tab's completion list: {"selected", "scroll"} while open.
        self.key_help = False  # The ? popup listing every key.
        self.key_group = ""  # A pending command prefix, currently Git's g.
        self.command_cursor, self.command_killed = 0, ""  # Emacs editing: point and the last kill.
        self.query_cursor = self.find_cursor = 0  # Point in the filter and in find; the kill is shared.
        # Key sequences that close Lens, such as the host's toggle binding.
        self.close_keys, self.close_typed = [tuple(keys) for keys in close_keys], ()
        self.index = None
        self.items = []
        # Comments: line ranges collected for the target agent pane, one buffer per target.
        self.comment_store, self.agent_host = comment_store, agent_host
        self.submit_key = "\x13"
        self.composer = None  # The message editor before sending.
        self.agent_picker = None
        self.comment_view = None  # A comment's paragraph, shown when its preview icon is clicked.
        # The comment list on the right, shown while there are comments; folded to a strip or open.
        self.sidebar_open, self.on_sidebar = sidebar_open, on_sidebar
        self.sidebar_x = self.sidebar_width = self.sidebar_scroll = 0
        self.sidebar_rows = []  # (screen row, comment) of each listed comment's first row.
        self.cwd_cache = None  # (target, working directory): drawing the list must not ask Herdr each time.
        self.confirm_clear = False  # X asked to discard the comments; the next key answers.
        self.comment_buffers = {}  # Buffers kept in memory when there is no store.
        self.comment_source = comments.Target(pane_id, source_terminal or "")
        self.comment_target, self.comment_buffer = None, comments.Buffer()
        self.apply_settings()
        self.init_comments()
        self.refresh()
        if initial_state is not None:
            self.restore_state(initial_state)
        if self.settings_errors:
            self.message = self.settings_errors  # Config mistakes outrank the restore note.

    def apply_settings(self):
        self.tree_padding = 1
        if self.settings_loader is None:
            return
        chosen = self.settings_loader()
        self.editor = chosen.editor or self.environment_editor
        self.diff_command, self.diff_pause = chosen.diff, chosen.diff_pause
        self.opener = chosen.opener
        if chosen.icons:
            self.icons = chosen.icons
        if chosen.align:
            self.alignment = chosen.align
        self.tree_padding = 1 if chosen.tree_padding is None else chosen.tree_padding
        self.bindings = chosen.keys
        self.binding_rules = chosen.rules
        self.submit_key = chosen.submit
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
                "horizontal": self.horizontal, "preview_focus": self.preview_focus,
                "history_mode": self.history_mode,
                "history_path": self.history_path if self.history_mode == "file" else "",
                "history_selected": self.history_selected,
                "history_file_selected": self.history_file_selected,
                "history_right_focus": self.history_right_focus,
                "history_right_scroll": self.history_right_scroll,
                "history_horizontal": self.history_horizontal,
                "history_patch": self.history_patch}

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
        # A previewed file that is still under the new root stays in the preview.
        kept = ""
        if self.active:
            try:
                kept = (previous / self.active).relative_to(index.root).as_posix()
            except ValueError:
                pass
        self.root, self.index = index.root, index
        self.history_mode = ""
        self.pending_selection = ""
        self.query = self.search_before = ""
        self.searching = False
        self.expanded.clear()
        self.selected = self.scroll = 0
        if kept:
            self.active = kept
        else:
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
        self.preview_scroll = self.horizontal = self.preview_cursor = self.preview_column = self.want_column = 0
        self.selection_anchor = None
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
        else:
            edited = command_line.edit(self.root_draft, self.root_cursor, key, self.command_killed)
            if edited and len(edited[0]) <= 4096:
                self.root_draft, self.root_cursor, self.command_killed = edited
        return True

    def draw_root(self, screen):
        height, width = screen.getmaxyx()
        box_width = min(88, width - 2)
        x, top = (width - box_width) // 2, max(0, (height - 9) // 2)
        for y in range(top, min(height, top + 9)):
            band(screen, y, x, "", box_width, self.style("surface"))
        band(screen, top, x, "  CHANGE ROOT", box_width, self.style("header") | curses.A_BOLD)
        put(screen, top + 1, x + 2, "Absolute path, ~, or a path relative to the current root", box_width - 4, self.style("muted"))
        band(screen, top + 3, x + 2, "", box_width - 4, self.style("selected"))
        self.draw_field(screen, top + 3, x + 2, box_width - 4, self.root_draft, self.root_cursor, self.style("selected"))
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
        if state["history_mode"]:
            self.open_history(file=state["history_mode"] == "file", path=state["history_path"])
            if self.history_mode:
                for _ in range(20):
                    if not self.history_more or len(self.history_commits) > state["history_selected"]:
                        break
                    self.history_load_more()
                self.history_selected = min(state["history_selected"], len(self.history_commits) - 1)
                self.history_select()
                self.history_file_selected = min(state["history_file_selected"], max(0, len(self.history_files) - 1))
                self.history_right_focus = state["history_right_focus"]
                self.history_right_scroll = state["history_right_scroll"]
                self.history_horizontal = state["history_horizontal"]
                self.history_patch = state["history_patch"] and self.history_mode == "project"
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
        elif key in LAYOUT_KEYS:
            chosen = LAYOUT_KEYS[key]
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
                    self.message = f"Layout: {LAYOUT_NAMES[chosen]}"
                except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as error:
                    self.message = f"Could not switch layout: {error}"
        return True

    def draw_layout(self, screen):
        height, width = screen.getmaxyx()
        box_width = min(62, width - 2)
        x, top = (width - box_width) // 2, max(0, (height - 10) // 2)
        for y in range(top, min(height, top + 10)):
            band(screen, y, x, "", box_width, self.style("surface"))
        band(screen, top, x, "  LAYOUT", box_width, self.style("header") | curses.A_BOLD)
        lines = [f"  Current: {LAYOUT_NAMES.get(self.layout, self.layout)}", "",
                 "  1 Popup       Open a floating window",
                 "  2 Overlay     Expand the navigator",
                 "  3 Left half   Share the pane, navigator on the left",
                 "  4 Right half  Share the pane, navigator on the right", "  Esc Cancel"]
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
            # "." stands for the root itself, so o and O can open it; ".." climbs out.
            self.items[:0] = [Row(".", directory=True), Row("..", directory=True)]
        self.selected = min(self.selected, max(0, len(self.items) - 1))

    def load(self, name: str):
        if name != self.active:
            self.selection_anchor = None
        self.active = name
        self.preview_scroll = self.horizontal = self.preview_cursor = self.preview_column = self.want_column = 0
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
        self.vault = None
        if self.markdown:
            path = self.index.root / name
            self.vault = obsidian_embeds.Vault(obsidian_embeds.vault_root(path, self.index.root), path)
        try:
            self.active_size = (self.index.root / name).stat().st_size
        except (OSError, AttributeError):
            self.active_size = None
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
                blocks = markdown_preview.diagram_blocks(self.source_text, self.vault)
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
                widest = width
                if source[0] == "image" and int(source[1].split("\n")[1]):
                    # Obsidian's |width is in pixels; it caps the image as it does in the app.
                    widest = min(width, max(1, round(int(source[1].split("\n")[1]) / self.cell_pixels()[0])))
                rows[source] = diagram_preview.scaled(size, width, self.body, self.cell_pixels(),
                                                      self.zoom_of(source), max_cols=widest)
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
        if (self.root_draft is None and not self.size_draft and not self.layout_dialog and self.app_picker is None
                and not self.comment_dialog()):
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
            if self.markdown and not self.diagram_source:
                self.syntax, self.language = None, ""
                sizes = self.markdown_rows(width)
                if sizes:
                    self.rendered, found = markdown_preview.render_diagrams(
                        self.source_text, width, self.palette, {source: rows for source, (_, rows) in sizes.items()},
                        self.vault)
                    self.markdown_diagrams = [(line, source, sizes[source]) for line, source, _ in found]
                else:
                    self.rendered = markdown_preview.render(self.source_text, width, self.palette, self.vault)
                self.content = ["".join(span.text for span in line) for line in self.rendered]
            else:
                # Code, and Markdown shown as source: the file's own lines, which comments point at.
                self.rendered = None
                self.content = self.source_text.splitlines() or ["(Empty file)"]
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
        if self.pending_anchor:
            self.jump_to_anchor()

    def span_style(self, style, background=None):
        """A span's curses style; background replaces the panel colour behind unshaded text."""
        attributes = (curses.A_BOLD if style.bold else 0) | (curses.A_UNDERLINE if style.underline else 0)
        if style.italic:
            attributes |= getattr(curses, "A_ITALIC", 0)
        if not curses.has_colors():
            return attributes | (curses.A_REVERSE if background is not None else 0)
        foreground = style.foreground if style.foreground >= 0 else self.palette["text"]
        background = style.background if style.background >= 0 else (
            self.palette["panel_bg"] if background is None else background)
        colors = (terminal_color(foreground, curses.COLORS), terminal_color(background, curses.COLORS, background=True))
        if colors not in self.color_pairs:
            number = 32 + len(self.color_pairs)  # After the named pairs theme() sets up.
            if number >= min(curses.COLOR_PAIRS, 256):
                return self.style("base") | attributes
            try:
                curses.init_pair(number, *colors)
            except curses.error:
                return self.style("base") | attributes
            self.color_pairs[colors] = curses.color_pair(number)
        return self.color_pairs[colors] | attributes

    def draw_styled_line(self, screen, y, x, width, spans, background=None):
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
                put(screen, y, x + start, "".join(visible), width - start,
                    self.span_style(span.style, background))

    def activate(self, screen=None, fold=False):
        """Enter: open a file or make a folder the root. A click folds instead."""
        if not self.items:
            return
        row = self.items[self.selected]
        if row.path == "..":
            self.parent_root()
        elif row.path == ".":
            self.message = "This folder: o opens it, O opens it with an application"
        elif row.directory and not fold:
            if self.change_root(row.path):
                self.selected = min(2, len(self.items) - 1)  # The first entry, below "." and "..".
        elif row.directory:
            self.toggle_fold(row)
        else:
            self.preview_selected()
            if self.changes:
                self.show_diff(screen)

    def toggle_fold(self, row):
        if row.path in self.expanded:
            self.expanded.remove(row.path)
        else:
            self.expanded.add(row.path)
        self.rebuild()

    def fold_tree(self):
        """Unfold the selected folder and every folder under it, or fold them once all are open; "." is the whole tree."""
        if self.index is None or not self.items:
            return
        row = self.items[self.selected]
        if not row.directory or row.path == "..":
            return  # Nothing to fold under a file, and ".." lies outside the root.
        prefix = "" if row.path == "." else row.path + "/"
        names = [name for name in self.index.files if not self.changes or name in self.index.status]
        parents = {name.rpartition("/")[0] for name in names}
        if not self.changes:
            parents.update(self.index.directories)
        folders = set()
        for folder in parents:
            while folder and (folder == row.path or folder.startswith(prefix)):
                folders.add(folder)
                folder = folder.rpartition("/")[0]
        if folders <= self.expanded:
            self.expanded -= folders
        else:
            self.expanded |= folders
        self.rebuild()
        # The folder stays visible either way, so the selection stays on it.
        self.selected = next((i for i, entry in enumerate(self.items) if entry.path == row.path), self.selected)

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

    def edit_target(self):
        """What the editor opens: the preview's file, else the selected file or folder."""
        if self.preview_focus:
            return self.active
        return self.items[self.selected].path if self.items else ""

    def edit(self, screen):
        name = self.edit_target()
        if not name:
            return
        try:
            if name == "..":
                path = self.root.parent
            else:
                path = checked_path(self.root, name) if name != "." else self.root
            if path.is_dir():
                # Editors such as Vim and Emacs browse a folder they are given.
                line = None
            elif not path.is_file():
                raise ValueError("File no longer exists; use diff to inspect deletions")
            else:
                # Code and plain text previews show source lines; start the editor there.
                line = self.preview_cursor + 1 if self.preview_focus and name == self.active and self.source_view() else 1
            command = editor_command(self.editor, path, line)
            result = self.run_terminal(screen, command, self.root)
            self.refresh()
            self.message = f"Editor exited with status {result.returncode}"
        except (OSError, ValueError, subprocess.SubprocessError) as error:
            self.message = str(error)

    def launch_target(self):
        """What o and O open: the preview's file, else the selected row."""
        if self.preview_focus and self.active:
            return self.active
        return self.items[self.selected].path if self.items else ""

    def launch(self, name=None, app=None):
        """Hand a file or folder to the OS, or to app."""
        if name is None:
            name = self.launch_target()
        if app:
            self.recent_apps = [app] + [known for known in self.recent_apps if known != app][:9]
        try:
            if name == "..":
                path = self.root.parent
            elif Path(name).expanduser().is_absolute():
                path = Path(name).expanduser()
            else:
                path = checked_path(self.root, name) if name else self.root
            if not path.exists():
                raise ValueError(f"No such file: {name}")
            self.detach(application_command(app, path) if app else opener_command(self.opener, path))
            self.message = f"Opened {path.name or path}" + (f" with {app}" if app else "")
        except (OSError, ValueError, subprocess.SubprocessError) as error:
            self.message = str(error)

    def detach(self, command):
        # Detached: a GUI application must not hold the terminal or block Lens.
        process = subprocess.Popen(command, cwd=self.root,
                                   stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
                                   stderr=subprocess.PIPE, start_new_session=True)
        try:
            _, error = process.communicate(timeout=2)
        except subprocess.TimeoutExpired:
            error = None  # Still running: the application took it.
        if process.returncode:
            detail = (error or b"").decode(errors="replace").strip().splitlines()
            raise ValueError(detail[-1] if detail else f"Open command exited with status {process.returncode}")

    def link_at(self, x, y):
        """The web address drawn at a screen cell of the preview, or None."""
        number = self.preview_scroll + y - self.content_top
        column = x - self.text_left + self.horizontal
        if (not self.active or self.diagram_view() or not 0 <= y - self.content_top < self.body
                or column < 0 or number >= len(self.content)):
            return None
        styled = self.rendered if self.rendered is not None else self.syntax
        spans = styled[number] if styled is not None else [markdown_preview.Span(clean(self.content[number]))]
        text, start = "", 0
        for span in spans:
            if start <= column < start + cells(span.text) and span.link:
                return span.link  # A Markdown link's text as well as its address.
            text, start = text + span.text, start + cells(span.text)
        for match in markdown_preview.WEB_ADDRESS.finditer(text):
            address = match[0].rstrip(".,;:!?'\"")
            # A closing bracket ends the address unless the address opened it, as Wikipedia's do.
            while address[-1] in ")]>" and address.count(address[-1]) > address.count(OPENING[address[-1]]):
                address = address[:-1].rstrip(".,;:!?'\"")
            left = cells(text[:match.start()])
            if left <= column < left + cells(address):
                return address
        return None

    def follow(self, target):
        """Open a linked note in the preview, at its heading or block; other files go to the OS."""
        path, _, subpath = target.rpartition("#")
        if Path(path).suffix.lower() not in obsidian_embeds.NOTE_SUFFIXES:
            self.launch(path)
            return
        origin = (self.active, self.preview_scroll, self.horizontal)
        self.open_file(path)
        if self.active != origin[0] or subpath:
            self.link_history = [*self.link_history, origin][-MAX_LINK_HISTORY:]
            self.link_future = []
        if subpath and self.active and (self.root / self.active).resolve() == Path(path):
            self.pending_anchor = subpath  # Rendered lines exist only after the next draw.

    def link_step(self, forward=False):
        """Back: return to where the last followed link left. Forward: undo a Back."""
        source, target = (self.link_future, self.link_history) if forward else (self.link_history, self.link_future)
        here = (self.active, self.preview_scroll, self.horizontal)
        while source:
            name, scroll, horizontal = source.pop()
            if self.index and name in self.index.files:
                target.append(here)
                del target[:-MAX_LINK_HISTORY]
                self.open_file(name)
                # The next draw renders the file, then clamps this to its length.
                self.preview_scroll, self.horizontal = scroll, horizontal
                self.message = f"{'Forward' if forward else 'Back'} to {name}"
                return
        self.message = "No link to go forward to" if forward else "No followed link to go back from"

    def jump_to_anchor(self):
        anchor, self.pending_anchor = self.pending_anchor, None
        normalize = lambda text: " ".join(clean(text).split()).lower()
        if anchor.startswith("^"):
            block = obsidian_embeds.section(self.source_text, anchor) or ""
            last = obsidian_embeds.LIST_ITEM.sub("", (block.strip().splitlines() or [""])[-1])
            # Rendered text has no Markdown markers, so match a few plain words of the block.
            wanted = " ".join(re.sub(r"[*_`~=\[\]]", "", last).split()[:4]).lower()
            found = lambda line: wanted and wanted in normalize(line)
        else:
            wanted = normalize(anchor.split("#")[-1])
            found = lambda line: normalize(line).lstrip("# ") == wanted
        for number, line in enumerate(self.content):
            if found(line):
                self.preview_scroll = self.preview_cursor = number
                return
        self.message = f"No #{anchor} in {self.active}"

    def open_link(self, x, y):
        """Ctrl-click: follow a vault link in Lens, or hand a web address to the OS."""
        address = self.link_at(x, y)
        if address is None:
            self.message = "No link under the pointer"
            return
        if address.startswith(markdown_preview.FILE_LINK):
            self.follow(address[len(markdown_preview.FILE_LINK):])
            return
        try:
            self.detach(opener_command("", address))
            self.message = f"Opened {address}"
        except (OSError, ValueError, subprocess.SubprocessError) as error:
            self.message = str(error)

    def begin_app_picker(self):
        try:
            apps = command_line.applications()
        except OSError as error:
            apps, self.message = [], f"Could not list applications: {error}"
        self.app_picker = {"target": self.launch_target(), "query": "", "cursor": 0, "selected": 0, "scroll": 0, "apps": apps}

    def app_choices(self):
        """Applications matching the picker's query: recent ones first, then name prefixes, then the rest."""
        picker = self.app_picker
        query = picker["query"].lower()
        recent = [app for app in self.recent_apps if query in app.lower()]
        rest = [app for app in picker["apps"] if query in app.lower() and app not in recent]
        rest.sort(key=lambda app: not app.lower().startswith(query))
        return recent + rest

    def app_picker_key(self, key):
        picker = self.app_picker
        choices = self.app_choices()
        if key == "\x1b":
            self.app_picker = None
        elif key in ("\n", "\r", curses.KEY_ENTER):
            # With no match, the typed text is used as is: an unlisted app or a command.
            app = choices[picker["selected"]] if choices else picker["query"].strip()
            self.app_picker = None
            if app:
                self.launch(picker["target"], app)
        elif key in (curses.KEY_UP, curses.KEY_DOWN, "\x10", "\x0e", curses.KEY_PPAGE, curses.KEY_NPAGE):
            step = {curses.KEY_UP: -1, "\x10": -1, curses.KEY_DOWN: 1, "\x0e": 1,
                    curses.KEY_PPAGE: -10, curses.KEY_NPAGE: 10}[key]
            picker["selected"] = max(0, min(len(choices) - 1, picker["selected"] + step))
        else:
            edited = command_line.edit(picker["query"], picker["cursor"], key, self.command_killed)
            if edited:
                if edited[0] != picker["query"]:
                    picker["selected"] = 0
                picker["query"], picker["cursor"], self.command_killed = edited
        return True

    def draw_app_picker(self, screen):
        picker, choices = self.app_picker, self.app_choices()
        empty = f"Enter opens with \"{picker['query']}\"" if picker["query"] else "No applications found"
        self.draw_picker(screen, picker, f"OPEN WITH  {picker['target'] or '.'}", picker["query"],
                         [(app, "recent" if app in self.recent_apps else "") for app in choices], empty,
                         "↑↓ Choose  Enter Open  ⌃U Clear  Esc Cancel", cursor=picker["cursor"])

    def draw_picker(self, screen, picker, title, query, choices, empty, hints, cursor=None):
        """A centred list box: a title, the typed query, (label, note) choices and a key-hint footer."""
        height, width = screen.getmaxyx()
        box_width = min(64, width - 2)
        rows = max(1, min(14, height - 10))
        box_height = rows + 5
        x, top = (width - box_width) // 2, max(0, (height - box_height) // 2)
        for y in range(top, min(height, top + box_height)):
            band(screen, y, x, "", box_width, self.style("surface"))
        band(screen, top, x, f"  {title}", box_width, self.style("header") | curses.A_BOLD)
        cursor = len(query) if cursor is None else cursor
        band(screen, top + 1, x + 2, "› ", box_width - 4, self.style("selected"))
        self.draw_field(screen, top + 1, x + 4, box_width - 6, query, cursor, self.style("selected"))
        selected = picker["selected"]
        if selected < picker["scroll"]:
            picker["scroll"] = selected
        elif selected >= picker["scroll"] + rows:
            picker["scroll"] = selected - rows + 1
        for offset, (label, note) in enumerate(choices[picker["scroll"]:picker["scroll"] + rows]):
            index = picker["scroll"] + offset
            style = self.style("selected") | curses.A_BOLD if index == selected else self.style("surface")
            band(screen, top + 2 + offset, x + 2, f" {label}", box_width - 4, style)
            if note:
                room = max(0, min(cells(note), box_width - cells(label) - 10))
                if room:
                    put(screen, top + 2 + offset, x + box_width - 3 - room, note, room, self.style("muted"))
        if not choices:
            put(screen, top + 2, x + 3, empty, box_width - 6, self.style("muted"))
        count = f"{selected + 1 if choices else 0}/{len(choices)}"
        put(screen, top + box_height - 2, x + 2, f"{hints}   {count}", box_width - 4, self.style("active"))

    # Comments: V selects preview lines, A adds them with a note, S edits and sends them.

    def init_comments(self):
        target = self.comment_source
        if self.comment_store is not None:
            try:
                remembered = self.comment_store.load_target(self.comment_source)
            except (OSError, ValueError):
                remembered = None
            # The last chosen agent, while that pane still runs the same terminal.
            if remembered is not None and remembered != target and self.target_pane(remembered) is not None:
                target = remembered
        self.use_target(target)

    def use_target(self, target):
        self.comment_target = target
        if self.comment_store is None:
            self.comment_buffer = self.comment_buffers.setdefault(target, comments.Buffer())
            return
        try:
            self.comment_buffer = self.comment_store.load(target)
        except (OSError, ValueError) as error:
            self.comment_buffer = comments.Buffer()
            self.message = f"Could not read comments: {error}"

    def save_comments(self):
        if self.comment_store is None:
            return
        try:
            self.comment_store.save(self.comment_target, self.comment_buffer)
        except (OSError, ValueError) as error:
            self.message = f"Could not save comments: {error}"

    def target_pane(self, target):
        """The target's live pane, or None once it is closed or runs another terminal."""
        if self.agent_host is None:
            return None
        try:
            pane = self.agent_host.pane(target.pane_id)
        except (OSError, ValueError, RuntimeError):
            return None
        if target.terminal_id and pane.get("terminal_id") != target.terminal_id:
            return None
        return pane

    def comment_dialog(self):
        return self.composer is not None or self.agent_picker is not None or self.comment_view is not None

    def toggle_selection(self, kind="line"):
        """V selects lines and v characters, as in Vim: the same key again ends the selection,
        the other key switches its kind."""
        if not self.source_view():
            self.message = ("Comments need the source: press s to show the Markdown source" if self.markdown
                            else "Comments need a text preview")
            return
        if self.selection_anchor is not None and kind == self.selection_kind:
            self.selection_anchor = None
            return
        self.clamp_cursor()
        self.preview_column = self.clamped_column(self.preview_cursor, self.preview_column)
        if self.selection_anchor is None:
            self.selection_anchor, self.anchor_column = self.preview_cursor, self.preview_column
        elif kind == "char":
            self.anchor_column = 0  # From a line selection: its first line, from the start.
        self.selection_kind = kind
        self.message = ("Select text: h l w b 0 ^ $ and j k extend, A copies it into the message, Esc cancels" if kind == "char"
                        else "Select lines: j k extend, A adds a comment, Esc cancels")

    def source_line(self, number):
        lines = self.source_text.splitlines()
        return lines[number] if 0 <= number < len(lines) else ""

    def clamped_column(self, number, column):
        return max(0, min(column, len(self.source_line(number)) - 1))

    def char_selecting(self):
        return self.selection_anchor is not None and self.selection_kind == "char" and self.source_view()

    def char_range(self):
        """((line, column), (line, column)) of a v selection, first to last, both inclusive."""
        ends = sorted(((self.selection_anchor, self.anchor_column), (self.preview_cursor, self.preview_column)))
        return ends[0], ends[1]

    def move_column(self, key):
        """h l w b 0 ^ $ along a source line. w and b continue onto the next or previous line."""
        number, column = self.preview_cursor, self.preview_column
        line = self.source_line(number)
        kind = lambda char: 0 if char.isspace() else 1 if char.isalnum() or char == "_" else 2
        if key == "h":
            column -= 1
        elif key == "l":
            column += 1
        elif key == "0":
            column = 0
        elif key == "^":
            column = len(line) - len(line.lstrip()) if line.strip() else 0  # The first character that is not a space.
        elif key == "$":
            column = len(line) - 1
        elif key == "w":
            if column < len(line):
                start = kind(line[column])
                while column < len(line) and kind(line[column]) == start and start:
                    column += 1
            while column < len(line) and line[column].isspace():
                column += 1
            if column >= len(line) and number + 1 < len(self.content):
                number, column = number + 1, 0
                following = self.source_line(number)
                column = len(following) - len(following.lstrip()) if following.strip() else 0
        elif key == "b":
            column -= 1
            while True:  # Back over spaces, and line ends, to the previous word.
                while column >= 0 and line[column].isspace():
                    column -= 1
                if column >= 0 or number == 0:
                    break
                number -= 1
                line = self.source_line(number)
                column = len(line) - 1
            if column >= 0:
                start = kind(line[column])
                while column > 0 and kind(line[column - 1]) == start:
                    column -= 1
        self.preview_cursor, self.preview_column = number, self.clamped_column(number, column)
        self.want_column = self.preview_column
        self.show_cursor()
        text = self.source_line(number)
        # Bring the column into view when a long line is scrolled sideways.
        point = len(clean(text[:self.preview_column]))
        self.reveal((number, point, point + 1))

    def begin_comment(self):
        if not self.preview_focus:
            # In the tree, a comment names the selected file or folder as a whole.
            row = self.items[self.selected] if self.items else None
            if row is None or row.path == "..":
                self.message = "Select a file or folder to comment on"
                return
            path = self.root if row.path == "." else self.root / row.path
            self.add_comment(str(path.resolve()), 0, 0, "")
            return
        if not self.source_view():
            self.message = ("Comments need the source: press s to show the Markdown source"
                            if self.preview_focus and self.markdown else "Open a text file in the preview to comment on it")
            return
        self.clamp_cursor()
        characters = self.char_range() if self.char_selecting() else None
        if characters:
            (first, start), (last, end) = characters
        else:
            first, last = self.selected_lines() or (self.preview_cursor, self.preview_cursor)
        path = self.root / self.active
        lines = comments.read_lines(path)
        if lines is None or last >= len(lines):
            self.message = "Those lines are not in the file; press Ctrl+R to reload it"
            return
        if characters:
            # Selected text is not a comment: it goes to the kill ring, and the message opens
            # so C-y can put it wherever it belongs.
            end = min(end, max(0, len(lines[last]) - 1))
            if first == last:
                copied = lines[first][start:end + 1]
            else:
                copied = "\n".join([lines[first][start:], *lines[first + 1:last], lines[last][:end + 1]])
            self.command_killed = copied
            self.selection_anchor = None
            self.begin_send(empty=True)
            if self.composer is not None:
                # The paste goes after a blank line, unless it starts the message.
                if self.composer["text"].strip():
                    self.composer["text"] = self.composer["text"].rstrip("\n") + "\n\n"
                self.composer["cursor"] = len(self.composer["text"])
                self.composer["hint"] = f"Copied {len(copied)} character{'' if len(copied) == 1 else 's'} · C-y pastes"
            return
        self.add_comment(str(path.resolve()), first + 1, last + 1, comments.lines_digest(lines[first:last + 1]))

    def add_comment(self, path, start, end, digest):
        """Add a comment and open its note."""
        comment = self.comment_buffer.add(path, start, end, "", digest)
        self.selection_anchor = None
        self.save_comments()
        self.edit_note(comment.id)

    def target_details(self):
        """(agent label, working directory, error) for the target pane."""
        if self.agent_host is None:
            return "", self.root, ""
        pane = self.target_pane(self.comment_target)
        if pane is None:
            return "", None, "The target pane is gone; choose another with :comment.target"
        cwd = pane.get("foreground_cwd") or pane.get("cwd")
        cwd = Path(cwd) if cwd and Path(cwd).is_absolute() else None
        label = pane.get("display_agent") or pane.get("agent") or ""
        return label, cwd, "" if label else "No agent is running in the target pane"

    def begin_clear(self):
        """X: ask before discarding the comments and draft, which cannot be brought back."""
        buffer = self.comment_buffer
        if not buffer.comments and buffer.draft is None:
            self.message = "No comments to discard"
            return
        count = len(buffer.comments)
        self.confirm_clear = True
        self.message = (f"Discard {count} comment{'' if count == 1 else 's'}"
                        f"{' and the message' if buffer.draft else ''}? y discards, any other key keeps them")

    def clear_key(self, key):
        self.confirm_clear = False
        if key in ("y", "Y"):
            count = len(self.comment_buffer.comments)
            self.comment_buffer.clear()
            self.save_comments()
            if not self.message.startswith("Could not"):
                self.message = f"Discarded {count} comment{'' if count == 1 else 's'}"
        else:
            self.message = "Comments kept"
        return True

    def open_composer(self, mode, text, number=None, error="", changed=()):
        self.selection_anchor = None
        self.composer = {"mode": mode, "id": number, "text": text, "cursor": len(text), "scroll": 0,
                         "list_scroll": 0, "cwd": self.comment_cwd(), "error": error, "changed": list(changed),
                         "saved": text, "hint": "", "layout": None, "list": []}

    def edit_note(self, number):
        """The note of one comment, in the editor by itself."""
        comment = self.comment_buffer.find(number)
        if comment is None:
            return
        self.close_composer()
        cwd = self.comment_cwd()
        self.open_composer("note", comment.note, number,
                           changed=[comments.reference(comment, cwd)] if comments.changed(comment) else ())

    def begin_send(self, empty=False):
        """The message to send: the text around the comments, above the comments themselves."""
        buffer = self.comment_buffer
        if not buffer.comments and buffer.draft is None and not empty:
            self.message = "No comments yet: select preview lines with V, then press A"
            return
        self.close_composer()
        label, cwd, error = self.target_details()
        self.cwd_cache = (self.comment_target, cwd)
        altered = [comments.reference(comment, cwd) for comment in buffer.comments if comments.changed(comment)]
        self.open_composer("message", buffer.draft or "", error=error, changed=altered)
        self.composer["label"] = label

    def persist_draft(self):
        """Save what is being edited, the message or a note, when it changed."""
        composer = self.composer
        if composer is None or composer["text"] == composer["saved"]:
            return
        if composer["mode"] == "note":
            self.comment_buffer.set_note(composer["id"], composer["text"])
        else:
            self.comment_buffer.draft = composer["text"] if composer["text"].strip() else None
        composer["saved"] = composer["text"]
        self.save_comments()

    def close_composer(self):
        if self.composer is not None:
            self.persist_draft()
            self.composer = None

    def comment_starts(self):
        """First preview lines of the active file's comments: line index -> comments starting there."""
        if not self.active or not self.comment_buffer.comments or not self.source_view():
            return {}
        path = str((self.root / self.active).resolve())
        starts = {}
        for comment in self.comment_buffer.comments:
            if comment.path == path and comment.start:
                starts.setdefault(comment.start - 1, []).append(comment)
        return starts

    def comment_cwd(self):
        """The target agent's working directory, asked of Herdr once per target."""
        if self.cwd_cache is None or self.cwd_cache[0] != self.comment_target:
            self.cwd_cache = (self.comment_target, self.target_details()[1])
        return self.cwd_cache[1]

    def open_comment_view(self, found):
        self.comment_view = {"ids": [comment.id for comment in found], "selected": 0, "confirm": False}

    def view_line_comments(self):
        """m: the comments on the cursor line, those starting there first, in the gutter icon's view."""
        if not self.preview_focus or not self.source_view():
            self.message = "Comments show in a code or text preview"
            return
        path, number = str((self.root / self.active).resolve()), self.preview_cursor + 1
        covering = [comment for comment in self.comment_buffer.comments
                    if comment.path == path and comment.start and comment.start <= number <= comment.end]
        if not covering:
            self.message = "No comment on this line · { and } go to the previous and next"
            return
        covering.sort(key=lambda comment: comment.start != number)
        self.open_comment_view(covering)

    def jump_comment(self, step):
        """{ and }: the cursor to the previous or next line where a comment starts."""
        starts = sorted(self.comment_starts())
        if not starts:
            self.message = "No comments in this file"
            return
        found = [line for line in starts if (line > self.preview_cursor if step > 0 else line < self.preview_cursor)]
        if not found:
            self.message = "No more comments " + ("below" if step > 0 else "above")
            return
        self.preview_cursor = found[0] if step > 0 else found[-1]
        self.show_cursor()
        position = starts.index(self.preview_cursor) + 1
        self.message = f"Comment {position}/{len(starts)} · m shows it"

    def comment_view_key(self, key):
        view = self.comment_view
        if key in ("j", "k", curses.KEY_DOWN, curses.KEY_UP, "\x0e", "\x10") and not view["confirm"]:
            step = 1 if key in ("j", curses.KEY_DOWN, "\x0e") else -1
            view["selected"] = max(0, min(len(view["ids"]) - 1, view["selected"] + step))
            return True
        number = view["ids"][view["selected"]]
        if view["confirm"]:
            self.comment_view = None
            if key in ("y", "Y"):
                self.comment_buffer.remove(number)
                self.save_comments()
                self.message = "Comment deleted"
            return True
        if key == "d":
            view["confirm"] = True
            return True
        self.comment_view = None
        if key in ("\n", "\r", curses.KEY_ENTER):
            self.edit_note(number)
        return True

    def draw_comment_view(self, screen):
        view, cwd = self.comment_view, self.comment_cwd()
        found = [comment for comment in map(self.comment_buffer.find, view["ids"]) if comment is not None]
        height, width = screen.getmaxyx()
        box_width = min(80, width - 2)
        rows = []  # (text, is it the reference)
        several = len(found) > 1
        for index, comment in enumerate(found):
            if rows:
                rows.append(("", False))
            # With several comments, a mark shows which one Enter and d act on.
            mark = ("› " if index == view["selected"] else "  ") if several else ""
            rows.extend((mark + segment, True)
                        for _, segment in wrap_rows(comments.reference(comment, cwd), box_width - 4 - len(mark)))
            note = comment.note.strip() or "(No note yet)"
            rows.extend((segment, False) for _, segment in wrap_rows(note, box_width - 4))
        room = max(1, min(16, height - 6))
        if len(rows) > room:
            rows = rows[:room - 1] + [("…", False)]
        box_height = len(rows) + 4
        x, top = (width - box_width) // 2, max(0, (height - box_height) // 2)
        for y in range(top, min(height, top + box_height)):
            band(screen, y, x, "", box_width, self.style("surface"))
        band(screen, top, x, f"  {ICONS[self.icons]['comment']} COMMENT", box_width, self.style("header") | curses.A_BOLD)
        for offset, (row, heading) in enumerate(rows):
            put(screen, top + 2 + offset, x + 2, row, box_width - 4,
                self.style("reference") | curses.A_BOLD if heading else self.style("surface"))
        hint = ("Delete this comment? y deletes, any other key keeps it" if view["confirm"]
                else ("j k Choose  " if several else "") + "Enter Edit the note  d Delete  Any other key closes")
        put(screen, top + box_height - 1, x + 2, hint, box_width - 4,
            self.style("removed") | curses.A_BOLD if view["confirm"] else self.style("active"))

    def commented_lines(self):
        """Preview lines of the active file that a comment covers, as a set of line indexes."""
        if not self.active or not self.comment_buffer.comments or not self.source_view():
            return set()
        path = str((self.root / self.active).resolve())
        return {number for comment in self.comment_buffer.comments if comment.path == path and comment.start
                for number in range(comment.start - 1, comment.end)}

    def composer_key(self, key):
        composer = self.composer
        if key == self.submit_key:
            if composer["mode"] == "note":
                self.begin_send()  # A note is saved on the way to the message it goes in.
            else:
                self.submit_comments()
        elif key == "\x1b":
            note = composer["mode"] == "note"
            self.close_composer()
            self.message = "Note saved · S shows the message" if note else "Message kept · S reopens it"
        elif isinstance(key, terminal_input.Mouse):
            if key.action == "click":
                self.composer_click(key.x, key.y)
            elif key.action in ("up", "down") and composer["mode"] == "message":
                composer["list_scroll"] = max(0, composer["list_scroll"] + (-3 if key.action == "up" else 3))
        elif isinstance(key, (str, int)):
            edited = command_line.edit_text(composer["text"], composer["cursor"], key, self.command_killed)
            limit = comments.MAX_NOTE if composer["mode"] == "note" else comments.MAX_DRAFT
            if edited and len(edited[0]) <= limit:
                if edited[0] != composer["text"]:
                    composer["hint"] = ""
                composer["text"], composer["cursor"], self.command_killed = edited
                composer["error"] = ""
        return True

    def composer_click(self, x, y):
        """A click in the text puts the point there, or shows a reference typed in it; in the message's
        comment list, a click on a reference shows it and a click on a note edits it."""
        composer = self.composer
        listed = next(((number, kind) for row, number, kind in composer["list"] if row == y), None)
        if listed is not None:
            number, kind = listed
            comment = self.comment_buffer.find(number)
            if comment is not None and kind == "reference":
                self.show_reference(comments.reference(comment, composer["cwd"]))
            elif comment is not None:
                self.edit_note(number)
            return
        layout = composer.get("layout")
        if layout is None:
            return
        area_top, left, area_rows, rows = layout
        number = composer["scroll"] + y - area_top
        if not 0 <= y - area_top < area_rows or not 0 <= number < len(rows) or x < left:
            return
        start, segment = rows[number]
        index, used = start, 0
        for char in segment:
            if used + cells(char) > x - left:
                break
            used += cells(char)
            index += 1
        composer["cursor"] = index
        text = composer["text"]
        # The whitespace-separated word under the pointer, less trailing punctuation.
        first = max(text.rfind(" ", 0, index), text.rfind("\n", 0, index)) + 1
        last = min((position for position in (text.find(" ", index), text.find("\n", index)) if position >= 0),
                   default=len(text))
        word = text[first:last].rstrip(",;.)")
        if first <= index < first + len(word) and REFERENCE_SHAPE.fullmatch(word):
            self.show_reference(word)

    def show_reference(self, word):
        """Show a reference in the preview, its range selected; what was being edited is saved."""
        match = REFERENCE.fullmatch(word)
        base = (self.composer["cwd"] if self.composer is not None else self.comment_cwd()) or self.root
        path = Path(match[1]).expanduser()
        path = path if path.is_absolute() else base / path
        try:
            path = path.resolve(strict=True)
            name = path.relative_to(self.root.resolve()).as_posix()
        except (OSError, ValueError):
            return  # Not a file under the root: only the point moves.
        self.close_composer()
        if path.is_dir():
            parent = name
            while parent and parent != ".":
                self.expanded.add(parent)
                parent = parent.rpartition("/")[0]
            self.rebuild()
            self.selected = next((i for i, row in enumerate(self.items) if row.path == name), self.selected)
            self.preview_focus = False
            self.message = f"{name}/ · S shows the message"
            return
        self.open_file(name)
        if self.active != name:
            return
        self.message = f"{word} · S shows the message"
        if not match[2]:
            return
        if not self.source_view() and self.markdown:
            self.preview_key("s")  # Line numbers count source lines.
        first, last = int(match[2]) - 1, int(match[4] or match[2]) - 1
        total = len(self.content)
        first, last = max(0, min(first, total - 1)), max(0, min(last, total - 1))
        # The cursor on the first line keeps the start in view; the selection reaches the last.
        self.selection_kind = "char" if match[3] else "line"
        self.selection_anchor, self.preview_cursor = last, first
        if match[3]:
            self.anchor_column = self.clamped_column(last, int(match[5] or match[3]) - 1)
            self.preview_column = self.want_column = self.clamped_column(first, int(match[3]) - 1)
        self.preview_scroll = max(0, min(first - max(1, self.body) // 3, max(0, self.preview_length() - self.body)))
        self.show_cursor()

    def submit_comments(self):
        composer = self.composer
        self.persist_draft()
        text = comments.compose(self.comment_buffer, composer["cwd"]).strip()
        if not text:
            composer["error"] = "The message is empty"
            return
        if self.agent_host is None:
            composer["error"] = "Sending needs Herdr"
            return
        label, _, error = self.target_details()
        if error:
            composer["error"] = error
            return
        try:
            self.agent_host.send(self.comment_target.pane_id, text)
        except (OSError, ValueError, RuntimeError) as failure:
            composer["error"] = f"Could not send: {failure}"
            return
        count = len(self.comment_buffer.comments)
        self.comment_buffer.clear()
        self.save_comments()
        self.composer = None
        self.message = f"Sent {count} comment{'' if count == 1 else 's'} to {label}"

    def draw_composer(self, screen):
        composer = self.composer
        note = composer["mode"] == "note"
        height, width = screen.getmaxyx()
        box_width = min(100, width - 2)
        box_height = max(10, min(height - 2, 30))
        x, top = (width - box_width) // 2, max(0, (height - box_height) // 2)
        for y in range(top, min(height, top + box_height)):
            band(screen, y, x, "", box_width, self.style("surface"))
        area_width = box_width - 4
        if note:
            comment = self.comment_buffer.find(composer["id"])
            reference = comments.reference(comment, composer["cwd"]) if comment else ""
            band(screen, top, x, f"  {ICONS[self.icons]['comment']} COMMENT  ", box_width, self.style("header") | curses.A_BOLD)
            put(screen, top, x + 2 + cells(f"{ICONS[self.icons]['comment']} COMMENT  "), reference, box_width - 16,
                self.style("header") | curses.A_BOLD | curses.A_UNDERLINE)
            put(screen, top + 1, x + 2, composer["error"] or "What the agent should know about these lines",
                area_width, self.style("removed") | curses.A_BOLD if composer["error"] else self.style("muted"))
        else:
            band(screen, top, x, f"  SEND TO  {composer.get('label') or 'agent'} · {self.comment_target.pane_id}",
                 box_width, self.style("header") | curses.A_BOLD)
            where = f"Paths relative to {composer['cwd']}" if composer["cwd"] else "Absolute paths"
            put(screen, top + 1, x + 2, composer["error"] or f"The message, then the comments · {where}", area_width,
                self.style("removed") | curses.A_BOLD if composer["error"] else self.style("muted"))
        if composer["changed"]:
            put(screen, top + 2, x + 2, "Changed since added: " + ", ".join(composer["changed"]), area_width,
                self.style("removed"))
        elif composer["hint"]:
            put(screen, top + 2, x + 2, composer["hint"], area_width, self.style("hint") | curses.A_BOLD)
        area_top, room = top + 3, box_height - 5
        rows = wrap_rows(composer["text"], area_width)
        # The message keeps the lower part for its comments, read-only.
        area_rows = room if note else max(3, min(len(rows) + 1, room // 3))
        self.draw_text_area(screen, composer, rows, area_top, x + 2, area_rows, area_width)
        if not composer["text"]:
            put(screen, area_top, x + 4, "Write a note for this comment" if note
                else "Anything to say around the comments (optional)", area_width - 2, self.style("muted"))
        composer["list"] = []
        if not note:
            self.draw_comment_list(screen, composer, area_top + area_rows, x + 2, top + box_height - 1, area_width)
        hints = ("Esc Save  {key} Save and review the message  Enter New line" if note else
                 "{key} Send  Esc Keep  Click a note to edit it, a reference to view it")
        put(screen, top + box_height - 1, x + 2, hints.format(key=key_label(self.submit_key)), area_width,
            self.style("active"))

    def draw_text_area(self, screen, composer, rows, area_top, left, area_rows, area_width):
        cursor_row = cursor_column = 0
        for number, (start, segment) in enumerate(rows):
            if start <= composer["cursor"] <= start + len(segment):
                cursor_row, cursor_column = number, cells(segment[:composer["cursor"] - start])
                # A cursor at a wrap point belongs to the next row, unless that row starts a new line.
                if composer["cursor"] < start + len(segment) or number + 1 == len(rows) \
                        or rows[number + 1][0] != start + len(segment):
                    break
        composer["scroll"] = max(0, min(composer["scroll"], cursor_row))
        if cursor_row >= composer["scroll"] + area_rows:
            composer["scroll"] = cursor_row - area_rows + 1
        composer["layout"] = (area_top, left, area_rows, rows)
        for offset, (start, segment) in enumerate(rows[composer["scroll"]:composer["scroll"] + area_rows]):
            put(screen, area_top + offset, left, segment, area_width, self.style("base"))
            for found in REFERENCE_SHAPE.finditer(segment):
                put(screen, area_top + offset, left + cells(segment[:found.start()]), found[0].rstrip(",;.)"),
                    area_width - cells(segment[:found.start()]), self.style("reference") | curses.A_UNDERLINE)
        y = area_top + cursor_row - composer["scroll"]
        if 0 <= y - area_top < area_rows and cursor_column < area_width:
            index = composer["cursor"]
            char = composer["text"][index:index + 1]
            char = char if char and char != "\n" else " "
            put(screen, y, left + cursor_column, char, cells(char), self.style("selected") | curses.A_REVERSE)

    def draw_comment_list(self, screen, composer, top, left, bottom, width):
        """The comments under the message, as they will be sent; each one's rows are clickable."""
        count = len(self.comment_buffer.comments)
        put(screen, top, left, f"── {count} comment{'' if count == 1 else 's'} " + "─" * width, width, self.style("gutter"))
        rows = []  # (comment ID, "reference" or "note", text)
        for comment in self.comment_buffer.comments:
            if rows:
                rows.append((None, "", ""))
            rows.extend((comment.id, "reference", segment)
                        for _, segment in wrap_rows(comments.reference(comment, composer["cwd"]), width))
            note = comment.note.strip() or "(No note · click to write one)"
            rows.extend((comment.id, "note", segment) for _, segment in wrap_rows(note, width))
        visible = max(0, bottom - top - 2)
        composer["list_scroll"] = max(0, min(composer["list_scroll"], max(0, len(rows) - visible)))
        for offset, (number, kind, text) in enumerate(rows[composer["list_scroll"]:composer["list_scroll"] + visible]):
            y = top + 1 + offset
            if number is None:
                continue
            composer["list"].append((y, number, kind))
            style = (self.style("reference") | curses.A_BOLD | curses.A_UNDERLINE if kind == "reference"
                     else self.style("muted") if text.startswith("(No note") else self.style("base"))
            put(screen, y, left, text, width, style)

    def begin_agent_picker(self):
        if self.agent_host is None:
            self.message = "Choosing an agent needs Herdr"
            return
        try:
            agents = self.agent_host.agents()
            here = self.agent_host.pane(self.pane_id)
        except (OSError, ValueError, RuntimeError) as error:
            self.message = f"Could not list agents: {error}"
            return
        self.agent_picker = {"scope": "tab", "query": "", "cursor": 0, "selected": 0, "scroll": 0,
                             "agents": agents, "tab_id": here.get("tab_id"), "workspace_id": here.get("workspace_id")}
        self.agent_picker["selected"] = next(
            (i for i, agent in enumerate(self.agent_choices()) if agent.get("pane_id") == self.comment_target.pane_id), 0)

    def agent_label(self, agent):
        name = agent.get("name") or agent.get("display_agent") or agent.get("agent") or "agent"
        title = agent.get("terminal_title_stripped") or agent.get("title") or agent.get("foreground_cwd") or ""
        return f"{name}  {title}".strip()

    def agent_choices(self):
        picker = self.agent_picker
        scope = picker["scope"]
        query = picker["query"].lower()
        return [agent for agent in picker["agents"]
                if (scope == "session" or (scope == "tab" and agent.get("tab_id") == picker["tab_id"])
                    or (scope == "workspace" and agent.get("workspace_id") == picker["workspace_id"]))
                and query in f"{self.agent_label(agent)} {agent.get('foreground_cwd') or ''}".lower()]

    def agent_picker_key(self, key):
        picker = self.agent_picker
        choices = self.agent_choices()
        if key == "\x1b":
            self.agent_picker = None
        elif key in ("\t", curses.KEY_BTAB):
            scopes = AGENT_SCOPES
            picker["scope"] = scopes[(scopes.index(picker["scope"]) + (1 if key == "\t" else -1)) % len(scopes)]
            picker["selected"] = picker["scroll"] = 0
        elif key in ("\n", "\r", curses.KEY_ENTER):
            if choices:
                agent = choices[picker["selected"]]
                self.agent_picker = None
                self.choose_target(comments.Target(agent["pane_id"], agent.get("terminal_id", "")),
                                   self.agent_label(agent))
        elif key in (curses.KEY_UP, curses.KEY_DOWN, "\x10", "\x0e", curses.KEY_PPAGE, curses.KEY_NPAGE):
            step = {curses.KEY_UP: -1, "\x10": -1, curses.KEY_DOWN: 1, "\x0e": 1,
                    curses.KEY_PPAGE: -10, curses.KEY_NPAGE: 10}[key]
            picker["selected"] = max(0, min(len(choices) - 1, picker["selected"] + step))
        else:
            edited = command_line.edit(picker["query"], picker["cursor"], key, self.command_killed)
            if edited:
                if edited[0] != picker["query"]:
                    picker["selected"] = picker["scroll"] = 0
                picker["query"], picker["cursor"], self.command_killed = edited
        return True

    def choose_target(self, target, label):
        self.use_target(target)
        if self.comment_store is not None:
            try:
                self.comment_store.save_target(self.comment_source, target)
            except (OSError, ValueError) as error:
                self.message = f"Could not remember the agent: {error}"
                return
        count = len(self.comment_buffer.comments)
        self.message = f"Comments go to {label}" + (f" · comment {count}" if count else "")

    def draw_agent_picker(self, screen):
        picker = self.agent_picker
        rows = []
        for agent in self.agent_choices():
            notes = []
            if agent.get("pane_id") == self.comment_target.pane_id:
                notes.append("target")
            if agent.get("pane_id") == self.pane_id:
                notes.append("this pane")
            if picker["scope"] != "tab":
                notes.append(agent.get("place", ""))
            notes.append(agent.get("agent_status", ""))
            rows.append((self.agent_label(agent), " · ".join(note for note in notes if note)))
        empty = "No agents here · Tab widens the scope" if picker["scope"] != "session" else "No agents found"
        self.draw_picker(screen, picker, f"SEND COMMENTS TO · {picker['scope'].upper()}", picker["query"], rows,
                         empty, "Tab Scope  ↑↓ Choose  Enter Pick  Esc Cancel", cursor=picker["cursor"])

    def draw_comment_dialogs(self, screen):
        if self.composer is not None:
            self.draw_composer(screen)
        if self.comment_view is not None:
            self.draw_comment_view(screen)
        if self.agent_picker is not None:
            self.draw_agent_picker(screen)

    def sidebar_shown(self):
        return bool(self.comment_buffer.comments) and not self.narrow

    def sidebar_for(self, width):
        """The comment list's width for a screen width, or 0 when it is not shown."""
        if not self.comment_buffer.comments or width < 90:
            return 0
        if not self.sidebar_open:
            return 2 + cells(ICONS[self.icons]["comment"])  # Folded: a strip with the icon and the count.
        return max(24, min(44, width // 4, width - self.divider_for(width) - 44))

    def toggle_sidebar(self):
        if not self.comment_buffer.comments:
            self.message = "No comments to list"
            return
        self.sidebar_open = not self.sidebar_open
        if self.on_sidebar is not None:
            try:
                self.on_sidebar(self.sidebar_open)
            except OSError as error:
                self.message = f"Could not save the comment list: {error}"

    def draw_sidebar(self, screen, x, width, bottom):
        self.sidebar_x, self.sidebar_width, self.sidebar_rows = x, width, []
        icon, count = ICONS[self.icons]["comment"], len(self.comment_buffer.comments)
        if not self.sidebar_open:
            self.panel(screen, x, width, bottom, False)
            put(screen, BOX_TOP + 1, x + 1, icon, cells(icon), self.style("comment") | curses.A_BOLD)
            for offset, char in enumerate(str(count)):
                put(screen, BOX_TOP + 2 + offset, x + 1, char, 1, self.style("comment") | curses.A_BOLD)
            return
        self.panel(screen, x, width, bottom, False, f"{icon} COMMENTS", str(count))
        cwd = self.comment_cwd()
        rows = []  # (comment, style name, text) per row, a blank row between comments.
        for comment in self.comment_buffer.comments:
            if rows:
                rows.append((None, "", ""))
            rows.append((comment, "comment", comments.reference(comment, cwd)))
            # The start of the note: its first three rows.
            lines = [line for line in comment.note.splitlines() if line.strip()]
            shown = [segment for line in lines for _, segment in wrap_rows(line, width - 4)]
            rows.extend((comment, "muted", segment) for segment in shown[:3])
            if len(shown) > 3:
                rows.append((comment, "muted", "…"))
        visible = bottom - self.content_top
        self.sidebar_scroll = max(0, min(self.sidebar_scroll, max(0, len(rows) - visible)))
        current = str((self.root / self.active).resolve()) if self.active else ""
        for offset, (comment, look, line) in enumerate(rows[self.sidebar_scroll:self.sidebar_scroll + visible]):
            y = self.content_top + offset
            if comment is None:
                continue
            style = self.style(look) | (curses.A_BOLD if look == "comment" else 0)
            self.sidebar_rows.append((y, comment, "reference" if look == "comment" else "note"))
            if look == "comment" and comment.path == current:
                band(screen, y, x + 1, "", width - 2, self.style("surface"))  # In the file previewed.
            put(screen, y, x + 2, line, width - 4, style)

    def sidebar_mouse(self, event):
        """Mouse over the comment list. Returns True when the event was its own."""
        if not self.sidebar_width or event.x < self.sidebar_x or self.narrow:
            return False
        if event.action in ("up", "down"):
            if self.sidebar_open:
                self.sidebar_scroll = max(0, self.sidebar_scroll + (-3 if event.action == "up" else 3))
            return True
        if event.action != "click":
            return True
        if not self.sidebar_open or event.y == BOX_TOP:
            self.toggle_sidebar()  # The strip opens the list; the list's title folds it.
            return True
        # A reference shows its lines; the note under it opens for editing.
        found = next(((comment, kind) for y, comment, kind in self.sidebar_rows if y == event.y), None)
        if found is not None and found[1] == "reference":
            self.show_reference(comments.reference(found[0], self.comment_cwd()))
        elif found is not None:
            self.edit_note(found[0].id)
        return True

    def run_terminal(self, screen, command, cwd, pause=False):
        self.release_image()
        terminal_input.disable()
        curses.def_prog_mode()
        curses.endwin()
        try:
            result = subprocess.run(command, cwd=cwd)
            if pause:
                # Tools that print and exit would otherwise vanish behind the redraw.
                try:
                    input("\nPress Enter to return to Lens ")
                except EOFError:
                    pass
            return result
        finally:
            curses.reset_prog_mode()
            try:
                curses.curs_set(0)
            except curses.error:
                pass
            terminal_input.enable(screen)
            screen.clear()
            screen.refresh()
            terminal_input.reset_keyboard()

    def show_diff(self, screen):
        name = self.current_file()
        if not name:
            self.message = "Select a file to compare with HEAD"
            return
        try:
            with comparison(self.index, name, self.diff_command) as (command, cwd):
                result = self.run_terminal(screen, command, cwd, pause=bool(self.diff_command) and self.diff_pause)
            tool = Path(command[0]).name
            # diff tools exit with 1 when the files differ, so only 2 and up are failures.
            failed = result.returncode > (1 if self.diff_command else 0)
            self.message = f"{tool} exited with status {result.returncode}" if failed else f"Returned from {tool}"
        except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as error:
            self.message = str(error)

    def open_history(self, *, file=False, path=""):
        if self.index is None or self.index.repository is None:
            self.message = "Git history is unavailable outside a Git repository"
            return
        name = self.current_file() if file and not path else ""
        if file and not (name or path):
            self.message = "Select a file to view its history"
            return
        try:
            path = path or ((self.root / name).relative_to(self.index.repository).as_posix() if file else "")
            branch = git_history.branch(self.index.repository)
            entries, more = git_history.commits(self.index.repository, path=path)
            if not entries:
                self.message = "No commits found for this file" if file else "No commits on this branch"
                return
            self.history_mode = "file" if file else "project"
            self.history_path, self.history_branch = path, branch
            self.history_commits, self.history_more = entries, more
            self.history_selected = self.history_scroll = 0
            self.history_right_focus = self.history_patch = False
            self.history_right_scroll = self.history_file_selected = 0
            self.history_select()
            self.message = ""
        except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as error:
            self.message = f"Could not load Git history: {error}"

    def history_select(self):
        self.history_patch = False
        self.history_patch_text = None
        self.history_horizontal = 0
        self.history_right_scroll = self.history_file_selected = 0
        self.history_file_jump = False
        self.history_error = ""
        try:
            commit = self.history_commits[self.history_selected]
            files = git_history.changed_files(self.index.repository, commit.oid)
            if self.history_mode == "file":
                files = [item for item in files if item.path == commit.path or item.previous == commit.path]
            self.history_files = files
        except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as error:
            self.history_files = []
            self.history_error = str(error)

    def history_load_more(self):
        if not self.history_more:
            return
        try:
            entries, more = git_history.commits(self.index.repository, len(self.history_commits), self.history_path)
            self.history_commits.extend(entries)
            self.history_more = more
        except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as error:
            self.history_more = False
            self.message = f"Could not load more commits: {error}"

    def history_move(self, amount):
        target = self.history_selected + amount
        if target >= len(self.history_commits) and self.history_more:
            self.history_load_more()
        target = max(0, min(target, len(self.history_commits) - 1))
        if target != self.history_selected:
            self.history_selected = target
            self.history_select()

    def history_lines(self):
        commit = self.history_commits[self.history_selected]
        heading = [commit.subject, f"{commit.oid[:12]}  {commit.author}  {commit.date}"]
        if self.history_patch or self.history_mode == "file":
            if not self.history_files:
                return heading + ["", self.history_error or "No file diff in this commit"], -1
            try:
                changed = self.history_files[self.history_file_selected]
                if self.history_patch_text is None:
                    self.history_patch_text = git_history.patch(self.index.repository, commit.oid, changed)
                return heading + ["", *self.history_patch_text.splitlines()], -1
            except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as error:
                return heading + ["", str(error)], -1
        body = commit.body.splitlines() if commit.body else []
        lines = heading + ([""] + body if body else []) + ["", "Changed files:"]
        first = len(lines)
        lines.extend(f"{'›' if i == self.history_file_selected else ' '} {item.status:4} {item.previous + ' → ' if item.previous else ''}{item.path}"
                     for i, item in enumerate(self.history_files))
        if not self.history_files:
            lines.append(self.history_error or "No changed files")
        return lines, first + self.history_file_selected if self.history_files else -1

    def history_key(self, key, screen):
        if isinstance(key, terminal_input.Mouse):
            over_right = self.history_right_focus if self.narrow else key.x > self.divider
            if key.action in ("up", "down"):
                amount = -3 if key.action == "up" else 3
                if over_right:
                    self.history_right_scroll = max(0, self.history_right_scroll + amount)
                else:
                    self.history_move(amount)
            elif key.action == "click" and self.content_top <= key.y < self.content_top + self.body:
                right = over_right
                self.history_right_focus = right
                if not right:
                    target = self.history_scroll + key.y - self.content_top
                    self.history_move(target - self.history_selected)
                elif self.history_mode == "project" and not self.history_patch:
                    _, first = self.history_lines()
                    target = self.history_right_scroll + key.y - self.content_top - first
                    if 0 <= target < len(self.history_files):
                        self.history_file_selected = target
            return True
        if key in ("\x1b", "\x07", curses.KEY_BACKSPACE):
            if self.history_patch:
                self.history_patch = False
                self.history_right_scroll = 0
            elif self.history_right_focus:
                self.history_right_focus = False
            elif key != "\x07":
                self.history_mode = ""
            return True
        if key == "h":
            return self.history_key("\x1b", screen)
        if key == "l":
            return self.history_key("\n", screen)
        if key in ("\t", curses.KEY_BTAB):
            self.history_right_focus = not self.history_right_focus
            return True
        if key == "\x12":
            self.refresh()
            self.open_history(file=self.history_mode == "file")
            return True
        if key == "\x17":
            self.begin_layout()
            return True
        if key in (curses.KEY_LEFT, curses.KEY_RIGHT) and self.history_right_focus \
                and (self.history_patch or self.history_mode == "file"):
            self.history_horizontal = max(0, self.history_horizontal + (-8 if key == curses.KEY_LEFT else 8))
            return True
        if key in ("\n", "\r", curses.KEY_ENTER):
            if not self.history_right_focus:
                self.history_right_focus = True
            elif self.history_mode == "project" and not self.history_patch and self.history_files:
                self.history_patch = True
                self.history_patch_text = None
                self.history_right_scroll = 0
                self.history_horizontal = 0
            return True
        movement = {"j": 1, "k": -1, curses.KEY_DOWN: 1, curses.KEY_UP: -1,
                    curses.KEY_NPAGE: self.body, curses.KEY_PPAGE: -self.body}
        if key in movement:
            amount = movement[key]
            if not self.history_right_focus:
                self.history_move(amount)
            elif self.history_mode == "project" and not self.history_patch:
                if key in ("j", "k", curses.KEY_DOWN, curses.KEY_UP):
                    self.history_file_selected = max(0, min(self.history_file_selected + amount,
                                                             len(self.history_files) - 1))
                    self.history_file_jump = bool(self.history_files)
                else:
                    self.history_right_scroll = max(0, self.history_right_scroll + amount)
            else:
                self.history_right_scroll = max(0, self.history_right_scroll + amount)
            return True
        if key in ("g", curses.KEY_HOME, "G", curses.KEY_END):
            last = key in ("G", curses.KEY_END)
            if not self.history_right_focus:
                self.history_move((len(self.history_commits) - 1 if last else 0) - self.history_selected)
            else:
                self.history_right_scroll = 1_000_000 if last else 0
            return True
        if key == " " and self.history_right_focus:
            self.history_right_scroll += self.body
        return True

    def mouse_history(self, screen=None):
        try:
            _, x, y, _, state = curses.getmouse()
        except curses.error:
            return
        if state & getattr(curses, "BUTTON4_PRESSED", 0):
            self.history_key(terminal_input.Mouse(x, y, "up"), screen)
        elif state & getattr(curses, "BUTTON5_PRESSED", 0):
            self.history_key(terminal_input.Mouse(x, y, "down"), screen)
        elif state & (curses.BUTTON1_CLICKED | curses.BUTTON1_DOUBLE_CLICKED | curses.BUTTON1_PRESSED):
            self.history_key(terminal_input.Mouse(x, y, "click"), screen)

    def draw_history(self, screen, height, width):
        bottom = height - 3
        self.content_top = BOX_TOP + 1
        self.body = bottom - self.content_top
        self.divider = max(38, min(width // 2, 62, width - 42))
        self.narrow = width < 90
        title = f"HISTORY · {self.history_path if self.history_mode == 'file' else self.history_branch}"
        put(screen, ROOT_ROW, 2, title, width - 4, self.style("active") | curses.A_BOLD)
        left_width = width - 1 if self.narrow else self.divider
        right_x = 0 if self.narrow else self.divider + 1
        right_width = width - 1 if self.narrow else width - self.divider - 2
        show_left = not self.narrow or not self.history_right_focus
        show_right = not self.narrow or self.history_right_focus
        if show_left:
            self.panel(screen, 0, left_width, bottom, not self.history_right_focus, "COMMITS",
                       f"{len(self.history_commits)}{'+' if self.history_more else ''}")
            self.history_scroll = max(0, min(self.history_scroll, self.history_selected))
            if self.history_selected >= self.history_scroll + self.body:
                self.history_scroll = self.history_selected - self.body + 1
            for offset, commit in enumerate(self.history_commits[self.history_scroll:self.history_scroll + self.body]):
                number = self.history_scroll + offset
                style = self.style("selected" if number == self.history_selected and not self.history_right_focus
                                   else "inactive" if number == self.history_selected else "base")
                band(screen, self.content_top + offset, 1, "", left_width - 2, style)
                put(screen, self.content_top + offset, 2,
                    f"{commit.date} {commit.oid[:7]} {commit.subject}", left_width - 4, style)
        if show_right:
            detail = "FILE DIFF" if self.history_mode == "file" or self.history_patch else "COMMIT DETAILS"
            self.panel(screen, right_x, right_width, bottom, self.history_right_focus, detail)
            lines, selected_line = self.history_lines()
            if selected_line >= 0 and self.history_right_focus and self.history_file_jump:
                self.history_right_scroll = max(0, min(self.history_right_scroll, selected_line))
                if selected_line >= self.history_right_scroll + self.body:
                    self.history_right_scroll = selected_line - self.body + 1
                self.history_file_jump = False
            self.history_right_scroll = max(0, min(self.history_right_scroll, max(0, len(lines) - self.body)))
            for offset, line in enumerate(lines[self.history_right_scroll:self.history_right_scroll + self.body]):
                number = self.history_right_scroll + offset
                style = (self.style("selected") if number == selected_line and self.history_right_focus
                         else self.style("added") if line.startswith("+") and not line.startswith("+++")
                         else self.style("removed") if line.startswith("-") and not line.startswith("---")
                         else self.style("hunk") if line.startswith("@@") else self.style("base"))
                if number == selected_line and self.history_right_focus:
                    band(screen, self.content_top + offset, right_x + 1, "", right_width - 2, style)
                shown = clean(line)[self.history_horizontal:] if number >= 3 and \
                    (self.history_patch or self.history_mode == "file") else line
                put(screen, self.content_top + offset, right_x + 2, shown, right_width - 4, style)
        band(screen, height - 2, 0, "", width - 1, self.style("modeline"))
        focus = "DIFF" if self.history_right_focus and (self.history_patch or self.history_mode == "file") else "DETAILS" if self.history_right_focus else "COMMITS"
        put(screen, height - 2, 0, f" {focus}  {self.history_selected + 1}/{len(self.history_commits)}  {title}",
            width - 1, self.style("modeline"))
        self.draw_echo(screen, height - 1, width)

    def style(self, name):
        return self.styles.get(name, 0)

    def panel(self, screen, x, width, bottom, focused, title="", note=""):
        """A bordered box with its title set into the top edge and a note at its right end."""
        border = self.style("active" if focused else "gutter")
        corner = ("╔", "═", "╗", "║", "╚", "╝") if focused else ("┌", "─", "┐", "│", "└", "┘")
        a, horizontal, b, vertical, c, d = corner
        put(screen, BOX_TOP, x, a + horizontal * (width - 2) + b, width, border)
        room = width - 6
        if note and cells(note) + 2 <= room // 2:
            put(screen, BOX_TOP, x + width - 3 - cells(note) - 1, f" {note} ", cells(note) + 2, border)
            room -= cells(note) + 3
        if title and room > 3:
            if cells(title) > room:
                title = "…" + title[-(room - 1):]  # Keep the end of a long path: the file name.
                while cells(title) > room:
                    title = "…" + title[2:]
            put(screen, BOX_TOP, x + 2, f" {title} ", cells(title) + 2,
                self.style("header" if focused else "surface") | curses.A_BOLD)
        put(screen, bottom, x, c + horizontal * (width - 2) + d, width, border)
        for y in range(BOX_TOP + 1, bottom):
            put(screen, y, x, vertical, 1, border)
            put(screen, y, x + width - 1, vertical, 1, border)

    def draw_tree(self, screen, x, width, bottom):
        focused = not self.preview_focus
        icons = ICONS[self.icons]
        icon = icons["changes" if self.changes else "project"]
        title = "CHANGED FILES" if self.changes else "PROJECT FILES"
        flag = icons["shown" if self.include_ignored else "hidden"]  # Ctrl+H toggles.
        git = (icons["loading"] if self.index and self.index.status_pending
               else icons["error"] if self.index and self.index.status_error else "")
        self.panel(screen, x, width, bottom, focused, f"{icon} {title}" if icon else title,
                   f"{git}  {flag}" if git else flag)
        if self.searching or self.query:
            # The filter sits at the foot of the tree, like a minibuffer under its window.
            count = f"{len(self.items)} match{'' if len(self.items) == 1 else 'es'}" if self.query.strip() else ""
            self.query_line(screen, x + 1, width - 2, self.query, " Type part of a name or path",
                            self.searching, count, y=bottom - 1, cursor=self.query_cursor)
        if not self.items:
            empty = "Loading Git status…" if self.index and self.index.status_pending else "Git status unavailable" if self.index and self.index.status_error else "No matching files"
            put(screen, self.content_top, x + 2, empty, width - 4, self.style("muted"))
        pad = self.tree_padding
        for offset, row in enumerate(self.items[self.scroll:self.scroll + self.tree_body]):
            selected = self.selected == self.scroll + offset
            style = self.style("folder" if row.directory else "base")
            if selected:
                style = self.style("inactive" if self.preview_focus else "selected")
            opened = row.path in self.expanded and row.path not in (".", "..")
            # The open or closed folder says enough; files line up after the glyph's width.
            marker = ("\uf07c " if opened else "\uf07b ") if row.directory else "  "
            label = row.path if self.query else row.path.rsplit("/", 1)[-1]
            # Inside Git the status column is always there, so rows do not shift when status arrives.
            status = self.index.status.get(row.path, "  ") + " " if self.index.repository else ""
            text = f"{' ' * pad}{status}{'  ' * row.depth}{marker}{label}"
            band(screen, self.content_top + offset, x + 1, "", width - 2, style)
            put(screen, self.content_top + offset, x + 1, text, width - 2 - pad, style)
            if self.query.strip() and row.path not in (".", ".."):
                self.draw_match(screen, self.content_top + offset, x + 1 + cells(text) - cells(label),
                                x + width - 1 - pad, label, selected)

    def draw_match(self, screen, y, left, right, label, selected):
        """Redraw a filter result: its folder dimmed, the matched characters in the accent colour."""
        marks = highlights(label, self.query)
        folder = label.rfind("/") + 1
        base = self.style("inactive" if self.preview_focus else "selected") if selected else self.style("base")
        column = left
        for index, char in enumerate(label):
            size = cells(char)
            if column + size > right:
                break
            if index in marks:
                style = (self.style("key") if selected else self.style("active")) | curses.A_BOLD
            elif index < folder:
                style = base | curses.A_DIM if selected else self.style("muted")
            else:
                style = base
            put(screen, y, column, char, size, style)
            column += size

    def draw_field(self, screen, y, x, width, text, cursor, style, editing=True):
        """Typed text with a block cursor over the character at point, the way every text field
        shows point. Text scrolls sideways to keep point visible. Returns the column after it."""
        start = 0
        # One cell for the cursor past the end, and one for the "…" once the start is hidden.
        while start < cursor and cells(text[start:cursor]) + 1 + (1 if start else 0) > width:
            start += 1
        shown = ("…" if start else "") + text[start:]
        point = cursor - start + (1 if start else 0)
        put(screen, y, x, shown, width, style)
        column = x + cells(shown[:point])
        if editing and column < x + width:
            char = shown[point:point + 1] or " "
            put(screen, y, column, char, cells(char), style | curses.A_REVERSE)
        return x + cells(shown) + (1 if editing and point == len(shown) else 0)

    def query_line(self, screen, left, width, text, placeholder, editing, note, y, cursor=None):
        """A query row in a box: ⌕, the text with a cursor at point while editing, a note on the right."""
        right = left + width
        band(screen, y, left, "", width, self.style("surface"))
        put(screen, y, left + 1, "\u2315", 1, self.style("active") | curses.A_BOLD)
        x = left + 3
        point = len(text) if cursor is None else cursor
        end = self.draw_field(screen, y, x, right - x - 1, text, point, self.style("base") | curses.A_BOLD, editing)
        if not text:
            x += 1 if editing else 0
            put(screen, y, x, placeholder, right - x - 1, self.style("muted"))
        x = max(x, end)
        if note and right - cells(note) - 1 > x + 2:
            put(screen, y, right - cells(note) - 1, note, cells(note), self.style("muted"))

    def draw_content(self, screen, x, width, bottom):
        note = ""
        if self.diagram_file():
            note = "source" if self.diagram_source else f"{round(self.zoom_of(self.diagram_list[0]) * 100)}%"
        elif self.markdown and self.diagram_source:
            note = "source"
        elif self.markdown and self.diagram_list and self.rendered is not None:
            current = self.current_diagram()
            keys = [key for _, key, _ in self.markdown_diagrams]
            if self.diagram_source:
                note = "diagram source"
            elif current in keys:
                note = f"diagram {keys.index(current) + 1}/{len(keys)} · {round(self.zoom_of(current) * 100)}%"
        self.panel(screen, x, width, bottom, self.preview_focus, self.active or "No file selected", note)
        if self.finding or (self.find_query and self.active):
            total = len(self.matches()) if self.find_query else 0
            found = (f"{self.find_index + 1}/{total}" if total and self.find_index >= 0
                     else f"{total} found" if self.find_query else "")
            self.query_line(screen, x + 1, width - 2, self.find_query, " Type text to find in the preview",
                            self.finding, found, y=bottom - 1, cursor=self.find_cursor)
        if self.diagram_view():
            self.draw_diagram(screen, x, width)
            return
        self.text_width = width - (4 if self.rendered is not None else 10)
        self.text_left = x + (2 if self.rendered is not None else 8)
        highlight = bool(self.find_query) and bool(self.matches())
        chosen = self.selected_lines()
        marked = self.commented_lines()
        starts = self.comment_starts()
        for offset, line in enumerate(self.content[self.preview_scroll:self.preview_scroll + self.body]):
            y = self.content_top + offset
            number = self.preview_scroll + offset
            # The selection, else the cursor line, shades the row behind the text.
            look, shade = None, None
            if chosen and chosen[0] <= number <= chosen[1]:
                look, shade = self.style("selected"), self.palette["selection_bg"]
            elif self.preview_focus and number == self.preview_cursor and self.cursor_view():
                look, shade = self.style("surface"), self.palette["active_row_bg"]
            if self.rendered is not None:
                if look is not None:
                    band(screen, y, x + 1, "", width - 2, look)
                self.draw_styled_line(screen, y, x + 2, width - 4, self.rendered[number], shade)
            elif self.active:
                gutter = self.style("active") | curses.A_BOLD if look is not None else self.style("gutter")
                put(screen, y, x + 1, f"{number + 1:5} │", 7, gutter)
                if number in marked:
                    # A comment covers this line: its number and a heavy bar in the comment colour.
                    put(screen, y, x + 1, f"{number + 1:5} ┃", 7, self.style("comment") | curses.A_BOLD)
                if number in starts:
                    # Where a comment starts; a click shows what the message says there.
                    put(screen, y, x + 1, ICONS[self.icons]["comment"], 2, self.style("comment") | curses.A_BOLD)
                if look is not None:
                    band(screen, y, x + 8, "", width - 9, look)
                if self.syntax is not None:
                    self.draw_styled_line(screen, y, x + 8, width - 10, self.syntax[number], shade)
                else:
                    put(screen, y, x + 8, clean(line)[self.horizontal:], width - 10, look or self.style("base"))
            else:
                put(screen, y + 1, x + 3, line, width - 6, self.style("muted"))
            if highlight and self.active:
                # Drawn over the line so the highlight wins.
                left = x + 2 if self.rendered is not None else x + 8
                self.draw_matches(screen, y, left, self.text_width, self.preview_scroll + offset)
            if self.char_selecting():
                self.draw_char_selection(screen, y, x + 8, width - 10, number)
            elif self.preview_focus and number == self.preview_cursor and self.source_view():
                self.draw_cursor_cell(screen, y, x + 8, width - 10, number)
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
        self.screen_width = width
        if height < 15 or width < 36:
            put(screen, 0, 0, "^W Layout (36 × 15 minimum)", width, curses.A_BOLD)
            if self.layout_dialog:
                self.draw_layout(screen)
            if self.size_draft:
                self.draw_size(screen)
            if self.root_draft is not None:
                self.draw_root(screen)
            if self.app_picker is not None:
                self.draw_app_picker(screen)
            self.draw_comment_dialogs(screen)
            screen.refresh()
            return
        if self.history_mode:
            self.draw_history(screen, height, width)
            if self.layout_dialog:
                self.draw_layout(screen)
            if self.size_draft:
                self.draw_size(screen)
            if self.key_help or self.key_group:
                self.draw_key_help(screen)
            if self.command_menu is not None and self.command is not None:
                self.draw_command_menu(screen)
            self.draw_comment_dialogs(screen)
            screen.refresh()
            return
        bottom = height - 3
        self.content_top = BOX_TOP + 1
        self.body = self.tree_body = bottom - self.content_top
        if self.searching or self.query:
            self.tree_body -= 1  # The filter row at the foot of the tree.
        if self.finding or (self.find_query and self.active):
            self.body -= 1  # The find row at the foot of the preview.
        self.divider = self.divider_for(width)
        self.narrow = width < 90
        sidebar = 0 if self.narrow else self.sidebar_for(width)
        content_width = width - 1 if self.narrow else width - self.divider - 2 - sidebar
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
        if self.cursor_view():
            self.clamp_cursor()
        focus = ("ROOT" if self.root_draft is not None else "COMMAND" if self.command is not None
                 else "SEARCH" if self.searching else "FIND" if self.finding
                 else "CONTENT" if self.preview_focus else "FILES")
        put(screen, ROOT_ROW, 2, "[..]", 4, self.style("active"))
        put(screen, ROOT_ROW, 8, str(self.root), width - 10, self.style("muted"))
        if self.narrow:
            if self.preview_focus:
                self.draw_content(screen, 0, width - 1, bottom)
            else:
                self.draw_tree(screen, 0, width - 1, bottom)
        else:
            self.draw_tree(screen, 0, self.divider, bottom)
            self.draw_content(screen, self.divider + 1, content_width, bottom)
            if sidebar:
                self.draw_sidebar(screen, self.divider + 1 + content_width, sidebar, bottom)
            else:
                self.sidebar_width = 0
        position = f"{self.preview_scroll + 1}/{self.preview_length()}" if self.preview_focus else f"{self.selected + 1 if self.items else 0}/{len(self.items)}"
        self.draw_mode_line(screen, height - 2, width, focus)
        self.draw_echo(screen, height - 1, width)
        if self.size_draft:
            self.draw_size(screen)
        if self.layout_dialog:
            self.draw_layout(screen)
        if self.root_draft is not None:
            self.draw_root(screen)
        if self.app_picker is not None:
            self.draw_app_picker(screen)
        self.draw_comment_dialogs(screen)
        if self.key_help or self.key_group:
            self.draw_key_help(screen)
        if self.command_menu is not None and self.command is not None:
            self.draw_command_menu(screen)
        screen.refresh()

    def command_choices(self):
        """Completion works on the text before the cursor; the text after it is kept."""
        return command_line.candidates(self.command[:self.command_cursor], self.root,
                                       self.index.files if self.index else [])

    def set_command(self, text, tail=""):
        self.command, self.command_cursor = text + tail, len(text)

    def draw_command_menu(self, screen):
        head, options = self.command_choices()
        self.command_menu["selected"] = min(self.command_menu["selected"], max(0, len(options) - 1))
        notes = {}
        if not head:
            notes = {name: command_line.lookup(name).help for name in options}
        self.draw_picker(screen, self.command_menu, "COMPLETE", f":{self.command}",
                         [(name, notes.get(name, "")) for name in options], "No completions",
                         "↑↓ Choose  Enter Insert  Esc Close", cursor=self.command_cursor + 1)

    def command_menu_key(self, key):
        """Keys while the completion list is open. Returns False for keys the command line handles."""
        menu = self.command_menu
        head, options = self.command_choices()
        steps = {curses.KEY_UP: -1, "\x10": -1, curses.KEY_BTAB: -1, curses.KEY_DOWN: 1, "\x0e": 1, "\t": 1,
                 curses.KEY_PPAGE: -10, curses.KEY_NPAGE: 10}
        if key in ("\x1b", "\x07"):
            self.command_menu = None
        elif key in ("\n", "\r", curses.KEY_ENTER):
            if options:
                option = options[min(menu["selected"], len(options) - 1)]
                self.set_command(command_line.accept(head, option), self.command[self.command_cursor:])
                # A folder leads on to its contents; anything else is finished.
                self.command_menu = {"selected": 0, "scroll": 0} if option.endswith("/") else None
            else:
                self.command_menu = None
        elif key in steps:
            if options:
                menu["selected"] = (menu["selected"] + steps[key]) % len(options) if key in ("\t", curses.KEY_BTAB) \
                    else max(0, min(len(options) - 1, menu["selected"] + steps[key]))
        else:
            menu["selected"] = menu["scroll"] = 0  # Typing narrows the list from the top.
            return False
        return True

    def command_key(self, key, screen):
        if self.command_menu is not None and self.command_menu_key(key):
            return True
        if key in ("\x1b", "\x07"):
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
            tail = self.command[self.command_cursor:]
            text, options = command_line.complete(self.command[:self.command_cursor], self.root,
                                                  self.index.files if self.index else [])
            self.set_command(text, tail)
            self.message = "" if options else "No completions"
            if len(options) > 1:
                self.command_menu = {"selected": 0, "scroll": 0}
        elif key in (curses.KEY_UP, curses.KEY_DOWN, "\x10", "\x0e"):
            step = -1 if key in (curses.KEY_UP, "\x10") else 1
            self.command_recall = max(0, min(len(self.command_history), self.command_recall + step))
            self.set_command(self.command_history[self.command_recall]
                             if self.command_recall < len(self.command_history) else "")
        elif key in ("\b", "\x7f", curses.KEY_BACKSPACE) and not self.command:
            self.command = None  # Backspace on an empty line closes it, as in Vim.
        else:
            edited = command_line.edit(self.command, self.command_cursor, key, self.command_killed)
            if edited:
                self.command, self.command_cursor, self.command_killed = edited
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
        needs = {"preview": "a file", "goto": "a line number", "find": "text", "cd": "a directory",
                 "zoom": "in, out, fit or a percent", "align": "left, center or right",
                 "layout": "popup, overlay, left or right", "icons": "nerd or plain"}
        if name in needs and not argument:
            self.message = f":{command.usage} needs {needs[name]}"
            return True
        if name == "quit":
            return False
        if name == "help":
            self.message = command_line.describe(argument)
        elif name == "preview":
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
            self.preview_cursor = max(0, min(line - 1, self.preview_length() - 1))
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
        elif name == "git.root":
            self.repository_root()
        elif name in ("git.history", "git.file-history"):
            self.open_history(file=name == "git.file-history")
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
        elif name in ("git.changes", "project"):
            self.history_mode = ""
            want = name == "git.changes"
            if self.changes != want:
                self.changes = want
                self.preview_focus = False
                self.selected = self.scroll = 0
                self.rebuild()
            self.message = "Changed files only" if want else "All project files"
        elif name == "git.ignored":
            if argument not in ("", "on", "off"):
                self.message = f":{command.usage}"
            elif argument == "" or (argument == "on") != self.include_ignored:
                self.toggle_ignored()
        elif name == "refresh":
            self.refresh()
            if self.history_mode:
                self.open_history(file=self.history_mode == "file")
            self.message = "Refreshed"
        elif name == "config":
            self.edit_settings(screen)
        elif name == "editor":
            self.edit(screen)
        elif name == "git.diff":
            self.show_diff(screen)
        elif name == "launch":
            self.launch(argument or None)
        elif name == "with":
            if argument:
                self.launch(app=argument)
            else:
                self.begin_app_picker()
        elif name == "comment.add":
            self.begin_comment()
        elif name == "comment.send":
            self.begin_send()
        elif name == "comment.target":
            self.begin_agent_picker()
        elif name == "comment.clear":
            self.begin_clear()
        elif name == "layout":
            keys = {mode: key for key, mode in LAYOUT_KEYS.items()}
            if argument not in keys:
                self.message = f":{command.usage}"
                return True
            self.begin_layout()
            if self.layout_dialog:
                return self.layout_key(keys[argument])
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
        if self.markdown and self.previewable and name in ("source", "diagram"):
            if self.diagram_source != (name == "source"):
                self.preview_key("s")
            self.message = "Markdown source" if self.diagram_source else "Rendered Markdown"
            return
        if not self.diagram_list:
            self.message = "No diagram in this preview"
            return
        if name in ("source", "diagram"):
            if self.diagram_source != (name == "source"):
                self.preview_key("s")
            self.message = "Diagram source" if self.diagram_source else "Diagram images"
            return
        if self.diagram_source:
            self.preview_key("s")
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

    def draw_mode_line(self, screen, y, width, focus):
        """The bar between the panels and the command line, as Emacs draws one above the minibuffer."""
        if self.preview_focus:
            top, shown, total = self.preview_scroll, self.body, self.preview_length()
            position = f"L{(self.preview_cursor if self.cursor_view() else top) + 1}/{total}"
            if self.source_view():
                position += f" C{self.clamped_column(self.preview_cursor, self.preview_column) + 1}"
        else:
            top, shown, total = self.scroll, self.tree_body, len(self.items)
            position = f"{self.selected + 1 if self.items else 0}/{total}"
        # Emacs's share of the view: All when it fits, Top and Bot at the ends, else a percentage.
        where = ("All" if total <= shown else "Top" if top == 0 else "Bot" if top + shown >= total
                 else f"{round(top * 100 / (total - shown))}%")
        name = self.active or self.root.name or str(self.root)
        size = human_size(self.active_size) if self.active and self.active_size is not None else ""
        style, dim = self.style("modeline"), self.style("modeline_dim")
        band(screen, y, 0, "", width - 1, style)
        x = 0
        count = len(self.comment_buffer.comments)
        for text, look in ((f" {focus} ", self.style("header") | curses.A_BOLD), (size, dim),
                           (name, style | curses.A_BOLD), (f"{position}  {where}", dim),
                           (f" comment {count} " if count else "", self.style("badge") | curses.A_BOLD)):
            if not text or x >= width - 2:
                continue
            put(screen, y, x, text, width - 2 - x, look)
            x += cells(text) + 2

    def echo_keys(self):
        """The few keys worth showing for the current state; ? lists the rest."""
        if self.key_group:
            return [(key, label.lower()) for key, label, _ in self.git_group_keys()]
        if self.command is not None:
            return [("Tab", "complete"), ("↑↓", "history"), ("Esc", "cancel")]
        if self.history_mode:
            if not self.history_right_focus:
                return [("Enter", "details" if self.history_mode == "project" else "diff"),
                        ("Tab", "switch"), ("Esc", "files"), ("?", "keys")]
            if self.history_mode == "project" and not self.history_patch:
                return [("j k", "file"), ("Enter", "diff"), ("Esc", "commits"), ("?", "keys")]
            return [("j k", "scroll"), ("Esc", "files" if self.history_mode == "project" else "commits"),
                    ("?", "keys")]
        if self.finding:
            return [("Enter", "keep"), ("⌃U", "clear"), ("Esc", "cancel")]
        if self.searching:
            return [("↑↓", "pick"), ("Enter", "apply"), ("Esc", "cancel")]
        # Send only once there is something to send: the count shows in the bar above.
        send = [("S", "review & send"), ("C", "list"), ("X", "clear")] if self.comment_buffer.comments or self.comment_buffer.draft is not None else []
        if self.preview_focus:
            if self.char_selecting():
                return [("h l w b", "move"), ("A", "copy to message"), ("Esc", "cancel")]
            if self.selection_anchor is not None:
                return [("j k", "extend"), ("A", "add comment"), ("Esc", "cancel")]
            if self.find_query:
                return [("n N", "next/prev"), ("/", "find"), (":", "command"), ("?", "keys")]
            if self.source_view():
                return [("/", "find"), ("v V", "select"), ("A", "comment"), *send, ("?", "keys")]
            return [("/", "find"), ("Tab", "files"), (":", "command"), *send, ("?", "keys")]
        return [("Space", "preview"), ("/", "filter"), ("A", "comment"), *send, ("?", "keys")]

    def draw_echo(self, screen, y, width):
        """The last row, as Emacs's echo area: the command line or the latest message on the left,
        the keys for the current state dimmed on the right."""
        band(screen, y, 0, "", width - 1, self.style("base"))
        if self.command is not None:
            style = self.style("base") | curses.A_BOLD
            put(screen, y, 0, f":{self.command}", width - 1, style)
            column = 1 + cells(self.command[:self.command_cursor])
            char = self.command[self.command_cursor:self.command_cursor + 1] or " "
            if column + cells(char) < width:
                put(screen, y, column, char, cells(char), style | curses.A_REVERSE)
            used = column + 1
        else:
            put(screen, y, 1, self.message, width - 2, self.style("base"))
            used = 1 + cells(self.message)
        keys = self.echo_keys()
        # Drop keys from the left until the rest fit beside the text.
        while keys and used + 4 + sum(cells(key) + cells(label) + 3 for key, label in keys) > width - 1:
            keys = keys[1:]
        x = width - 1 - sum(cells(key) + cells(label) + 3 for key, label in keys)
        for key, label in keys:
            put(screen, y, x, key, cells(key), self.style("active") | curses.A_BOLD)
            put(screen, y, x + cells(key) + 1, label, cells(label), self.style("muted"))
            x += cells(key) + cells(label) + 3

    def key_groups(self):
        if self.history_mode:
            common = (("Tab", "Switch panels"), (":", "Command line"), ("?", "This list"),
                      ("⌃R", "Reload history"), ("⌃W", "Layout"), ("⌃Q", "Quit"))
            if not self.history_right_focus:
                current = (("j k ↑ ↓", "Move commits"), ("PgUp PgDn", "Move a page"),
                           ("g G", "First / last loaded"), ("Enter l", "Show details"),
                           ("Esc h", "Return to files"))
                if self.history_mode == "file":
                    current = tuple((key, "Show diff" if key == "Enter l" else label)
                                    for key, label in current)
            elif self.history_mode == "project" and not self.history_patch:
                current = (("j k ↑ ↓", "Choose a file"), ("PgUp PgDn", "Scroll a page"),
                           ("g G", "Top / end"), ("Enter l", "Show file diff"),
                           ("Esc h", "Back to commits"))
            else:
                current = (("j k ↑ ↓", "Scroll diff"), ("PgUp PgDn", "Scroll a page"),
                           ("Space", "Next page"), ("← →", "Scroll sideways"), ("g G", "Top / end"),
                           ("Esc h", "Back to files" if self.history_mode == "project" else "Back to commits"))
            return self.configured_key_groups((("History", common), ("Current panel", current)))
        repository = self.index is not None and self.index.repository is not None
        general = tuple((key, label) for key, label in KEY_GROUPS[0][1]
                        if not (key == "⌃D" and (not self.current_file() or not repository))
                        and not (key in ("t", "c") and not repository)
                        and not (key == "⌃Y" and self.layout != "popup"))
        if repository and not self.preview_focus:
            general += (("g", "Git commands"),)
        panel = KEY_GROUPS[2] if self.preview_focus else KEY_GROUPS[1]
        if not self.preview_focus and (not self.current_file() or not self.index or not self.index.repository):
            panel = (panel[0], tuple((key, label) for key, label in panel[1] if key != "H"))
        groups = [("General", general), panel]
        if self.preview_focus and self.diagram_list:
            groups.append(KEY_GROUPS[3])
        notes = (("V", "Select lines"), ("v", "Select text"), ("h l w 0 ^ $", "Move in the line"),
                 ("b", "Word back, in a text selection"), ("m", "The comment on this line"),
                 ("{ }", "Previous / next comment"),
                 ("A", "Add comment, or copy the text")) if self.preview_focus \
            else (("A", "Comment on file or folder"),)
        if self.preview_focus and self.markdown:
            notes = (("s", "Rendered / source"),) + notes
        groups.append(("Comments", notes + (("S", "Review and send"), ("C", "Fold / unfold the list"),
                                            ("X", "Discard all"),
                                            (":comment.target", "Choose agent"))))
        return self.configured_key_groups(tuple(groups))

    def configured_key_groups(self, groups):
        active = self.key_context()
        chosen = {}
        for rule in self.binding_rules:
            if settings.when_matches(rule.when, active):
                chosen[rule.key] = (rule.spec, rule.target)
        if not chosen:
            return groups
        overridden = {spec for spec, _ in chosen.values() if len(spec) == 1}
        shown = []
        for title, rows in groups:
            remaining = []
            for label, description in rows:
                parts = [part for part in label.replace("/", " / ").split() if part not in overridden]
                while parts and parts[0] == "/":
                    parts.pop(0)
                while parts and parts[-1] == "/":
                    parts.pop()
                if parts:
                    remaining.append((" ".join(parts), description))
            shown.append((title, tuple(remaining)))
        custom = tuple((spec, target) for spec, target in chosen.values() if target != "none")
        if custom:
            shown.append(("Configured", custom))
        return tuple(shown)

    def git_group_keys(self):
        if self.history_mode or self.preview_focus or not self.index or not self.index.repository:
            return ()
        keys = [("p", "Project history", "git.history")]
        if self.current_file():
            keys.append(("f", "File history", "git.file-history"))
        keys.extend((("r", "Repository root", "git.root"),
                     ("c", "Changed files", "git.changes"),
                     ("i", "Ignored files", "git.ignored")))
        if self.current_file():
            keys.append(("d", "Diff with HEAD", "git.diff"))
        return tuple(keys)

    def key_context(self):
        """State names available to conditional user key bindings."""
        active = {"history" if self.history_mode else "preview" if self.preview_focus else "tree"}
        if self.index and self.index.repository:
            active.add("git")
        if self.current_file():
            active.add("file")
        if self.preview_focus and self.diagram_list:
            active.add("diagram")
        if self.changes:
            active.add("changes")
        if self.history_mode:
            active.add("historyFile" if self.history_mode == "file" else "historyProject")
        return active

    def draw_key_help(self, screen):
        """Keys for the active view and panel, grouped in a centred box."""
        groups = (("Git · g", tuple((key, label) for key, label, _ in self.git_group_keys())),) \
            if self.key_group else self.key_groups()
        height, width = screen.getmaxyx()
        key_width = max(cells(key) for _, keys in groups for key, _ in keys)
        column_width = key_width + 2 + max(cells(label) for _, keys in groups for _, label in keys)
        columns = max(1, min(3, (width - 6) // (column_width + 3)))
        # Fill columns top to bottom with whole groups, balancing their heights.
        stacks, lengths = [[] for _ in range(columns)], [0] * columns
        for group in groups:
            shortest = lengths.index(min(lengths))
            stacks[shortest].append(group)
            lengths[shortest] += len(group[1]) + 2
        box_width = min(width - 2, columns * (column_width + 3) + 3)
        box_height = min(height, max(lengths) + 3)
        x, top = (width - box_width) // 2, max(0, (height - box_height) // 2)
        for row in range(top, top + box_height):
            band(screen, row, x, "", box_width, self.style("surface"))
        band(screen, top, x, "  GIT · g" if self.key_group else "  KEYS", box_width,
             self.style("header") | curses.A_BOLD)
        put(screen, top, x + box_width - 16, "Esc cancels" if self.key_group else "any key closes",
            14, self.style("header"))
        for number, stack in enumerate(stacks):
            left, row = x + 3 + number * (column_width + 3), top + 2
            for title, keys in stack:
                put(screen, row, left, title.upper(), column_width, self.style("inactive") | curses.A_BOLD)
                row += 1
                for key, label in keys:
                    put(screen, row, left, key, key_width, self.style("surface") | curses.A_BOLD)
                    put(screen, row, left + key_width + 2, label, column_width - key_width - 2, self.style("inactive"))
                    row += 1
                row += 1

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
        self.find_before, self.find_query, self.find_cursor = self.find_query, "", 0
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
        if isinstance(key, terminal_input.Mouse):
            if key.action in ("up", "down"):
                self.handle_mouse(key, screen)
            return True
        edited = command_line.edit(self.find_query, self.find_cursor, key, self.command_killed)
        if edited is None or edited[0] == self.find_query:
            if edited:
                self.find_cursor = edited[1]  # Only the point moved.
            return True
        self.find_query, self.find_cursor, self.command_killed = edited
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
                            else "Press s to search the diagram source")
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
        self.preview_cursor = line
        if self.rendered is None:
            # Code and plain text do not wrap: bring the match into the visible columns.
            text = clean(self.content[line])
            if self.syntax is not None:
                first, last = cells(text[:start]), cells(text[:end])
            else:
                first, last = start, end  # Plain text scrolls by characters.
            if first < self.horizontal or last > self.horizontal + self.text_width:
                self.horizontal = max(0, first - self.text_width // 3)

    def draw_char_selection(self, screen, y, x, width, number):
        """Shade the selected characters of one line, and show the cursor as a block on its column."""
        (first, start), (last, end) = self.char_range()
        if not first <= number <= last:
            return
        line = self.source_line(number)
        start = start if number == first else 0
        end = end + 1 if number == last else len(line)
        self.draw_segment(screen, y, x, width, number, start, max(start + 1, end), self.style("selected"))
        if number == self.preview_cursor:
            self.draw_cursor_cell(screen, y, x, width, number)

    def column_at(self, number, cell):
        """The character of a source line drawn at a screen cell of the text, counting from its left edge."""
        line = self.source_line(number)
        text = clean(line)
        if self.syntax is not None:
            target, index = cell + self.horizontal, 0
            while index < len(text) and cells(text[:index + 1]) <= target:
                index += 1
        else:
            shown, index = text[self.horizontal:], 0  # Plain text scrolls by characters.
            while index < len(shown) and cells(shown[:index + 1]) <= cell:
                index += 1
            index += self.horizontal
        # Back from the tab-expanded text to the line's own characters.
        column = next((i for i in range(len(line)) if len(clean(line[:i + 1])) > index), len(line))
        return self.clamped_column(number, column)

    def draw_cursor_cell(self, screen, y, x, width, number):
        column = self.clamped_column(number, self.preview_column)
        self.draw_segment(screen, y, x, width, number, column, column + 1, self.style("selected") | curses.A_REVERSE)

    def draw_segment(self, screen, y, x, width, number, start, end, style):
        """Draw characters start to end of a source line over the preview, where the line shows them.
        Past the end of the line, a space stands in so an empty line or the end still shows."""
        line = self.source_line(number)
        text = clean(line)
        first, last = len(clean(line[:start])), len(clean(line[:end]))
        shown = text[first:last] + " " * max(0, end - max(start, len(line)))
        if self.syntax is not None:
            column = cells(text[:first]) - self.horizontal
        else:
            column = cells(text[self.horizontal:first]) if first >= self.horizontal else -1
        if column < 0 or column >= width or not shown:
            return
        put(screen, y, x + column, shown, width - column, style | curses.A_BOLD)

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
        if self.preview_focus and self.cursor_view():
            # A line moves the cursor; a page scrolls and carries the cursor along, as in Vim.
            self.clamp_cursor()
            if abs(amount) > 1:
                cursor = self.preview_cursor
                self.scroll_preview(amount)
                self.preview_cursor = cursor  # Keep its row on screen; the scroll clamped it.
            self.move_cursor(amount, clamp=False)
            if self.source_view():
                self.preview_column = self.clamped_column(self.preview_cursor, self.want_column)
        elif self.preview_focus:
            self.scroll_preview(amount)
        else:
            self.selected = max(0, min(len(self.items) - 1, self.selected + amount))

    def scroll_preview(self, amount: int):
        self.preview_scroll = max(0, min(max(0, self.preview_length() - self.body), self.preview_scroll + amount))
        if self.cursor_view():
            self.clamp_cursor()

    def cursor_view(self):
        """Whether the preview shows lines the cursor can sit on, rather than one image."""
        return self.previewable and bool(self.active) and not self.diagram_view()

    def source_view(self):
        """Whether preview lines are the file's own lines, the only ones a comment can name."""
        return self.cursor_view() and not (self.markdown and not self.diagram_source)

    def clamp_cursor(self):
        """Keep the cursor on a line inside the visible rows, after a scroll moved them."""
        last = max(0, len(self.content) - 1)
        bottom = self.preview_scroll + max(1, self.body) - 1
        self.preview_cursor = max(0, min(max(self.preview_scroll, min(self.preview_cursor, bottom)), last))

    def move_cursor(self, amount: int, clamp=True):
        if clamp:
            self.clamp_cursor()
        self.preview_cursor = max(0, min(len(self.content) - 1, self.preview_cursor + amount))
        self.show_cursor()

    def show_cursor(self):
        """Scroll just enough that the cursor line is visible."""
        if self.preview_cursor < self.preview_scroll:
            self.preview_scroll = self.preview_cursor
        elif self.preview_cursor >= self.preview_scroll + max(1, self.body):
            self.preview_scroll = self.preview_cursor - max(1, self.body) + 1
        self.preview_scroll = max(0, min(self.preview_scroll, max(0, self.preview_length() - self.body)))

    def selected_lines(self):
        """The (first, last) shown lines of the V selection, or None."""
        if self.selection_anchor is None or self.selection_kind != "line" or not self.source_view():
            return None
        return tuple(sorted((self.selection_anchor, self.preview_cursor)))

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
        if key == "s" and (self.diagram_list or (self.markdown and self.previewable)):
            # In Markdown, v switches the whole file between rendered and source.
            self.diagram_source = not self.diagram_source
            self.preview_scroll = self.horizontal = self.preview_cursor = self.preview_column = self.want_column = 0
            self.selection_anchor = None
            self.render_width = None
            return True
        if not self.preview_focus:
            return False
        if key in ("n", "N") and self.find_query:
            self.find_next(1 if key == "n" else -1)
            return True
        half = max(1, page // 2)
        movements = {
            "j": 1, "\n": 1, "\r": 1, curses.KEY_ENTER: 1,
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
            ctrl = bool(state & getattr(curses, "BUTTON_CTRL", 0))
            self.handle_mouse(terminal_input.Mouse(x, y, "click", ctrl), screen)

    def divider_for(self, width):
        # The preview keeps at least 40 columns however far the divider is dragged.
        if self.tree_width is None:
            return max(26, min(width // 4, 38))
        return max(16, min(self.tree_width, width - 40))

    def drag_divider(self, event):
        """Mouse drags on the border between the boxes resize the tree. Returns True if handled."""
        if event.action == "click" and not self.narrow and abs(event.x - self.divider) <= 1 \
                and BOX_TOP <= event.y <= self.content_top + self.body:
            self.dragging = True
        elif event.action == "drag" and self.dragging:
            self.tree_width = self.divider = self.divider_for_pointer(event.x)
        elif event.action == "release" and self.dragging:
            self.dragging = False
            if self.on_tree_width is not None:
                try:
                    self.on_tree_width(self.tree_width)
                except OSError as error:
                    self.message = f"Could not save the tree width: {error}"
        else:
            return event.action in ("drag", "release")  # Stray motion does nothing else.
        return True

    def divider_for_pointer(self, x):
        self.tree_width = x + 1  # The tree's right border follows the pointer.
        return self.divider_for(self.screen_width)

    def handle_mouse(self, event, screen=None):
        if (self.root_draft is not None or self.size_draft or self.layout_dialog or self.app_picker is not None
                or self.comment_dialog()):
            return
        if self.drag_divider(event):
            return
        x, y = event.x, event.y
        if y == ROOT_ROW and event.action == "click" and not self.searching:
            if 2 <= x < 6:
                self.parent_root()
            elif x >= 8:
                self.begin_root()
            return
        if BOX_TOP <= y <= self.content_top + self.body and self.sidebar_mouse(event):
            return  # The comment list, its title row included.
        if y <= BOX_TOP or y > self.content_top + self.body or x < 0:
            return
        over_preview = self.preview_focus if self.narrow else x > self.divider
        if event.action in ("up", "down"):
            amount = -3 if event.action == "up" else 3
            if over_preview:
                self.scroll_preview(amount)
            else:
                self.selected = max(0, min(len(self.items) - 1, self.selected + amount))
            return
        if event.action == "click" and event.ctrl and over_preview:
            self.open_link(x, y)
            return
        self.searching = False
        if not self.narrow:
            self.preview_focus = over_preview
        if event.action == "click":
            if self.preview_focus and self.cursor_view() and self.content_top <= y < self.content_top + self.body:
                number = self.preview_scroll + y - self.content_top
                if number < len(self.content) and 0 <= x - (self.text_left - 7) < 2 and self.source_view():
                    found = self.comment_starts().get(number)
                    if found:
                        self.open_comment_view(found)
                        return
                if number < len(self.content):
                    self.preview_cursor = number
                    if self.source_view():
                        self.preview_column = self.want_column = self.column_at(number, x - self.text_left)
            if not self.preview_focus and self.content_top <= y < self.content_top + self.tree_body:
                index = self.scroll + y - self.content_top
                if index < len(self.items):
                    self.selected = index
                    self.activate(screen, fold=True)

    def key(self, key, screen) -> bool:
        if isinstance(key, terminal_input.Appearance):
            self.appearance = key.mode
            self.update_theme()
            return True
        if isinstance(key, terminal_input.Mouse) and key.action in ("drag", "release"):
            self.drag_divider(key)  # Motion never cancels a search or a dialog.
            return True
        if self.key_group:
            self.key_group = ""
            if key == "\x11":
                return False
            if key in ("\x1b", "\x07"):
                return True
            for suffix, _, command in self.git_group_keys():
                if key == suffix:
                    return self.run_command(command, screen)
            self.message = "Unknown Git key · press g to see commands"
            return True
        typing = (self.layout_dialog or self.size_draft or self.root_draft is not None
                  or self.app_picker is not None or self.key_help
                  or self.finding or self.searching or self.command is not None
                  or self.composer is not None or self.comment_view is not None
                  or self.agent_picker is not None or self.confirm_clear)
        target = None
        if not typing:
            active = self.key_context()
            target = next((rule.target for rule in reversed(self.binding_rules)
                           if rule.key == key and settings.when_matches(rule.when, active)), None)
            if target is None:
                target = self.bindings.get(key)
        if target is not None:
            if target == "none":
                return True
            if target.startswith(":"):
                return self.run_command(target[1:].strip(), screen)
            key = settings.ACTIONS[target]
        if key == "\x11":
            return False
        if key == "\x03":
            return True
        if self.close_keys:
            typed = self.close_typed + (key,)
            if typed in self.close_keys:
                return False
            if any(keys[:len(typed)] == typed for keys in self.close_keys):
                self.close_typed = typed  # Wait for the rest of the binding.
                return True
            self.close_typed = ()
        # C-g cancels like Escape everywhere, except that it never closes Lens.
        cancel = key == "\x07"
        if cancel and self.history_mode and not self.comment_dialog():
            return self.history_key(key, screen)
        if cancel:
            key = "\x1b"
        if self.key_help:
            self.key_help = False  # Any key closes the list; it does nothing else.
            return True
        if self.layout_dialog:
            return self.layout_key(key)
        if self.app_picker is not None:
            return self.app_picker_key(key)
        if self.confirm_clear:
            return self.clear_key(key)
        if self.comment_view is not None:
            return self.comment_view_key(key)
        if self.agent_picker is not None:
            return self.agent_picker_key(key)
        if self.composer is not None:
            return self.composer_key(key)
        if self.size_draft:
            return self.size_key(key)
        if self.root_draft is not None:
            return self.root_key(key)
        if self.finding:
            return self.find_key(key, screen)
        if self.command is not None:
            return self.command_key(key, screen)
        if key == "g" and not self.searching and self.git_group_keys():
            self.key_group = "git"
            return True
        if key == "?" and not self.searching:
            self.key_help = True
            return True
        if (key == ":" or key == "\x1bx") and not self.searching:
            self.command, self.command_recall, self.command_menu = "", len(self.command_history), None
            self.command_cursor = 0
            return True
        if self.history_mode:
            if key == curses.KEY_MOUSE:
                self.mouse_history(screen)
                return True
            return self.history_key(key, screen)
        if key == "/" and self.preview_focus and not self.searching and self.active:
            self.begin_find()
            return True
        # The cursor moves along a source line; b stays page up outside a text selection.
        if self.preview_focus and self.source_view() and (
                key in ("h", "l", "w", "0", "^", "$") or (key == "b" and self.char_selecting())):
            self.move_column(key)
            return True
        if not self.preview_focus and not self.searching:
            key = {"h": curses.KEY_LEFT, "j": curses.KEY_DOWN,
                   "k": curses.KEY_UP, "l": curses.KEY_RIGHT}.get(key, key)
        navigation = (curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT,
                      curses.KEY_PPAGE, curses.KEY_NPAGE, curses.KEY_HOME, curses.KEY_END)
        if (self.searching or key in ("/", "c") or isinstance(key, terminal_input.Mouse)
                or (not self.preview_focus and key in navigation)):
            self.pending_selection = ""
        if key == "/" and not self.searching:
            if not self.searching:
                self.search_before = self.query
            self.searching = True
            self.query_cursor = len(self.query)
            self.preview_focus = False
        elif self.searching:
            steps = {curses.KEY_UP: -1, curses.KEY_DOWN: 1, "\x10": -1, "\x0e": 1,
                     curses.KEY_PPAGE: -self.tree_body, curses.KEY_NPAGE: self.tree_body}
            if key in steps:
                # Pick among the matches without leaving the filter.
                self.selected = max(0, min(len(self.items) - 1, self.selected + steps[key]))
                return True
            if key == "\x1b":
                self.query = self.search_before
                self.searching = False
            elif key in ("\n", "\r", curses.KEY_ENTER):
                self.searching = False
                return True  # Keep the match picked with the arrows.
            elif isinstance(key, terminal_input.Mouse):
                self.handle_mouse(key, screen)
                return True
            else:
                edited = command_line.edit(self.query, self.query_cursor, key, self.command_killed)
                if edited is None:
                    return True
                changed = edited[0] != self.query
                self.query, self.query_cursor, self.command_killed = edited
                if not changed:
                    return True  # Only the point moved.
            self.selected = self.scroll = 0
            self.rebuild()
        elif isinstance(key, terminal_input.Mouse):
            self.handle_mouse(key, screen)
        elif key == "\x0f":
            self.begin_root()
        elif key == "t":
            self.repository_root()
        elif key == "parent":
            self.parent_root()
        elif key == "H" and not self.preview_focus:
            self.open_history(file=True)
        elif key == "V" and self.preview_focus:
            self.toggle_selection("line")
        elif key == "v" and self.preview_focus:
            self.toggle_selection("char")
        elif key == "A":
            self.begin_comment()
        elif key == "S":
            self.begin_send()
        elif key == "X":
            self.begin_clear()
        elif key == "C":
            self.toggle_sidebar()
        elif key == "m" and self.preview_focus:
            self.view_line_comments()
        elif key in ("{", "}") and self.preview_focus:
            self.jump_comment(1 if key == "}" else -1)
        elif key == "\x08":
            self.toggle_ignored()
        elif key == "link-back" or (key in ("\x7f", curses.KEY_BACKSPACE, "H") and self.preview_focus):
            self.link_step()
        elif key == "link-forward" or (key == "L" and self.preview_focus):
            self.link_step(forward=True)
        elif (key == "=" and not self.preview_focus and not self.query and self.items
              and self.items[self.selected].directory):
            self.fold_tree()  # Elsewhere "=" zooms a diagram, as "+" does.
        elif self.preview_key(key):
            pass
        elif key == " " and not self.preview_focus:
            row = self.items[self.selected] if self.items else None
            if row and row.directory:
                if row.path not in (".", ".."):  # These two never fold.
                    self.toggle_fold(row)
            else:
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
            if self.selection_anchor is not None:
                self.selection_anchor = None  # Escape drops the selection before leaving the preview.
            elif self.preview_focus:
                self.preview_focus = False
            elif self.query:
                self.query = ""
                self.selected = self.scroll = 0
                self.rebuild()
            elif not cancel:
                return False
        elif key in ("\n", "\r", curses.KEY_ENTER):
            if not self.preview_focus:
                self.activate(screen)
        elif key in ("\t", curses.KEY_BTAB):
            self.preview_focus = not self.preview_focus
        elif key == "\x04":
            self.show_diff(screen)
        elif key in ("\x05", "e"):
            self.edit(screen)
        elif key == "o":
            self.launch()
        elif key == "O":
            self.begin_app_picker()
        elif key == "c":
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
                elif row.path == ".":
                    pass
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
                self.persist_draft()
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
            self.persist_draft()
            terminal_input.disable()
