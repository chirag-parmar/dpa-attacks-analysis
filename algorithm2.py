# Algorithm 2 - Inversion

import multiplier
import random

#x = bytes(random.randint(0, 255))
x = b'\x0b'
z = multiplier.sec_gf_mul(x, x)

y = multiplier.sec_gf_mul(x,z)

print(multiplier.sec_gf_mul(y,multiplier.sec_gf_mul(y, multiplier.sec_gf_mul(y,y))))
print(multiplier.gf_exp(y,4))



#y = multiplier.sec_gf_mul(y,w)

#y = 
