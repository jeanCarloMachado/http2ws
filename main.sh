#!/bin/sh

DEBUG=1 python websocket.py &
pidWebsocket=$!

DEBUG=1 python webserver.py &
pidWebserver=$!


echo "pidWebserver: $pidWebserver"
echo "pidWebsocket: $pidWebsocket"

tail -f /tmp/http2ws_sock

