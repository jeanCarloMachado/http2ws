#!/usr/bin/env bash

pkill -f http.server
pkill -f websocket.py
pkill -f webserver.py
pkill -f main.sh

rm -rf /tmp/http2ws_sock

exit 0
