# Algorithm 4 - RefreshMasks

import random
import os
import numpy as np

# @description: TODO
# @params: x - integer - input array
def refresh_masks(x):
    d = len(x)
    for i in range (1, d) :
        t = random.randint(0, 255)
        x[0] = x[0] ^ t
        x[i] = x[i] ^ t

    return x

# x = [23, 255]
# print(refresh_masks(x))
