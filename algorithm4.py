# Algorithm 4 - RefreshMasks

import random
import os
import numpy as np

def refresh_masks(byte_x_array):
    
    d = len(byte_x_array)

    for i in range(1,d+1):
        t = random.randint(0, 255)
	byte_x_array[0] = byte_x_array[0] + t
	byte_x_array[i] = byte_x_array[i] + t
    
    return byte_x_array

