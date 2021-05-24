# Algorithm 3 - Secure Inversion in GF(2^8)

import random
import os
from multiplier import *
from algorithm4 import *
from algorithm1 import *
from algorithm2 import *
import numpy as np

# @description: TODO
# @params: x - integer - input array
def sec_exp_254 (x):
    
    d = len(x)
    w = np.empty(d, dtype=int)
    y = np.empty(d, dtype=int)
    z = np.empty(d, dtype=int)

    for i in range (d):
        z[i] = sec_gf_sqr(x[i]) # x ^ 2
    
    refresh_masks(z)
    y = sec_mult(z,x)
     
    for i in range (d):
        w[i] = sec_gf_sqr(sec_gf_sqr(y[i])) # y ^ 4
  
    refresh_masks(w)
    y = sec_mult(y,w)

    for i in range (d):
        y[i] = sec_gf_sqr(sec_gf_sqr(sec_gf_sqr(sec_gf_sqr(y[i])))) # y ^ 16

    y = sec_mult(y,w)
    y = sec_mult(y,z)

    return y

# x = [0xc8, 0xc7]
# y= sec_exp_254(x)
# x_prime = x[0] ^ x[1]
# y_prime = y[0] ^ y[1]
# print(sec_gf_mul(x_prime, y_prime)) # should be equal to 1
