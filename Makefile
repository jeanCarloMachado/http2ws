.PHONY: example
all: example

clean:
	./clean.sh

serve: clean
	debug=1 ./main.sh &

browseExample:
	${BROWSER} http://localhost:8001

example: serve browseExample
	cd example ; python -m http.server 8001 &

build:
	docker build . -t jeancarlomachado/http2ws -t http2ws
deploy: build
	docker push jeancarlomachado/http2ws
