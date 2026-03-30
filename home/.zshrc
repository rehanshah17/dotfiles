# Homebrew first so all tools resolve correctly
export PATH="/opt/homebrew/bin:$PATH"
export PATH="/opt/homebrew/sbin:$PATH"

# Oh My Zsh
export ZSH="$HOME/.oh-my-zsh"
ZSH_THEME=""
plugins=(git)
# Keep ls theming managed locally instead of Oh My Zsh defaults
DISABLE_LS_COLORS="true"

source $ZSH/oh-my-zsh.sh

# ls output tuned to Starship chalk palette and stable spacing
export CLICOLOR=1
export LSCOLORS="ExGxFxDxCxegedabagacad"
if command -v eza >/dev/null 2>&1; then
  # Plain-weight colors (no bold) to avoid thick rendering
  export EZA_COLORS="di=34:ex=32:fi=0:ln=36:or=31:sn=35:uu=33:gu=33"
  alias ls='eza --group-directories-first --color=auto --icons=never'
elif command -v gls >/dev/null 2>&1; then
  export LS_COLORS="di=34:ln=36:so=35:pi=33:ex=32:bd=34;46:cd=34;43:su=30;41:sg=30;46:tw=30;42:ow=30;43"
  alias ls='gls --color=tty --group-directories-first'
else
  alias ls='ls -G'
fi


# VS Code helper
code () {
  VSCODE_CWD="$PWD" open -n -b "com.microsoft.VSCode" --args "$@"
}

# pyenv (guarded)
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
if command -v pyenv >/dev/null; then
  eval "$(pyenv init -)"
  eval "$(pyenv virtualenv-init -)"
fi

# Node
export PATH="/opt/homebrew/opt/node@22/bin:$PATH"

# C++ / OpenSSL
export CPLUS_INCLUDE_PATH=/Library/Developer/CommandLineTools/SDKs/MacOSX.sdk/usr/include/c++/v1
export OPENSSL_ROOT_DIR=/opt/homebrew/opt/openssl@3

# Local binaries
export PATH="$HOME/.local/bin:$PATH"

# Ruby (guarded)
if command -v rbenv >/dev/null; then
  export PATH="/opt/homebrew/opt/ruby/bin:$PATH"
  export PATH="$(gem environment gemdir)/bin:$PATH"
  eval "$(rbenv init - zsh)"
fi

# Postgres
export PATH="/opt/homebrew/opt/postgresql@16/bin:$PATH"

# Completion system
autoload -Uz compinit
compinit

# Carapace
# Keep bridges lean for faster completion startup.
if command -v carapace >/dev/null 2>&1; then
  export CARAPACE_BRIDGES='zsh,bash,fish'
  source <(carapace _carapace zsh)
fi

# direnv (auto-load per-project envs when installed)
if command -v direnv >/dev/null 2>&1; then
  eval "$(direnv hook zsh)"
fi

# fzf (Ctrl+R history, Alt+C cd, tab completion)
# Guard for non-TTY shells (e.g. scripted `zsh -ic`).
if [[ -o interactive ]] && [[ -t 0 ]] && [[ -t 1 ]]; then
  if [[ -r /opt/homebrew/opt/fzf/shell/completion.zsh ]]; then
    source /opt/homebrew/opt/fzf/shell/completion.zsh
  fi
  if [[ -r /opt/homebrew/opt/fzf/shell/key-bindings.zsh ]]; then
    source /opt/homebrew/opt/fzf/shell/key-bindings.zsh
  fi

  export FZF_DEFAULT_OPTS="${FZF_DEFAULT_OPTS:-} --height=60% --layout=reverse --border --prompt='❯ '"
fi

# Zoxide (before Starship)
eval "$(zoxide init zsh)"

# Make `cd` use zoxide (interactive shells)
if [[ -o interactive ]]; then
  alias cd='z'
  alias cdi='zi'
fi

# Starship (last renderer)
eval "$(starship init zsh)"

# System aliases
alias ..="cd .."
alias x="exit"
fetch () {
  if command -v fastfetch >/dev/null 2>&1; then
    fastfetch -c ~/.config/fastfetch/config.jsonc 2>/dev/null
    return
  fi
  neofetch --config ~/.config/neofetch/config.conf 2>/dev/null
}
alias nf="fetch"
alias term="~/.local/bin/term"
alias kp="~/.local/bin/kproj"
alias ks="~/.local/bin/kssh"
alias kl="~/.local/bin/klog"
alias dots="~/.local/bin/dotfiles-snapshot"
alias inbox="cd ~/Inbox"
alias dlinbox="cd ~/Inbox/Downloads"
alias sortbox="cd ~/Inbox/ToSort"
alias mvdl="~/.local/bin/move-downloads-to-inbox"
alias inboxmv="~/.local/bin/inbox-mv"

# Git aliases
alias add="git add"
alias commit="git commit"
alias pull="git pull"
alias stat="git status"
alias gdiff="git diff HEAD"
alias vdiff="git difftool HEAD"
alias log="git log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit"
alias cfg="git --git-dir=$HOME/dotfiles/ --work-tree=$HOME"
alias push="git push"
alias g="lazygit"

# Colors
source ~/.config/colors.sh
export PATH="/opt/homebrew/opt/openjdk/bin:$PATH"

# The next line updates PATH for the Google Cloud SDK.
if [ -f '/Users/rehanshah/google-cloud-sdk/path.zsh.inc' ]; then . '/Users/rehanshah/google-cloud-sdk/path.zsh.inc'; fi

# The next line enables shell command completion for gcloud.
if [ -f '/Users/rehanshah/google-cloud-sdk/completion.zsh.inc' ]; then . '/Users/rehanshah/google-cloud-sdk/completion.zsh.inc'; fi
