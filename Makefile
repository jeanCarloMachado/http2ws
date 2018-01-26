.PHONY: example
all: example

clean:
	./clean.sh

example: clean
	debug=1 ./main.sh
	cd example ; python -m http.server 8001 &
	${BROWSER} http://localhost:8001

build:
	docker build . -t jeancarlomachado/http2ws -t http2ws
deploy: build
	docker push jeancarlomachado/http2ws
