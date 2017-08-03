import asyncio
import websockets
import sys
import os, tempfile
from signal import *
from fifo import *
import threading
from queue import Queue

if not os.path.exists(filename):
    try:
        os.mkfifo(filename)
    except OSError as oe:
        if oe.errno != errno.EEXIST:
            raise


my_queue = Queue(maxsize=0)
connected = set()

async def connectionHandler(websocket, path):
    global connected

    connected.add(websocket)
    try:
        # Implement logic here.
        await asyncio.wait([ws.send("Hello!") for ws in connected])
        await asyncio.sleep(10)
    finally:
        # Unregister.
        connected.remove(websocket)


def read_file_callback():
    tmp = fifo.read()
    if tmp != "":
        my_queue.put(tmp)


async def send_messages():
    global connected
    while True:
        message = my_queue.get()
        for i in connected:
            if i.state_name == 'OPEN':
                await i.send(message)




def socket_thread():
    second_loop = asyncio.new_event_loop()
    start_server = websockets.serve(connectionHandler, 'localhost', 8765)
    second_loop.run_until_complete(start_server)
    second_loop.run_forever()
    return

def dispatch_thread():
    third_loop = asyncio.new_event_loop()
    third_loop.run_until_complete(send_messages())
    third_loop.run_forever()
    return

threads = []
t = threading.Thread(target=socket_thread)
threads.append(t)
t2 = threading.Thread(target=dispatch_thread)
threads.append(t2)
t.start()
t2.start()
loop = asyncio.get_event_loop()
fifo = open(filename, 'r', 1)
loop.add_reader(fifo.fileno(), read_file_callback)
loop.run_forever()

def clean(*args):
    os.remove(filename)
    sys.exit(0)

for sig in (SIGABRT, SIGILL, SIGINT, SIGSEGV, SIGTERM):
    signal(sig, clean)

