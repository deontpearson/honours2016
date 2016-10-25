#!/bin/bash
# Builds the main.py file with custom modules, then runs the main.py file
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BUILD="$DIR/build-server.sh"
#START="$DIR/start-server.sh ip=146.231.123.9 port=80 debug=true ssl=false"
START="$DIR/start-server.sh ip= port=443 debug=false ssl=true"
#START="$DIR/start-server.sh ip=146.231.123.9 port=80 debug=false ssl=false"
sudo $BUILD
sudo $START
