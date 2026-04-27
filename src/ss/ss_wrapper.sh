#!/usr/bin/env bash
# Structured Skills (ss) CLI Wrapper

# Ensure the current directory is in PYTHONPATH so the 'ss' package is found
export PYTHONPATH=$PYTHONPATH:.

# Execute the CLI module
exec python3 -m ss.cli "$@"
