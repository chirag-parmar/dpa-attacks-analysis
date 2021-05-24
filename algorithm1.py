# Algorithm1 - SecMult

import random
import multiplier
import os
import numpy as np

# @description: TODO
# @params: a - integer array - first input byte array
#          b - integer array - second input byte array
def sec_mult(a, b):

    d = len(a)
    r = np.zeros((d+1, d+1), dtype=int)
    c = np.empty(d, dtype=int)

    for i in range(d):
        for j in range(i+1,d):
            r[i][j] = random.randint(0, 255)
            r[j][i] = (r[i][j] ^ multiplier.sec_gf_mul(a[i], b[j])) ^ multiplier.sec_gf_mul(a[j], b[i])

    for i in range(d):
        c[i] = multiplier.sec_gf_mul( a[i], b[i])
        for j in range(d):
            if i != j:
                c[i] = c[i]^r[i][j]
 
    return c

# a = [0x01,0x02]
# b = [0x01,0x02]

# print(sec_mult(a, b))
