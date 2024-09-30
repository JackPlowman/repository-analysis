#!/bin/sh
set -e +x

cd ..
cd ..
# Echo cwd
echo "Current working directory: $(pwd)"
# Show files
ls -la

printenv

# Run the analyser
python -m analyser
