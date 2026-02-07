# Environment (Quick Reference)

This is a quick reference for your current terminal + workflow setup on macOS.

## Core stack

- Shell: `zsh` + Oh My Zsh (`~/.zshrc`)
- Prompt: Starship (`~/.config/starship.toml`)
- Jumping: zoxide (`cd` → `z`)
- Fuzzy finder: fzf (Ctrl+R, Alt+C)
- Terminals: Kitty + Ghostty
- Multiplexer: tmux (`~/.tmux.conf`)
- System info: `fetch` / `nf` (Fastfetch)

## PARA folders

- `~/Inbox` (processing)
- `~/Projects` (active work)
- `~/Areas` (ongoing responsibilities)
- `~/Resources` (reference)
- `~/Archive/YYYY` (done/old)

Downloads rule: keep `~/Downloads` empty; move items into `~/Inbox/Downloads`.

## Kitty

- Config: `~/.config/kitty/kitty.conf`
- Active theme: `~/.config/kitty/theme.conf`
- Theme picker: `kitty-theme` (script: `~/.config/kitty/kitty-theme`)

Theme sync: applying a Kitty theme updates Starship palette via `~/.config/starship/update-palette`.

## Ghostty

- Config: `~/.config/ghostty/config`
- Theme picker: `ghostty-theme` (script: `~/.config/ghostty/ghostty-theme`)
- Themes: `~/.config/ghostty/themes/*`

Theme sync: applying a Ghostty theme updates Starship palette from the selected Ghostty theme file.

## Starship

- Config: `~/.config/starship.toml`
- Palette updater: `~/.config/starship/update-palette`

Manual refresh: `~/.config/starship/update-palette`

## tmux

- Prefix: `Ctrl+A`
- New window: `prefix` then `c`
- Split vertical: `prefix` then `-`
- Split horizontal: `prefix` then `|`
- Reload config: `prefix` then `r`

## Helpful commands / aliases

From `~/.zshrc`:

- `fetch` / `nf`: Fastfetch info
- `mvdl`: move everything from `~/Downloads` → `~/Inbox/Downloads`
- `inboxmv`: pick files in `~/Inbox/Downloads` and move them into PARA folders
- `inbox`, `dlinbox`, `sortbox`: jump to Inbox folders
- `kp`: pick a project directory and open in Kitty
- `ks`: pick an SSH host and open in Kitty
- `kl`: pick a file and tail it in Kitty
- `dots`: update `~/terminal-dotfiles` snapshot

## Homebrew (important)

Your `brew doctor` reports `/opt/homebrew` permissions are broken right now, so installs will fail until fixed.

- Helper: `~/.local/bin/homebrew-fix` prints the exact commands to run in your normal terminal.

## Finder + keyboard QoL

Applied defaults:

- Finder: shows path bar + status bar + hidden files
- Finder: new window opens in `~/Projects`
- Keyboard: fast key repeat + press-and-hold disabled

## Raycast Script Commands

Installed in:

- `~/Library/Application Support/com.raycast.macos/script-commands`

Includes:

- Open Kitty terminal
- Kitty/Ghostty theme pickers
- Open `~/Inbox/Downloads`
- Inbox move helper

## Touch ID for sudo (optional)

Helpers (run in a normal terminal, will prompt for your macOS password):

- `~/.local/bin/enable-touchid-sudo`
- `~/.local/bin/disable-touchid-sudo`

## Inbox reminder (LaunchAgent)

Files:

- Script: `~/.local/bin/inbox-reminder`
- Agent: `~/Library/LaunchAgents/com.rehan.inbox-reminder.plist`

Enable (run in a normal terminal):

```bash
uid=$(id -u)
launchctl bootout "gui/$uid" "$HOME/Library/LaunchAgents/com.rehan.inbox-reminder.plist" 2>/dev/null || true
launchctl bootstrap "gui/$uid" "$HOME/Library/LaunchAgents/com.rehan.inbox-reminder.plist"
launchctl enable "gui/$uid/com.rehan.inbox-reminder"
launchctl kickstart -k "gui/$uid/com.rehan.inbox-reminder"
```

