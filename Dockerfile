FROM  python:alpine3.6

RUN pip install websockets flask

ADD config.py /config.py
ADD websocket.py /websocket.py
ADD webserver.py /webserver.py
ADD main.sh /main.sh
WORKDIR /

EXPOSE 5000
EXPOSE 8765

ENTRYPOINT ./main.sh
