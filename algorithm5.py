# Algorithm 5 - AES S-box

import algorithm3

af_matrix = [[1,0,0,0,1,1,1,1],
             [1,1,0,0,0,1,1,1],
             [1,1,1,0,0,0,1,1],
             [1,1,1,1,0,0,0,1],
             [1,1,1,1,1,0,0,0],
             [0,1,1,1,1,1,0,0],
             [0,0,1,1,1,1,1,0],
             [0,0,0,1,1,1,1,1]]

v = [1,1,0,0,0,1,1,0]

def at (a, i):
    for j in range (7):
            c += af_matrix[i][j] * a[j]
    c = c ^ v[i]
    return c



def sec_sbox_aes ( byte_array_x):
    byte_array_y = sec_exp_254(byte_array_x)
    for i in range (d+1):
        byte_array_y[i] = at(byte_array_y[i], i)
        byte_array_y[0] = byte_array_y[0] + b'\63'

    byte_array_y[0] = byte_array_y[0] + b'\63'
    return byte_array_y
