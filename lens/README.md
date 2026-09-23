# Lens

Browse the focused Herdr pane's working directory in a popup or overlay with a project tree,
filename search, file previews, and side-by-side Git comparisons in vimdiff. Works alongside any shell or agent,
including Claude Code and Codex, on macOS and Linux.

Requires Herdr 0.9.0 or later, `uv` on Herdr's `PATH`, and Python 3.11 or later
with curses. `uv` manages the Python dependencies automatically; the first launch
requires network access to download any missing dependencies. Git is optional
for browsing and required for change indicators and diffs. Comparing files also
requires `vimdiff` or Vim compiled with diff support.
Markdown rendering uses the Python `Rich` library and source highlighting uses
`Pygments`; both dependencies are managed automatically. Glow is not required.

## Install

```sh
herdr plugin install studykit/studykit-plugins/lens
```

Open **Files: browse project** or **Files: browse changes** from Herdr's plugin
actions. You can also invoke either action from the CLI:

```sh
herdr plugin action invoke studykit.lens.browse
herdr plugin action invoke studykit.lens.changes
```

The navigator uses the pane that was focused when you invoked the action. Its root is
that pane's foreground working directory, falling back to the pane's directory.
A new navigator opened from another pane uses that pane's directory. The navigator keeps
its source directory until you explicitly change the navigation root.

## Display modes

The first launch opens in a **Popup**. Later launches use your last selected
layout. Press **Ctrl+W**, then choose a display mode:

| Key | Mode | Behavior |
| --- | --- | --- |
| 1 | Popup | Show a floating window above your work |
| 2 | Overlay | Expand the navigator across the tab's pane area |
| Escape | Cancel | Keep the current display mode |

Switching modes briefly reopens the navigator and restores the navigation root,
filter, selected file, expanded folders, preview, scroll position, and focus.
Scroll positions may adjust to fit the new dimensions. Finish search or a root/size
dialog before opening the layout menu.

**Ctrl+Y** adjusts the popup's size while Popup is active. Layout and popup
dimensions are remembered across launches and shared across roots. Closing an
overlay restores the previous focus and zoom state.

In Overlay mode, invoking either file action again in the same tab focuses the
existing navigator and restores its zoom instead of creating another pane.
Its root, filter, preview, and current mode remain intact; use Ctrl+G to switch
between the project and changed-files views. Each tab can have its own
navigator. Close the overlay before opening a fresh view from another source
pane in that tab.

## Navigation

| Input | Action |
| --- | --- |
| `/` | Enter filename/path search, including inside collapsed folders |
| Ctrl+O | Change the navigation root by entering a directory path |
| Enter / click on the tree's `..` row | Move the navigation root to its parent |
| Backspace (tree focused) / click `[..]` | Move the navigation root to its parent |
| Ctrl+T | Move to the current Git repository root |
| Enter / Escape in search | Apply the filter / cancel and restore the previous filter |
| Click or Enter | Expand a folder or open the file; in changed-files mode, open vimdiff |
| h / j / k / l (tree focused) | Collapse or move to parent / down / up / expand or enter a folder |
| Space (tree focused) | Preview the selected file while keeping tree focus, including in changed-files mode |
| Left / Right | Collapse / expand folders; scroll horizontally in preview |
| Up / Down, Page Up / Down | Move through files or scroll preview |
| Ctrl+N / Ctrl+P | Scroll preview down / up one line without changing focus |
| Ctrl+F / Ctrl+B | Scroll preview down / up one screen without changing focus |
| j / k, Enter (preview focused) | Scroll down / up one line; Enter scrolls down |
| Space / f / b (preview focused) | Scroll down / down / up one screen |
| d / u (preview focused) | Scroll down / up half a screen |
| g / G (preview focused) | Jump to the beginning / end |
| Mouse wheel | Scroll the panel under the pointer without changing keyboard focus |
| Tab / Shift+Tab | Switch focus between files and preview |
| Ctrl+D | Open a side-by-side HEAD / working-tree comparison in vimdiff |
| Ctrl+E | Open the selected file in an editor |
| Ctrl+G | Toggle changed files only |
| Ctrl+H | Show / hide Git-ignored files; enabling switches to the full project view |
| Ctrl+R | Refresh the file list and preview, then reload Git status |
| Ctrl+W, then 1 / 2 | Switch to Popup / Overlay |
| Ctrl+Y (Popup) | Adjust popup size and remember it for future launches |
| Ctrl+U in search | Clear the search text |
| Escape | Return to files from content; clear search when in files; otherwise close |
| Ctrl+C | Close immediately, retaining the current view for the next launch |

