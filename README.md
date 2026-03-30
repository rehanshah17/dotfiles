# dotfiles

Kitty + Starship configs. Follow the steps below to set up a new Mac from scratch.

---

## 1. Xcode Command Line Tools

```bash
xcode-select --install
```

---

## 2. Homebrew

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

After install, add to your shell profile:

```bash
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
```

---

## 3. Core terminal tools

```bash
brew install \
  git gh \
  zoxide fzf fd ripgrep bat eza tree \
  starship \
  tmux \
  lazygit git-delta \
  fastfetch \
  carapace direnv \
  wget httpie
```

---

## 4. Kitty

Download from [https://sw.kovidgoyal.net/kitty/](https://sw.kovidgoyal.net/kitty/) or via Homebrew Cask:

```bash
brew install --cask kitty
```

Then copy configs from this repo:

```bash
mkdir -p ~/.config/kitty
cp -r home/.config/kitty/ ~/.config/kitty/
```

---

## 5. Starship

Starship is installed via Homebrew above. Copy the config:

```bash
cp home/.config/starship.toml ~/.config/starship.toml
```

Add to `~/.zshrc`:

```bash
eval "$(starship init zsh)"
```

---

## 6. Oh My Zsh

```bash
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
```

---

## 7. Shell config (`~/.zshrc`)

Suggested additions to `~/.zshrc` after installing the tools above:

```zsh
# Homebrew
export PATH="/opt/homebrew/bin:$PATH"
export PATH="/opt/homebrew/sbin:$PATH"

# Local binaries
export PATH="$HOME/.local/bin:$PATH"

# fzf
if [[ -r /opt/homebrew/opt/fzf/shell/completion.zsh ]]; then
  source /opt/homebrew/opt/fzf/shell/completion.zsh
fi
if [[ -r /opt/homebrew/opt/fzf/shell/key-bindings.zsh ]]; then
  source /opt/homebrew/opt/fzf/shell/key-bindings.zsh
fi
export FZF_DEFAULT_OPTS="--height=60% --layout=reverse --border --prompt='❯ '"

# Carapace
export CARAPACE_BRIDGES='zsh,fish,bash,inshellisense'
source <(carapace _carapace)

# direnv
eval "$(direnv hook zsh)"

# Zoxide (replaces cd)
eval "$(zoxide init zsh)"
alias cd='z'
alias cdi='zi'

# Starship (must be last)
eval "$(starship init zsh)"
```

---

## 8. Language runtimes

### Python (pyenv)

```bash
brew install pyenv pyenv-virtualenv
```

Add to `~/.zshrc`:

```zsh
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

Install a Python version:

```bash
pyenv install 3.13
pyenv global 3.13
```

### Node (via Homebrew)

```bash
brew install node@22
export PATH="/opt/homebrew/opt/node@22/bin:$PATH"  # add to ~/.zshrc
```

Or use `nvm`:

```bash
brew install nvm
```

### Ruby (rbenv)

```bash
brew install rbenv ruby-build
eval "$(rbenv init - zsh)"  # add to ~/.zshrc
rbenv install 3.3.0
rbenv global 3.3.0
```

---

## 9. Dev tools

```bash
brew install \
  neovim \
  awscli \
  cmake \
  postgresql@14 \
  openjdk
```

VS Code: [https://code.visualstudio.com/](https://code.visualstudio.com/)

---

## 10. Useful macOS defaults

```bash
# Finder: show path bar, status bar, hidden files
defaults write com.apple.finder ShowPathbar -bool true
defaults write com.apple.finder ShowStatusBar -bool true
defaults write com.apple.finder AppleShowAllFiles -bool true

# Keyboard: fast key repeat
defaults write NSGlobalDomain KeyRepeat -int 2
defaults write NSGlobalDomain InitialKeyRepeat -int 15
defaults write NSGlobalDomain ApplePressAndHoldEnabled -bool false

killall Finder
```

---

## Repo structure

```
home/.config/kitty/     → ~/.config/kitty/
home/.config/starship.toml → ~/.config/starship.toml
```
