.PHONY: example
all: example

example: clean
	python webserver.py &
	python websocket.py &
	cd example ; python -m http.server 8001 &
	${BROWSER} http://localhost:8001

container_build:
	docker build . -t jeancarlomachado/http2ws
deploy: container_build
	docker push jeancarlomachado/http2ws
clean:
	-pkill -f websocket.py
	-pkill -f webserver.py
	-pkill -f "http.server 8001" || true
