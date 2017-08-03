from flask import Flask, request, jsonify
import json

from config import named_pipe_path

app = Flask(__name__)
app.debug=True

@app.route('/')
def hello_world():
    return 'Hello socket'

@app.route('/send', methods=['POST'])
def register():
    fifo = open(named_pipe_path, 'w', 1)
    fifo.write(json.dumps(request.json))
    fifo.flush()
    fifo.close()
    return '{"status": "Ok"}'

app.run(host= '0.0.0.0',port=5000)