Search is case-insensitive, ranks filename matches ahead of path matches, and
accepts fuzzy abbreviations such as `rdm` for `README.md`. Git projects show tracked
files and untracked files that are not ignored. Without Git, common dependency
directories are excluded. Hidden files are included. Git status uses the usual
two-column codes, including `??` for new files and `D` for deleted files.

The file list and saved preview appear before Git status finishes loading.
You can navigate, search, and close the navigator while `Git: loading…` is shown;
change indicators appear when ready. The changes-only view shows its loading
state first, then fills with changed files. If status lookup fails, the file
browser remains usable; press Ctrl+R to retry.

Changes made outside the navigator are not watched automatically. Press Ctrl+R
to discover new files and update modified-file indicators, or close and reopen
the navigator. Returning from its Ctrl+E editor also refreshes the view. Existing
search filters, collapsed folders, and ignored-file visibility still apply;
use Ctrl+H to include files excluded by Git ignore rules.

Git-ignored files are hidden by default. Ctrl+H includes excluded directories,
their files, empty folders, and nested repositories in the tree and file search.
The header shows `Ignored: shown` or `Ignored: hidden`. Git metadata (`.git`,
`.hg`, `.svn`) remains hidden, and directory symlinks are not followed. Outside
Git, this toggle also includes normally skipped dependency/cache directories.
Ignored files are not treated as Git changes; Ctrl+G still shows only changes
reported by the current repository. Switch the root to a nested repository to
use that repository's own Git status and diff base.

The toggle is preserved while changing roots, refreshing, or resizing, and is
restored when reopening the same root. Roots without a saved view start with
excluded files hidden. Hiding an excluded file also clears its
open preview. Extra filesystem traversal is bounded at 50,000 combined entries;
if the limit is reached, change the root to a smaller folder. No ignore rules or
Git tracking settings are modified.

To change projects, press Ctrl+O, clear the prefilled path with Ctrl+U, enter a
directory, and press Enter. Absolute paths, `~`, spaces, and paths relative to
the current navigation root (including `..`) are supported; no shell expansion
or commands are executed. Escape cancels. When a folder is selected in the tree,
Ctrl+O prefills that folder, so Enter makes it the new root. Clicking the displayed
root path also opens this dialog. Ctrl+T jumps to the Git root when available.
The tree always starts with a `..` entry, including empty directories and
changes-only mode. Enter or click it to go up; at the filesystem root it does
nothing. Filename search results omit this entry. Backspace moves up only in
the unfiltered tree, and remains a text-editing key during search.
Closed folders display `▸ `, expanded folders display `▾ `, and the parent
entry displays `↑  ..`. Files have no folder icon. Use a Nerd Font in your
terminal to display these folder glyphs.

Changing roots clears the filename filter, expanded folders, and old preview,
then focuses the new tree. The changes-only mode stays as selected. Invalid or
unreadable destinations leave the previous tree intact. The source pane's working
directory is never changed. Resizing preserves the chosen root; closing and
opening a fresh navigator starts from the invoking pane's directory again.

Reopening the same root automatically restores its last view: expanded folders,
selected file, filename filter, tree position, preview file and scroll offsets,
file/content focus, changed-files mode, and ignored-file visibility. Views are
shared across panes that use the same canonical directory; different roots keep
separate views. A new navigator still starts at the invoking pane's directory, never
at an unrelated previously visited root. Opening a fresh navigator with the
explicit changes action enables changed-files mode, even if that root's saved
view showed all files. Refocusing an existing overlay preserves its current view.

