# Algorithm 2 - Inversion

import multiplier
import random

def inversion (x):

    z = multiplier.sec_gf_mul(x, x)

    y = multiplier.sec_gf_mul(x,z)

    #print(multiplier.sec_gf_mul(y,multiplier.sec_gf_mul(y, multiplier.sec_gf_mul(y,y))))
    #print(multiplier.gf_exp(y,4))

    #w = multiplier.gf_exp(y,4)
    w = multiplier.sec_gf_sqr(y)
    w = multiplier.sec_gf_sqr(w)

    y = multiplier.sec_gf_mul(y,w)

    #y = multiplier.gf_exp(y,16)
    y = multiplier.sec_gf_sqr(y)
    y = multiplier.sec_gf_sqr(y)
    y = multiplier.sec_gf_sqr(y)
    y = multiplier.sec_gf_sqr(y)

    y = multiplier.sec_gf_mul(y,w)

    y = multiplier.sec_gf_mul(y,z)

    return y

x = bytes(random.randint(0, 255))
#x = b'\x0b'
print(inversion(x))
