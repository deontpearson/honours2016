#!/bin/bash
# Builds the main.py file with custom modules, then runs the main.py file
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BUILD="$DIR/build-server.sh"
START="$DIR/start-server.sh ip=xxx.xxx.xxx.xxx port=80 debug=false"
sudo $BUILD
sudo $START
