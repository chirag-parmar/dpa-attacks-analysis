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

        for sd in self.intermediates.keys():
            self.hdf5_file.create_dataset("intermediates_" + str(sd), data=self.intermediates[sd], dtype=np.float64)
        
        self.hdf5_file.create_dataset("inputs", data=self.inputs, dtype=np.uint8)
        self.hdf5_file.create_dataset("d", data=self.d, dtype=np.uint8)
        self.hdf5_file.close()

    def record_order(self, d):
        self.d = [d]

    def record_values(self, values):
        for value in values:       
            self.trace.append(get_hamming_weight(value))
            self.intermediate.append(float(value))

    def record_input(self, input):
        self.inputs.append(input)
    
    def save_trace(self):
        trace = np.array(self.trace)
        intermediate = np.array(self.intermediate)

        for l in range(0, 300, 2):
            sd = round(l/100, 2)
            noise = np.random.normal(0, sd, trace.shape)

            if sd not in self.traces.keys():
                self.traces[sd] = []
                     
            self.traces[sd].append(trace + noise)

        for l in range(0, 200, 2):
            sd = round(l/10, 2)
            intermediate_noise = np.random.normal(0, sd, intermediate.shape)

            if sd not in self.intermediates.keys():
                self.intermediates[sd] = [] 
                     
            self.intermediates[sd].append(intermediate + intermediate_noise)

        self.trace = []
        self.intermediate = []

    def get_trace_hypothesis(self):
        # TODO: Print warning because this function can be only used properly with d=0
        return np.array(self.traces[0.0])

    def get_intermediate_hypothesis(self):
        # TODO: Print warning because this function can be only used properly with d=0
        return np.array(self.intermediates[0.0])