Use Ctrl+C to close immediately without first changing focus or clearing the
filter. Escape retains its existing back/clear/close behavior; those changes are
remembered too. Search-entry mode and unfinished layout/root/size dialogs are not
reopened. When changing roots inside the navigator, the departing root's view is saved
for later launches, while the destination opens with the normal fresh tree.

Saved views contain navigation metadata, not file contents. Files are read again
on reopening; missing previews are cleared, stale expanded folders are discarded,
and scroll positions adjust to the new content and window dimensions. Corrupt or
unavailable saved state does not prevent browsing. Popup dimensions remain a
shared preference rather than a per-root setting.

Typing only changes the filter after `/`. Enter leaves search and focuses the
file list; press Enter again to open the selected result. Ordinary character keys
outside search do not change the filter. Within search, `/` is an ordinary path
separator.
In the tree, `l` expands a collapsed folder; press it again to select its first
child. `h` collapses an expanded folder or selects the parent. Space does nothing
on a folder or an empty list. Space updates the preview without moving focus,
so `j` / `k` continue moving through files. Press Tab to focus and scroll the
preview, or use Ctrl+N/P and Ctrl+F/B to scroll while staying in the tree.
Enter and clicking a file still transfer focus to content. In filename
search, `h`, `j`, `k`, `l`, and Space remain text.

Vimdiff compares HEAD on the left with the working tree on the right, including
staged and unstaged changes together. New files have an empty left side; deleted
files have an empty right side. Staged renames use the original file as the base.
Within vimdiff, `Tab` switches sides, `]c` / `[c` jump between changes, and `q` or
`:qa!` returns to the navigator. Both sides are read-only temporary snapshots.
The comparison uses a bundled Vim theme and key mappings, independent of your vimrc.

The active panel has a bright header, a double border, and an explicit
`FOCUS: FILES`, `FOCUS: CONTENT`, or `FOCUS: SEARCH` badge. Opening a file moves focus
to content; Tab, Escape, or clicking the file panel brings it back. `/` activates
the highlighted search field. Narrow terminals show one panel at a time.

The navigator follows your Herdr theme: background, text, selection, borders, and
Markdown/code colors come from the selected built-in palette and `[theme.custom]`
overrides. Reopen the navigator or press Ctrl+R to reread theme settings. The `terminal`
theme preserves terminal-default colors. RGB values are approximated using the
terminal's 256-color palette (or available basic colors). With `auto_switch`, the
navigator uses the host appearance reported when it opens; without a report it uses
Herdr's dark fallback. Vimdiff keeps its separate comparison theme.

Folder names and icons use the ordinary directory color from `ls`: an exported
`LS_COLORS` `di` entry takes priority, followed by the first pair in `LSCOLORS`.
Without either setting, the default is blue on macOS/BSD and bold blue on Linux.
Invalid settings fall back to the Herdr text color. Selection highlights and the
panel background remain themed, except for an explicitly configured directory
background. Restart the navigator after changing the inherited environment. Shell
aliases, extension rules, and special directory-permission colors are not read.

With the tree focused, use Ctrl+N / Ctrl+P to scroll the current preview down / up
one line, or Ctrl+F / Ctrl+B to scroll one screen. These keys preserve tree
selection and focus; they do not load the selected file. Press Space first to
preview a file. On narrow layouts, use Tab to reveal the content panel.
Mouse-wheel scrolling also preserves keyboard focus and search mode: the panel
under the pointer scrolls, while clicks still change focus. On narrow layouts,
the wheel scrolls the currently visible panel.

Other familiar `man`/`less` scrolling keys work only while content is focused.
Additional aliases are `e` / `y` for down / up one line, Ctrl+U for up half a screen, and
`<` / `>` for the beginning / end. Ctrl+D and Ctrl+E retain their navigator
actions (vimdiff and editor); use plain `d` and `j` for scrolling. Search input
and the layout/root/popup-size dialogs take priority, so these letters remain ordinary text
in search. Markdown scrolling follows rendered lines, not source lines.

