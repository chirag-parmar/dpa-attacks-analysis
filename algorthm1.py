# Algorithm1 - SecMult

import random;

r = [][];
a,b = [];
c = [];

for i in range(d+1):
    for j in range(i+1,d+1):
        r[i][j] = random.randint(8);
        r[j][i] = (r[i][j] ^ gf_mult( a[i], b[j] )) ^ gf_mult( a[j], b[i]);

for i in range(d+1):
    c[i] = gf_mult( a[i], b[i]);
    for j in range(d+1):
        if i != j:
            c[i] = c[i]^r[i][j];
