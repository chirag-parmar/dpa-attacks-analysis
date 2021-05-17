# Algorithm 3 - Secure Inversion in GF(2^8)

import random
import os
import multiplier
import algorithm4
import algorithm1


def sec_exp_254 (byte_array_x):
    
    d = len(byte_array_x)

    for i in range (d+1):
        byte_array_z[i] = sec_gf_mul( byte_array_x[i], byte_array_x[i])
    
    refresh_masks(byte_array_z)
    byte_array_y = sec_mult(byte_array_z,byte_array_x)
     
    for i in range (d+1):
        byte_array_w[i] = gf_exp( byte_array_y[i], 4)
  
    refresh_masks(byte_array_w)
    byte_array_y = sec_mult(byte_array_y,byte_array_w)

    for i in range (d+1):
        byte_array_y[i] = gf_exp( byte_array_y[i], 16)

    byte_array_y = sec_mult(byte_array_y,byte_array_w)
    byte_array_y = sec_mult(byte_array_y,byte_array_z)

    return byte_array_y



x = [b'\x07', b'\x00']
print(sec_exp_254 (x))
