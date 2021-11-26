# http://127.0.0.1:5000/


import websockets
import asyncio

PORT = 5000

print("Server listening on Port " + str(PORT))

async def echo(websocket, path):
    print("A client just connected")
    try:
        async for message in websocket:
            print("Received message from client: " + message)
            await websocket.send("Pong: " + message)
    except websockets.exceptions.ConnectionClosed as e:
        print("A client just disconnected")

start_server = websockets.serve(echo, "localhost", PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()



























"""
from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
   
app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('connect')
def test_connect(auth):
    print("Connected")
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect')
def test_disconnect():
    print("Disconnected")



@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)


if __name__ == '__main__':
    socketio.run(app)
"""




"""
from __future__ import division
from numba import cuda

# CUDA kernel
@cuda.jit
def my_kernel(io_array):
    pos = cuda.grid(1)
    if pos < io_array.size:
        io_array[pos] *= 2 # do the computation


import numpy
import math

@app.route('/')
def hello_world():
    data = numpy.ones(256)
    threadsperblock = 256
    blockspergrid = math.ceil(data.shape[0] / threadsperblock)
    my_kernel[blockspergrid, threadsperblock](data)
    out_arr = numpy.array_str(data)    
    return out_arr
   #return 'Hello World'

   app.run(host='127.0.0.1',port=8000,debug=True)
"""
