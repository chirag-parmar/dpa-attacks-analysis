import h5py  # Add support for hdf5 files
import numpy as np  # Add support for matrix manipulations

# path of the traces hdf5 file which will be used in the dpa analysis
base_path = './traces/'

class Reader:

    def __init__(self, filename):
        self.hdf5_file = h5py.File(base_path + filename + ".h5", "r")

    def get_traces(self):

        traces = {}

        for key in self.hdf5_file.keys():
            if key.startswith("traces"):
                temp = key.split("_", 1)[1]
                sd = float(temp.replace("_", "."))
                traces[sd] = self.hdf5_file[key][:].astype(np.uint8)

        return traces

    def get_intermediates(self):

        intermediates = {}

        for key in self.hdf5_file.keys():
            if key.startswith("intermediates"):
                temp = key.split("_", 1)[1]
                sd = float(temp.replace("_", "."))
                intermediates[sd] = self.hdf5_file[key][:].astype(np.uint8)

        return intermediates

    def get_inputs(self):
        inputs = self.hdf5_file["inputs"][:].astype(np.uint8)
        return inputs

    def get_d(self):
        d = self.hdf5_file["d"][0].astype(np.int)
        return d

