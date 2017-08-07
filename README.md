# http2ws

A simple and fast message subscription system that pushes messages in http and deliver to subscribed websocket clients. Ideal for notifications systems. Where the client is the browser and you have multiple api's sending messages.

## Send a new message

```sh
curl -X POST http://localhost:5000/send -H "Content-Type: application/json" -d '{"recipient":"gandalf","content":"my_message"}'

```


## Consume the message

```sh
var exampleSocket = new WebSocket("ws://localhost:8765");
exampleSocket.onopen = function (event) {
    //list every message to the recipient gandalf
    exampleSocket.send('{"recipient": "'+"gandalf"+'"}');
};
exampleSocket.onmessage = function (event) {
  console.log(event.data)
}

```

## Configuring


By default the webserver port is 5000  and websocket port is 8765
you can change it by setting the following variables

```sh
HTTP2WS_WEBSERVER_PORT=5001 python webserver.py
HTTP2WS_WEBSOCKET_PORT=8764 python websocket.py
HTTP2WS_WEBSOCKET_HOST=172.17.0.1
```

## SSL

Set the following variables if you want to use ssl

```sh
HTTP2WS_SSL_CERT=/tmp/hmg/file.cert HTTP2WS_SSL_KEY=/tmp/hmg/file_key.cert python websocket.py

```
## Container

```sh
docker run -p 5000:5000 -p 8765:8765 http2ws:latest
```

## License

The content of this project itself is licensed under the Creative
Commons Attribution 3.0 license, and the underlying source code used to
format and display that content is licensed under the MIT license.
