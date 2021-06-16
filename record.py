import random
from  algorithm5 import *
import numpy as np
from recorder import *

def record(file, order=0, n_traces=256, zero_masks=False):
    recorder = Recorder()

    d = order

    # if n_traces > pow(256, order+1):
    #     raise Exception("number of traces to be recorded cannot be greater than total possible traces")

    recorder.record_order(d)

    for i in range(n_traces):
        p = i % 256
        recorder.record_input(p)
        s = np.empty(d+1, dtype=int)
        s[0] = p #p stands for plaintext

        # state masking
        for i in range (1, d+1):
            if zero_masks:
                s[i] = 0
            else:
                s[i] = random.randint(0, 255)
            s[0] = s[0] ^ s[i]

        y = sec_sbox_aes(s, recorder)
            
        recorder.save_trace()

    recorder.save_dataset(file)

#record("no_masks")
#record("with_masks_3", 3, n_traces=5000)
record("with_masks_19", 19, n_traces = 5000)
#record("no_masks_1000traces", n_traces=1000)

