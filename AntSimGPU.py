# import json
# http://127.0.0.1:5000/

from __future__ import division
from numba import cuda
#from flask import Flask
import numpy
import math



# CUDA kernel
@cuda.jit
def my_kernel(io_array):
    pos = cuda.grid(1)
    if pos < io_array.size:
        io_array[pos] *= 2 # do the computation

# Host code   
data = numpy.ones(256)
threadsperblock = 256
blockspergrid = math.ceil(data.shape[0] / threadsperblock)
my_kernel[blockspergrid, threadsperblock](data)
print(data)







#app = Flask(__name__)

#@app.route('/')
#def hello_world():
#   return 'Hello World'

#if __name__ == '__main__':
#   app.run() 
   # app.run(host='127.0.0.1',port=8000,debug=True)

