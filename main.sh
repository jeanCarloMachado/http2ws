#!/bin/sh

rm -rf /tmp/http2ws_sock || true

DEBUG=1 python websocket.py &
pidWebsocket=$!
sleep 2

DEBUG=1 python webserver.py &
pidWebserver=$!
sleep 2

echo "pidWebserver: $pidWebserver"
echo "pidWebsocket: $pidWebsocket"

tail -f /tmp/http2ws_sock

