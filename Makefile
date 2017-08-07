.PHONY: example
all: example

example: clean
	python webserver.py &
	python websocket.py &
	cd example ; python -m http.server 8001 &
	${BROWSER} http://localhost:8001

container_build:
	docker build . -t http2ws
deploy:
	docker push compufour/hooks

clean:
	-pkill -f websocket.py
	-pkill -f webserver.py
	-pkill -f "http.server 8001" || true
