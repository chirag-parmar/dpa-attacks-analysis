# Algorithm 7 - dth-order secure AES computation

import random
from  algorithm5 import *
import numpy as np

d = 8
p = 0x01


s = np.empty(d+1, dtype=int)
s[0] = p #p stands for plaintext

# state masking

for i in range (1, d+1):
    s[i] = random.randint(0, 255)
    s[0] = s[0] ^ s[i]

y = sec_sbox_aes(s)
result = 0

for r in y:
    result ^= r

print(hex(result))