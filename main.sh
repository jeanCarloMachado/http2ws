#!/bin/sh

DEBUG=1 python websocket.py 1>&2 &
DEBUG=1 python webserver.py 1>&2

