#!/bin/bash
# Builds the main.py file with custom modules, then runs the main.py file
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo "Starting..."
if [ $# -lt 2 ]; then
    echo "bash usage: start-server.sh ip=IP port=PORT"
else
  for a in "$@"
  do
    case $a in
      ip=*)
      IP="${a#*=}"
      shift # past argument=value
      ;;
      port=*)
      PORT="${a#*=}"
      shift # past argument=value
      ;;
      debug=*)
      DEBUG="${a#*=}"
      shift # past argument=value
      ;;
      ssl=*)
      SSL="${a#*=}"
      shift # past argument=value
      ;;
      --default)
      DEFAULT=YES
      shift # move past unknown value
      ;;
      *)
      ;;
    esac
  done

  if [ "$DEBUG" == true ]; then
    if [ "$SSL" == true ]; then
      S="$DIR/server.py -i $IP -p $PORT -d -s"
    else
      S="$DIR/server.py -i $IP -p $PORT -d"
    fi
  else
    if [ "$SSL" == true ]; then
      S="$DIR/server.py -i $IP -p $PORT -s"
    else
      S="$DIR/server.py -i $IP -p $PORT"
    fi
  fi
  python $S || echo "FAILED"
fi
