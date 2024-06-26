# Algorithm 2 - Inversion

from multiplier import *
import random

def inversion (x):

    z = sec_gf_sqr(x)

    y = sec_gf_mul(x,z)

    w = sec_gf_sqr(sec_gf_sqr(y)) # y^4

    y = sec_gf_mul(y,w)

    y = sec_gf_sqr(sec_gf_sqr(sec_gf_sqr(sec_gf_sqr(y)))) # y^16

    y = sec_gf_mul(y,w)

    y = sec_gf_mul(y,z)

    return y

# x = bytes(random.randint(0, 255))
# #x = b'\x0b'
# print(inversion(x))
