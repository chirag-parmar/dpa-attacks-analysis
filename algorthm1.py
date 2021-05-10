# Algorithm1 - SecMult

import random
import multiplier
import os
import numpy as np

d = 2
r = [[0, 0], [0 , 0]]
a = [b'\x07', b'\x00']
b = [b'\x0b', b'\x00']
c = [0 , 0]

for i in range(d):
    for j in range(i+1,d):
        r[i][j] = random.randint(0, 255)
        r[j][i] = (r[i][j] ^ int(multiplier.sec_gf_mul( a[i], b[j] ), 16)) ^ int(multiplier.sec_gf_mul( a[j], b[i]), 16)

for i in range(d):
    c[i] = int(multiplier.sec_gf_mul( a[i], b[i]), 16)
    for j in range(d):
        if i != j:
            c[i] = c[i]^r[i][j]
