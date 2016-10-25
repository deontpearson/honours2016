#!/bin/bash
# Builds the main.py file with custom modules, then runs the main.py file
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo "Building..."
B="$DIR/build.py"
python $B
if [ $? -eq 0 ]; then
  echo "Build Success!"
else
  echo "Build Failed!"
fi
