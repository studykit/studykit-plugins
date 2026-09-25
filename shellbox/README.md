# shellbox

A [Herdr](https://herdr.dev) plugin that opens an interactive shell in a popup
for the focused pane. It works without Lens or any other plugin.

## Requirements

- Herdr 0.9.0 or later on macOS or Linux
- Python 3.11 or later and `tmux` on Herdr's `PATH`

## Install

```sh
herdr plugin install studykit/studykit-plugins/shellbox
```

Focus the source pane, then choose **Shell: toggle popup** from Herdr's
plugin actions. You can also run:

```sh
herdr plugin action invoke studykit.shellbox.open
```

The first invocation starts your interactive `$SHELL` in the focused pane's
current working directory. Each pane has its own shell. Bind the action to a
Herdr key; that same key hides the popup while it is visible and shows it again
from the source pane. The shell keeps its directory, variables, and running
commands. Type `exit` or press Ctrl+D at the shell prompt to end that shell.
The tmux status line shows the Herdr pane ID and title of the source pane.

If you close a pane while its shell is still running, a popup asks whether to
end it. Press `y` to end the shell; any other key keeps it running, and the
popup shows the `tmux` command that attaches to it later.

While a pane's shell is running, Herdr shows a tmux logo to the left of that
pane's agent name, in the sidebar and in split pane borders. A pane without an
agent shows the logo alone as its border title. The logo is the Nerd Font
`nf-dev-tmux` glyph and disappears when the shell exits. To use a
different mark, such as an emoji, set it in the plugin's `config.toml`
(described below); set `indicator = ""` to turn it off:

```toml
indicator = "🐚"
```

The popup loads your `~/.tmux.conf` or XDG tmux configuration, including your
prefix and custom bindings. It also applies the configuration to an existing
popup session when the file changes.

Ctrl+Q also hides the popup by default. To choose a different additional close
key, run `herdr plugin config-dir studykit.shellbox` and put a `config.toml` in the
directory it prints:

```toml
close_key = "prefix+q"
```

This example uses your tmux prefix followed by `q`. Use tmux key names such as
`C-q` or `M-q` for a key that works without the prefix. Set `close_key = "none"`
to manage the detach binding entirely in your tmux configuration. Changes take
effect the next time you open the popup; the running shell is preserved.

To use Ctrl+H as the show/hide key, put this in your Herdr configuration:

```toml
[[keys.command]]
key = "ctrl+h"
type = "plugin_action"
command = "studykit.shellbox.open"
description = "toggle shell popup"
```
