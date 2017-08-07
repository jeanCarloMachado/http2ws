#!/usr/bin/env sh


# cleanup() {
#     pkill -f websocket.py
#     pkill -f webserver.py
# }
# trap cleanup EXIT SIGINT SIGTERM

python webserver.py
#python websocket.py


