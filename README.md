# Web2Sock


## Send a new message


```sh
curl -X POST http://localhost:5000/send -H "Content-Type: application/json" -d '{"recipient":"my_recipient","content":"my_message"}'

```


## Consume the message

```sh
var exampleSocket = new WebSocket("ws://localhost:8765");
exampleSocket.onopen = function (event) {
    console.log('opened')
};
exampleSocket.onmessage = function (event) {
  console.log(event.data)
}


```
