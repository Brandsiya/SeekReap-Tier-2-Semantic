#!/bin/sh
if git diff --name-only HEAD~1 | grep -q '^README.md$'; then
  git diff --name-only HEAD~1 | grep -q '^docs/governance/' || exit 1
fi
