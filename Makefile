all: serve

serve:
	./main.sh

container_build:
	docker build . -t compufour/hooks
deploy:
	docker push compufour/hooks
