#!/bin/sh

ps -ax | egrep "webserver\.py|websocket\.py"  | cut -d ' ' -f1 | xargs kill -9

DEBUG=1 python webserver.py &
pidWebserver=$!
DEBUG=1 python websocket.py &
pidWebsocket=$!

echo "pidWebserver: $pidWebserver"
echo "pidWebsocket: $pidWebsocket"

tail -f /tmp/http2ws_sock
