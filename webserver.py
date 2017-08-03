from flask import Flask, request, jsonify
import json

from fifo import *

app = Flask(__name__)
app.debug=True

@app.route('/')
def hello_world():
    return 'Hello socket'

@app.route('/send', methods=['POST'])
def register():
    body=request.json

    fifo = open(filename, 'w', 1)
    fifo.write(body['content'])
    fifo.flush()
    fifo.close()

    return '{"status": "Ok"}'


app.run(host= '0.0.0.0',port=5000)
