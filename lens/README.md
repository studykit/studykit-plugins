# Lens

A file browser for [Herdr](https://herdr.dev). It opens on the focused pane's working
directory, in a popup, an overlay, or half of the tab. It has a project tree, fuzzy
filename search, previews of code, Markdown and diagrams, and Git diffs. It works
alongside any shell or agent, including Claude Code and Codex, on macOS and Linux.

## Requirements

- Herdr 0.9.0 or later
- `uv` on Herdr's `PATH`, and Python 3.11 or later with curses. `uv` installs the
  Python dependencies itself, so the first launch needs network access.
- Git, for change indicators and diffs. Without Git you can still browse.
- `vimdiff` (or Vim built with diff support) to compare files, unless you set another
  diff tool in the [settings](#settings).
- For diagram images: a terminal that supports the Kitty graphics protocol, such as
  Ghostty, kitty or WezTerm, and the renderers listed under [Diagrams](#diagrams).
- A [Nerd Font](https://www.nerdfonts.com) for the folder glyphs and the optional
  file-tree icons.

## Install

```sh
herdr plugin install studykit/studykit-plugins/lens
```

Lens adds three Herdr plugin actions:

| Action | What it does |
| --- | --- |
| **Files: browse project** (`studykit.lens.browse`) | Open Lens, or focus the one already open in this tab |
| **Files: browse changes** (`studykit.lens.changes`) | Open Lens showing only changed files |
| **Files: toggle Lens** (`studykit.lens.toggle`) | Open Lens, or close it when it is open |

Run them from Herdr's plugin actions, or from the CLI:

```sh
herdr plugin action invoke studykit.lens.browse
```

To bind them to keys, add something like this to your Herdr configuration:

```toml
[[keys.command]]
key = "prefix+t"
type = "plugin_action"
command = "studykit.lens.toggle"
description = "open or close Lens"

[[keys.command]]
key = "prefix+d"
type = "plugin_action"
command = "studykit.lens.changes"
description = "browse changed files"
```

Lens is a Herdr plugin only. It needs no separate Claude Code or Codex install.

## Getting around

Lens starts in the working directory of the pane that was focused when you opened it.
That directory is the **root** of the tree. The root stays put until you change it,
and Lens never changes the pane's own directory.

The screen has two panels: the file tree on the left and the preview on the right.
Tab switches between them. The active panel has a double border. The bar under the
panels shows which part has the keys: `FILES`, `CONTENT`, `SEARCH`, `FIND`, `ROOT` or
`COMMAND`. It also shows the file name and your position. The bottom line shows
messages and a few useful keys. Press `?` for the full key list. On a narrow
terminal, only one panel shows at a time.

### Keys

These keys work outside text fields. Letters in a text field are just text.

**Everywhere**

| Key | Action |
| --- | --- |
| Tab / Shift+Tab | Switch between the tree and the preview |
| `?` | List every key |
| `:` or Alt+X | Open the [command line](#command-line) |
| `/` | Filter filenames (tree), or find text (preview) |
| Escape | Go back one step: leave the preview, clear the filter, then close Lens |
| Ctrl+G | Cancel like Escape, but never close Lens |
| Ctrl+C | Close Lens right away |
| Ctrl+E | Open the selected file or folder in your editor |
| Ctrl+D | Compare the file with Git HEAD |
| `o` | Open the file or folder in the application your OS assigns to it, such as Finder for a folder |
| `O` | Pick an application to open it with. Type to filter; recent choices come first. |
| `c` | Show only changed files, or every file |
| Ctrl+H | Show or hide Git-ignored files |
| Ctrl+R | Reload the files, the preview, Git status and the theme |
| Ctrl+O | Change the root by typing a path |
| `t` | Change the root to the Git repository root |
| Ctrl+W, then 1–4 | Switch to Popup, Overlay, Left half or Right half |
| Ctrl+Y | Resize the popup |

**File tree**

| Key | Action |
| --- | --- |
| Up / Down, `j` / `k` | Move |
| Page Up / Page Down, Home / End | Move a page, or to the start / end |
| Enter, or click | Open a file in the preview. On a folder, make it the root. In changed-files mode, open the diff. |
| Space | Preview the file and stay in the tree; on a folder, fold or unfold it |
| `l` / Right | Unfold a folder; press again to go to its first entry |
| `h` / Left | Fold a folder, or go to the parent |
| `e` | Edit the selected file or folder |
| Backspace, or Enter on `..` | Move the root up one folder |
| Ctrl+N / Ctrl+P | Scroll the preview one line without leaving the tree |
| Ctrl+F / Ctrl+B | Scroll the preview one screen without leaving the tree |

The tree always starts with `..` (the parent folder) and `.` (the root itself). On
`.`, `o` and `O` open the root. Clicking a folder folds or unfolds it.

**Preview**

| Key | Action |
| --- | --- |
| `j` / `k`, Enter, `e` / `y` | Scroll one line |
| Space / `f`, `b` | Scroll one screen down / up |
| `d` / `u`, Ctrl+U | Scroll half a screen down / up |
| `g` / `G`, `<` / `>` | Go to the start / end |
| Left / Right | Scroll sideways |
| `n` / `N` | Next / previous find match |
| `v` | Switch diagrams between image and source |
| `+` (or `=`) / `-` / `0` | Zoom the diagram in / out / back to fit |
| `[` / `]` | Select the previous / next diagram in Markdown |
| `a` | Align diagrams left, center or right |

**Mouse**: click to select or focus, scroll the wheel over either panel, and drag the
border between the panels to resize the tree. Lens remembers the width.

### Filtering filenames

Press `/` in the tree and type. The filter searches the whole project, including
folded folders. It ignores case and matches loosely, so `rdm` finds `README.md`.
Filename matches come before path matches. Up / Down or Ctrl+P / Ctrl+N pick a match.
Enter applies the filter and returns to the tree, so press Enter again to open the
file. Escape restores the previous filter.

### Finding text in the preview

Press `/` in the preview. Matches are highlighted, and the current one more
strongly. The preview jumps to the first match at or after your position as you
type. An all-lowercase query ignores case; a capital letter makes it
case-sensitive. Enter keeps the search and Escape returns to where you started.
`n` / `N` go to the next / previous match and wrap at the ends. Enter on an empty
query repeats the last search. Markdown is searched as it is shown. To search a
diagram, press `v` first to show its source.

### Text fields

Every place you type edits with Emacs keys: the filter, find, the command line, the
Change root prompt, and the application picker. They share one kill ring.

| Key | Action |
| --- | --- |
| Ctrl+A / Ctrl+E, Home / End | Go to the start / end |
| Ctrl+B / Ctrl+F, Left / Right | Move one character |
| Alt+B / Alt+F | Move one word |
| Ctrl+D | Delete forward |
| Ctrl+K / Ctrl+U | Kill to the end / start |
| Alt+D / Alt+Backspace | Kill a word forward / back |
| Ctrl+W | Kill the argument before the cursor |
| Ctrl+Y | Yank the last kill |
| Ctrl+G or Escape | Cancel |

### Changing the root

- **Enter** on a folder makes it the root. **Backspace** or `..` goes up.
- **`t`** goes to the Git repository root.
- **Ctrl+O**, or a click on the root path, asks for a directory. It starts with the
  selected folder filled in. The path can be absolute, start with `~`, or be relative
  to the root, and `..` works too. Nothing is passed to a shell.

A new root clears the filter and the unfolded folders. The preview stays if its file
is still under the new root, for example after `t` or going up. The changed-files
view stays as it was. If the path is invalid, the old tree stays.

## Git

In a Git project the tree shows tracked files and untracked files that are not
ignored. Changed files carry the usual two-letter status codes, such as `M`, `??`
for a new file and `D` for a deleted one. You can browse right away: `Git…` shows in
the tree's title while the status loads, and the codes appear when it is ready. If
the status lookup fails, press Ctrl+R to retry.

`c` (or **Files: browse changes**) lists only changed files. Enter on one opens the
diff.

**Diffs.** Ctrl+D compares HEAD (left) with the working tree (right), including
staged and unstaged changes. A new file has an empty left side, and a deleted file an
empty right side. A staged rename is compared with the original file. Vimdiff opens
with its own theme and keys, and your vimrc does not apply. Tab switches sides,
`]c` / `[c` jump between changes, and `q` returns to Lens. Both sides are read-only
copies. To use another diff tool, see [Settings](#settings).

**Ignored files.** Git-ignored files are hidden. Ctrl+H shows them, together with
excluded folders, empty folders and nested repositories, and the tree title shows
`+ignored`. `.git`, `.hg` and `.svn` stay hidden, and Lens does not follow folder
symlinks. Outside Git, Lens skips common dependency and cache folders, and Ctrl+H
shows them. Ignored files never count as changes. To use a nested repository's own
status, make it the root.

Lens does not watch for changes. Press Ctrl+R to see new files and updated status.
Lens also refreshes when you return from the editor.

## Previews

- **Code and config files** are highlighted by extension or by name, such as
  `Dockerfile` or `Makefile`. They keep line numbers and do not wrap; Left / Right
  scrolls long lines. The header shows the language.
- **Markdown** (`.md`, `.markdown`) is rendered and wraps to the panel. Rendering
  includes headings, lists, tables, code blocks and footnotes. If rendering fails,
  you see the source.
- **Plain text** and unknown file types show with line numbers.
- **Binary files** are not previewed.

Files are only displayed, never run. Colors follow your Herdr theme, including
`[theme.custom]` overrides.

### Obsidian Markdown

Lens also renders these Obsidian features:

- Wiki links (`[[Note]]`, `[[Note#Heading]]`, `[[Note|Label]]`), for display only
- Callouts (`> [!note]`, `> [!warning]` …), with nesting. They always show expanded.
- Highlights (`==text==`) and task checkboxes (`- [ ]`, `- [x]`)
- YAML frontmatter, in a **Properties** panel
- Embeds (`![[Note]]`, `![[image.png]]`), shown as placeholders

Lens does not follow links, transclude notes, hide comments, or run MathJax or
Dataview.

### Diagrams

Lens draws diagram files, and tagged code blocks in Markdown, as images. It uses
local tools only, so nothing is sent to a rendering service. If a language's tools
are not installed, you see the source.

| Language | Fence tags | Files | Tools on `PATH` |
|---|---|---|---|
| PlantUML | `plantuml`, `puml` | `.puml`, `.plantuml`, `.pu`, `.iuml`, `.wsd` | `plantuml` (or `PLANTUML_JAR` with Java) |
| Mermaid | `mermaid`, `mmd` | `.mmd`, `.mermaid` | `mmdc` from `@mermaid-js/mermaid-cli` |
| D2 | `d2` | `.d2` | `d2`, `rsvg-convert` |
| Graphviz | `dot`, `graphviz`, `gv` | `.dot`, `.gv` | `dot` |
| Pikchr | `pikchr` | `.pikchr`, `.pik` | `pikchr`, `rsvg-convert` |
| Svgbob | `bob`, `svgbob` | `.bob` | `svgbob_cli`, `rsvg-convert` |
| WaveDrom | `wavedrom` | — | `wavedrom-cli`, `rsvg-convert` |
| Vega-Lite | `vega-lite`, `vegalite` | `.vl.json` | `vl2svg` from `vega-lite` and `vega-cli`, `rsvg-convert` |
| Structurizr DSL | `structurizr` | `workspace.dsl` | `structurizr-cli`, `plantuml` |

`rsvg-convert` comes from librsvg. Diagrams get a white background so they are easy
to read in dark themes. For Structurizr, Lens shows the workspace's first view.
Mermaid takes a few seconds to render.

- **Diagram files** fit the panel. *Rendering …* shows until the image is ready, or an
  error if the tool fails. Only the first `@startuml` block of a PlantUML file is
  shown. Relative includes resolve from the file's folder.
- **Markdown blocks** are drawn in place of the code. They are as wide as the panel
  and at most one panel tall. Each block shows as code until its image is ready. A
  block that fails stays as code, and the error shows on the bottom line. Inside a
  PlantUML fence you can leave out `@startuml` / `@enduml`.
- **Zoom** goes from 25% to 400% with `+` / `-`, and `0` fits again. A zoomed file
  pans with the scroll keys. In Markdown, zoom applies to the selected diagram: the
  first one on screen, or the one you pick with `[` / `]`.
- **Alignment**: `a` cycles every diagram between left, center and right. Lens
  remembers the choice.
- `v` shows every diagram as source.

If Herdr clears a diagram from the screen, press Ctrl+R. With
`[terminal].kitty_graphics = false` in Herdr's configuration, Lens always shows the
source.

## Command line

Press `:` (as in Vim) or Alt+X (as in Emacs), type a command, and press Enter. You can
shorten a command to any unambiguous prefix. Tab completes command names, paths and
arguments. When more than one fits, Tab opens a list: typing narrows it, Up / Down or
Tab choose, and Enter inserts the choice. Up / Down (or Ctrl+P / Ctrl+N) recall
earlier commands. Escape, Ctrl+G, or Backspace on an empty line cancels.

| Command | Action |
| --- | --- |
| `preview FILE` | Preview a file and show it in the tree |
| `goto LINE` (`goto-line`), or just the number | Go to a line in the preview |
| `top` / `bottom` | Go to the start / end of the preview |
| `find TEXT` | Find text in the preview; `n` / `N` continue |
| `cd DIR` (`root`) | Change the root |
| `git-root` | Change the root to the Git repository root |
| `changes` / `project` | Show only changed files / every file |
| `ignored [on\|off]` | Show or hide Git-ignored files |
| `refresh` | Reload the file list and preview |
| `editor` / `diff` | Open the current file in your editor / the diff tool |
| `launch [FILE]` (`xdg-open`, `start`) | Open a file or folder in its OS application |
| `with [APP]` (`app`) | Open with APP: a macOS application name, or a command elsewhere. Alone, it shows the list. |
| `zoom in\|out\|fit\|PERCENT` | Zoom the current diagram |
| `align left\|center\|right` | Align diagrams |
| `source` / `diagram` | Show diagrams as source / images |
| `layout popup\|overlay\|left\|right` | Switch the display mode |
| `icons nerd\|plain` | Use Nerd Font icons or plain text in the tree |
| `config` (`settings`) | Edit the settings file |
| `help [COMMAND]` | List the commands, or describe one |
| `quit` (`q`, `exit`) | Close Lens |

## Display modes

Lens first opens as a popup. After that it uses the mode you last chose. Press
**Ctrl+W**, then:

| Key | Mode |
| --- | --- |
| 1 | **Popup**: a floating window above your panes |
| 2 | **Overlay**: covers the tab's pane area |
| 3 | **Left half**: the left half of the tab, with your panes in the right half |
| 4 | **Right half**: the right half of the tab, with your panes in the left half |

Your panes keep their splits in the other half, and they return to full size when
Lens closes. Opening a half turns off the tab's zoom. Closing an overlay restores the
previous focus and zoom.

In Overlay and half modes each tab has its own Lens. Opening Lens again in the same
tab focuses the existing one, with its current root and view, and `c` switches
between all files and changed files.

**Popup size.** In Popup mode, press Ctrl+Y. Left / Right change the width and Up /
Down the height, in steps of 5%. `1` to `4` pick Small, Medium, Large or Maximum.
Enter applies and Escape cancels. Width and height each range from 40% to 100%.

Switching modes or resizing the popup briefly reopens Lens. Your root, filter,
folders, preview and focus stay as they were. Lens remembers the mode and popup size
for next time.

## Saved views

When you open Lens on a root you have visited before, it restores that root's last
view: unfolded folders, the selected file, the filter, the preview and its scroll
position, focus, changed-files mode and ignored-file visibility. Each root has its
own view. Lens saves navigation state only, never file contents. Files are read
fresh, and anything that no longer exists is dropped.

Lens always opens at the current pane's directory, never at a root you visited
earlier. **Files: browse changes** always starts in changed-files mode.

## Settings

Lens reads `~/.config/lens/config.toml`, or `$XDG_CONFIG_HOME/lens/config.toml`, or
the path in `LENS_CONFIG`. Run `:config` to edit it. The first time, Lens creates it
with commented examples, and it reloads the settings when your editor exits. Other
edits apply the next time Lens opens. Lens reports mistakes on the bottom line and
applies the rest.

```toml
[editor]
# {file} and {line} are replaced; without {file}, the path is appended.
# {line} is the first line shown in a code or text preview, otherwise 1.
command = "nvim +{line} {file}"

[diff]
# Replaces vimdiff for Ctrl+D and :diff. {before} is the HEAD copy and {after}
# the working copy, both temporary files; {name} is the path.
# Without {before}/{after}, the two paths are appended.
command = "difft {before} {after}"
pause = true       # wait for Enter afterwards, for tools that print and exit

[open]
# Optional. Unset, "o" uses the OS default (open, xdg-open or start).
# command = "xdg-open {file}"

[ui]
icons = "nerd"     # or "plain"
align = "center"   # diagram alignment: left, center, right
tree_padding = 1   # blank columns on each side of the tree's rows (0 - 8)

[keys]
# A key, then an action name or a ":" command line. These add to the
# built-in keys and do not apply while you are typing.
"ctrl+f" = "search"
"alt+z" = ":zoom fit"
"F" = ":find TODO"
```

Without `[editor]`, Lens uses `VISUAL`, then `EDITOR`, then `nvim`, `vim` or `vi`.
Arguments work, for example `EDITOR='code --wait'`. Set these in the environment that
starts Herdr.

To use Emacs ediff as the diff tool, set this `command`. Quitting ediff with `q` also
closes its frame:

```toml
command = '''emacsclient -nw -a '' --eval '(ediff-files "{before}" "{after}" (list (lambda () (let ((frame (selected-frame))) (add-hook (quote ediff-quit-hook) (lambda () (run-at-time 0 nil (function delete-frame) frame)) t t)))))' '''
```

You can write a key in `[keys]` as:

- a single character, such as `"q"`, `"N"` or `"+"`
- `ctrl+`, `alt+` or `shift+` followed by a letter
- one of `space`, `tab`, `enter`, `escape`, `backspace`, `delete`, `up`, `down`,
  `left`, `right`, `home`, `end`, `pageup` or `pagedown`

| Action | Built-in key |
| --- | --- |
| `focus`, `back`, `quit` | Tab, Escape, Ctrl+C |
| `search`, `command`, `next-match`, `prev-match` | `/`, `:`, `n`, `N` |
| `preview`, `edit`, `diff` | Space, Ctrl+E (and `e` in the tree), Ctrl+D |
| `changes`, `ignored`, `refresh` | `c`, Ctrl+H, Ctrl+R |
| `root`, `git-root`, `parent` | Ctrl+O, `t`, Backspace |
| `layout`, `popup-size` | Ctrl+W, Ctrl+Y |
| `top`, `bottom` | `g`, `G` |
| `zoom-in`, `zoom-out`, `zoom-fit`, `align` | `+`, `-`, `0`, `a` |
| `prev-diagram`, `next-diagram`, `source` | `[`, `]`, `v` |
| `launch`, `launch-with` | `o`, `O` |

**Theme and colors.** Lens follows your Herdr theme, and Ctrl+R rereads it. The
`terminal` theme keeps your terminal's default colors. With `auto_switch`, Lens
follows the light or dark appearance the terminal reports when Lens opens. Folder
names use the directory color from `LS_COLORS` (`di`) or `LSCOLORS`. Without either,
they are blue on macOS and bold blue on Linux.

## Limits

- Previews: 256 KiB per file
- Diffs: 8 MiB per side
- File lists: 50,000 entries, including ignored files. If a folder is larger, pick a
  smaller root.

Lens does not preview or compare symlinks that point outside the root.
