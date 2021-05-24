# Algorithm 5 - AES S-box

from algorithm3 import *
import numpy as np

af_matrix = np.array([[1,0,0,0,1,1,1,1],
             [1,1,0,0,0,1,1,1],
             [1,1,1,0,0,0,1,1],
             [1,1,1,1,0,0,0,1],
             [1,1,1,1,1,0,0,0],
             [0,1,1,1,1,1,0,0],
             [0,0,1,1,1,1,1,0],
             [0,0,0,1,1,1,1,1]], dtype=bool)

v = np.array([1,1,0,0,0,1,1,0], dtype=bool)

def at (a):
    # convert byte a to numpy array
    matrix_a = convert_to_binary_array(a)
    result = af_matrix.dot(matrix_a)
    result_byte = np.packbits(np.uint8(np.flip(result)))[0]
    return result_byte ^ 0x63
    # return result_byte

def sec_sbox_aes (x):
    d = len(x)
    y = sec_exp_254(x)

    for i in range (d):
        y[i] = at(y[i])
        y[0] = y[0] ^ 0x63

    y[0] = y[0] ^ 0x63
    return y

def convert_to_binary_array(a):
    binary_string = "{:08b}".format(a)
    binary_array = []
    for bit in binary_string:
        binary_array.append(int(bit))

    return np.array(binary_array, dtype=bool)
