#!/usr/bin/env bash

ps -ax | egrep "webserver\.py|websocket\.py"  | cut -d ' ' -f1 | xargs kill -9 

exit 0
