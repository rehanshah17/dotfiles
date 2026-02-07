#!/usr/bin/env bash
# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Kitty: SSH Host
# @raycast.mode silent
# @raycast.packageName Terminal
#
# Optional parameters:
# @raycast.icon 🔐
# @raycast.description Pick an SSH host from ~/.ssh/config and open in Kitty

exec "$HOME/.local/bin/kssh"

