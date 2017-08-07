.PHONY: example
all: serve

serve:
	./main.sh

example:
	cd example ; python -m http.server 8001
	${BROWSER} http://localhost:8001

container_build:
	docker build . -t http2ws
deploy:
	docker push compufour/hooks

clean:
	pkill -f 'http.server 8001'

