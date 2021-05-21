# Algorithm 7 - dth-order secure AES computation

import random
import algorithm5

s[0] = p #p stands for plaintext

# state masking

for i in range (d+1):
    s[i] = random.randint(16 *8)
    s[0] = s[0] ^ s[i]

# all but last rounds

for r in range (0, Nr):
    for i in range (d+1):
        s[i] = s[i] ^ k[i][r]
    for l,j in range (1,5):
        s = sec_sbox_aes (s)
    for i in range (d+1):
        #define mix columns and shift rows

