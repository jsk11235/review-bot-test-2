#!/bin/bash
# Project-specific setup for the PR review bot.
# Install any toolchains or test dependencies your ci.yml needs.
# This runs on ubuntu-latest before Claude Code.
#
# Examples:
#   pip install pytest ruff
#   curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
#   source "$HOME/.cargo/env"

set -euo pipefail

echo "No project-specific setup configured. Edit .github/review-bot-setup.sh"
