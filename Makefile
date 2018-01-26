.PHONY: example
all: example

example: clean
	python webserver.py &
	DEBUG=1 python websocket.py &
	#DEBUG=1 HTTP2WS_SSL_CERT=/tmp/hmg/file.cert HTTP2WS_SSL_KEY=/tmp/hmg/file_key.cert python websocket.py &
	cd example ; python -m http.server 8001 &
	${BROWSER} http://localhost:8001

build:
	docker build . -t jeancarlomachado/http2ws -t http2ws
deploy: build
	docker push jeancarlomachado/http2ws
