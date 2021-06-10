import h5py  # Add support for hdf5 files
import numpy as np  # Add support for matrix manipulations
from hamming import *

# base path for datasets
basepath = './traces/'

class Recorder:
    """Class used to load traces measured with measuring script."""

    def __init__(self):
        self.trace = []
        self.traces = {}
        self.intermediate = []
        self.intermediates = {}
        self.inputs = []
        self.d = []

    def save_dataset(self, filename):
        self.hdf5_file = h5py.File(basepath + filename + ".h5", "w")

        for sd in self.traces.keys():
            self.hdf5_file.create_dataset("traces_" + str(sd), data=self.traces[sd], dtype=np.float64)
            self.hdf5_file.create_dataset("intermediates_" + str(sd), data=self.intermediates[sd], dtype=np.float64)
        
        self.hdf5_file.create_dataset("inputs", data=self.inputs, dtype=np.uint8)
        self.hdf5_file.create_dataset("d", data=self.d, dtype=np.uint8)
        self.hdf5_file.close()

    def record_order(self, d):
        self.d = [d]

    def record_values(self, values):
        for value in values:       
            self.trace.append(get_hamming_weight(value))

        self.intermediate.extend(values)

    def record_input(self, input):
        self.inputs.append(input)
    
    def save_trace(self):
        trace = np.array(self.trace)
        intermediate = np.array(self.intermediate)

        for l in range(0, 30, 2):
            sd = round(l/10, 1)
            noise = np.random.normal(4, sd, trace.shape)
            intermediate_noise = np.random.normal(128, sd, intermediate.shape)

            if sd not in self.traces.keys():
                self.traces[sd] = []

            if sd not in self.intermediates.keys():
                self.intermediates[sd] = [] 
                     
            self.traces[sd].append(trace + noise)
            self.intermediates[sd].append(intermediate + intermediate_noise)

        self.trace = []
        self.intermediate = []

    def get_trace_hypothesis(self):
        # TODO: Print warning because this function can be only used properly with d=0
        return np.array(self.traces[0.0])

    def get_intermediate_hypothesis(self):
        # TODO: Print warning because this function can be only used properly with d=0
        return np.array(self.traces[0.0])