Markdown files (`.md` and `.markdown`) are rendered with Rich inside the navigator.
The preview styles headings, emphasis, lists, tables, and code blocks and wraps to the
panel width. Rendered Markdown omits source line numbers; the position indicator
counts rendered lines. Footnote definitions (`[^label]: ...`) remain visible in
their original location, with each reference starting on a separate line.

Obsidian-style previews also support:

- Wiki links (`[[Note]]`, `[[Note#Heading]]`, `[[Note#^block]]`) and display aliases
  (`[[Note|Label]]`), styled with the theme's link color. Links are display-only.
- Callouts (`> [!note]`, `> [!warning]`, and other standard types) with colored
  borders and titles, Markdown bodies, and nesting. Unknown types use the note
  color. Fold markers (`+` / `-`) are accepted, but preview always shows the body;
  interactive folding is not supported.
- Highlights (`==text==`) and task-list checkboxes (`- [ ]`, `- [x]`).
- YAML frontmatter in a syntax-highlighted **Properties** panel. Values are
  displayed as source, not evaluated.
- Visible embed placeholders (`![[Note]]`, `![[image.png|300]]`) that retain the
  target name. Linked files are not loaded and images are not decoded.
- `<br>` line breaks, including inside table cells. Escape alias separators in
  tables as `[[Note\|Label]]`, following Obsidian's table syntax.

Code blocks, inline code, and backslash-escaped examples remain literal. This is
a subset of Obsidian rendering: vault link navigation, transclusion, comment
hiding, MathJax, Mermaid diagrams, and Dataview execution are not implemented.
If rendering fails, the preview shows the Markdown source.

Code and configuration files use Pygments syntax highlighting based on their
extension or recognized filename (such as `Dockerfile` and `Makefile`). Supported
formats include Python, JavaScript/TypeScript/TSX, Java, Kotlin, Go, Rust, C,
shell scripts, JSON, YAML, TOML, INI, SQL, HTML, XML, and CSS. The content header
shows the detected language. Colors follow the Herdr theme, including in Markdown
code blocks. Code previews retain source line numbers and do not wrap; Left/Right
scrolls long lines horizontally. Files are displayed, never executed.

Unknown extensions and plain text use the normal numbered preview. Highlighting
errors also fall back to plain text. Binary files remain excluded.

In Popup mode, press **Ctrl+Y** to adjust the popup size. Left/Right changes
width, Down/Up changes height, in five-percentage-point steps. Keys `1` through
`4` select Small, Medium, Large, or Maximum. Enter applies and remembers the size;
Escape cancels. Width and height can each range from 40% to 100% of Herdr's
available area; Herdr clamps small dimensions to its minimum popup size.

Herdr 0.9 does not expose an API to resize an existing popup. Applying a size
briefly closes and reopens it, preserving the source folder, search, expanded
folders, selected file, preview position, and focus. Adjust the size before
opening an editor or vimdiff. The preference is shared across Herdr sessions.

File previews are limited to 256 KiB, comparisons to 8 MiB per side, and file lists
to 50,000 entries. Binary content and symlinks outside the selected directory are
not previewed or compared.

The editor comes from `VISUAL`, then `EDITOR`, then an installed `nvim`, `vim`, or
`vi`. Configure these in the environment used to launch Herdr. Editor arguments
are supported, for example `EDITOR='code --wait'`. Closing the editor returns to
the navigator. Browsing and diff previews do not modify project files.

## Optional keyboard shortcuts

Add bindings to your Herdr configuration, choosing unused keys:

```toml
[[keys.command]]
key = "prefix+t"
type = "plugin_action"
command = "studykit.lens.browse"
description = "browse project files"

[[keys.command]]
key = "prefix+d"
type = "plugin_action"
command = "studykit.lens.changes"
description = "browse changed files"
```

This is a Herdr UI plugin, installed through Herdr. It does not require a separate
Claude Code or Codex marketplace installation.
