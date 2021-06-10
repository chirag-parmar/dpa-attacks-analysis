# Algorithm 5 - AES S-box

from algorithm3 import *
import numpy as np

af_vector = [0xF1, 0xE3, 0xC7, 0x8F, 0x1F, 0x3E, 0x7C, 0xF8]

def at(a):
    result_string = ""
    for byte in af_vector:
        temp = add_bits_of_int(byte & a)
        result_string += str(temp)

    result = int(result_string[::-1], 2) # parse the bits inverted

    return  result ^ 0x63

def sec_sbox_aes (x, recorder):
    d = len(x)
    y = sec_exp_254(x, recorder)

    for i in range(d):
        y[i] = at(y[i])
        y[0] = y[0] ^ 0x63

    y[0] = y[0] ^ 0x63

    return y

def add_bits_of_int(a):
    binary_string = "{:08b}".format(a)
    result = 0
    for bit in binary_string:
        result ^= int(bit)

    return result

# print(hex(at(0x00))) # should be 0x63
# print(hex(at(0x01))) # should be 0x7c