from hamming import *
import numpy as np

weight_dict = {}

# sort bytes by weight
for i in range(256):
    w = get_hamming_weight(i)

    if w not in weight_dict.keys():
        weight_dict[w] = []

    weight_dict[w].append(i)

xor_weight_dict = {}

for j in range(9):
    weight_j_bytes = weight_dict[j]
    for k in range(j, 9):
        weight_k_bytes = weight_dict[k]
        for byte_j in weight_j_bytes:
            for byte_k in weight_k_bytes:
                key = str(j) + str(k)

                if key not in xor_weight_dict.keys():
                    xor_weight_dict[key] = []
                
                xor_weight_dict[key].append(get_hamming_weight(byte_j ^ byte_k))

xor_weights_avg = {}
xor_weights_prob = {}

for key in xor_weight_dict.keys():
    xor_weights_avg[key] = np.mean(xor_weight_dict[key])

for key in xor_weight_dict.keys():
    xor_weights_prob[key] = np.bincount(xor_weight_dict[key]).argmax()

print(xor_weights_avg)
print(xor_weights_prob)