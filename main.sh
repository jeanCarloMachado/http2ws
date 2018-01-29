#!/bin/sh

DEBUG=1 python websocket.py &
pidWebsocket=$!

echo "pidWebsocket: $pidWebsocket"
DEBUG=1 python webserver.py



