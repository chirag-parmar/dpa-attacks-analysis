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
        x[0] ^= t
        x[i] ^= t

    return x

# test for checking refresh masks
# x = [23, 255, 47, 68, 97]

# def combine(arr):
#     res = 0
#     for share in arr:
#         res ^= share
    
#     return res

# print(x)
# refresh_x = refresh_masks(x)
# print(refresh_x)
# print(combine(refresh_x) == combine(x))
