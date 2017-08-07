import asyncio
import websockets
import sys
import os, tempfile
from signal import *
from config import named_pipe_path, websocket_port, websocket_host
import threading
from queue import Queue
import json
import time

debug_mode = (os.getenv('debug') is not None) or False

if not os.path.exists(named_pipe_path):
    try:
        os.mkfifo(named_pipe_path)
    except OSError as oe:
        if oe.errno != errno.EEXIST:
            raise


my_queue = Queue(maxsize=0)
connected_list = []
identified_map = dict()


async def connectionHandler(websocket, path):
    global connected_list
    global identified_map

    connected_list.append(websocket)

    message = await websocket.recv()
    decoded_message = json.loads(message)
    identified_map[decoded_message['recipient']] =  connected_list.index(websocket)
    if debug_mode:
        print ("Add to connected  list index: " + str(connected_list.index(websocket)) + " litening to recipient: " + decoded_message['recipient']) 
    try:
        await asyncio.sleep(3600 * 24)
    finally:
        connected_list.remove(websocket)


def read_file_callback():
    time.sleep(0.2)
    tmp = fifo.read()
    if tmp != "":
        data = json.loads(tmp)
        my_queue.put(data)

async def send_messages():
    global connected_list
    global identified_map
    while True:
        message = my_queue.get()
        if message['recipient'] in identified_map:
            connected_index = identified_map[message['recipient']]
            if debug_mode:
                print ("Connected  list index: " + str(connected_index))
            i = connected_list[connected_index]
            if i.state_name == 'OPEN':
                data = {"content": message['content']}
                await i.send(json.dumps(data))

        else:
            if debug_mode:
                print ("No one listening to recipient: " + message['recipient'])



def websocket_thread():
    second_loop = asyncio.new_event_loop()
    start_server = websockets.serve(connectionHandler, websocket_host, websocket_port)
    second_loop.run_until_complete(start_server)
    second_loop.run_forever()
    return

def message_dispatch_thread():
    third_loop = asyncio.new_event_loop()
    third_loop.run_until_complete(send_messages())
    third_loop.run_forever()
    return

threads = []
t = threading.Thread(target=websocket_thread)
threads.append(t)
t.start()
t2 = threading.Thread(target=message_dispatch_thread)
threads.append(t2)
t2.start()

loop = asyncio.get_event_loop()
fifo = open(named_pipe_path, 'r', 1)
loop.add_reader(fifo.fileno(), read_file_callback)
loop.run_forever()

def clean(*args):
    os.remove(named_pipe_path)
    sys.exit(0)

for sig in (SIGABRT, SIGILL, SIGINT, SIGSEGV, SIGTERM):
    signal(sig, clean)

