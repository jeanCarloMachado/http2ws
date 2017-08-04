# http2ws

A message subscription system that pushes messages in http and deliver to subscribed websocket clients - ideal for notifications systems. Where the client is the browser and you have multiple api's sending messages.

## Send a new message

```sh
curl -X POST http://localhost:5000/send -H "Content-Type: application/json" -d '{"recipient":"gandalf","content":"my_message"}'

```


## Consume the message

```sh
var exampleSocket = new WebSocket("ws://localhost:8765");
exampleSocket.onopen = function (event) {

    exampleSocket.send('{"recipient": "'+"gandalf"+'"}');
};
exampleSocket.onmessage = function (event) {
  console.log(event.data)
}


```
