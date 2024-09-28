#!/bin/bash
set -e +x

just install
just ruff-fix
