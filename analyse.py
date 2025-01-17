from reader import Reader
from recorder import Recorder
import record
import numpy as np
import matplotlib.pyplot as plt
from  algorithm5 import *
import time

def calculate_corr(hypothesis, traces):
    # calculagte correlation
    coeff_matrix = np.corrcoef(hypothesis, traces)
    x, y = hypothesis.shape
    
    # remove unnecessary columns and rows from correlation matrix
    # first few hypothesis rows and last few trace columns
    coeff_matrix = coeff_matrix[:x, x:]

    return coeff_matrix

def plot_corr(title, hypothesis, traces):

    coeff_matrix = calculate_corr(hypothesis, traces)

    # plot the above matrix row wise i.e. per hypothesis
    fig = plt.figure(figsize = (12, 8))
    fig.suptitle(title)

    plot_num = 1
    for hypothesis_corr in coeff_matrix:            
        sub_plot = fig.add_subplot(2, 4, plot_num)
        sub_plot.plot(list(range(1, len(hypothesis_corr)+1)), hypothesis_corr)
        sub_plot.set_ylabel("Corr. Coeff.")
        sub_plot.set_xlabel("Time")
        sub_plot.set_title("Operation #{}".format(plot_num))
        plot_num += 1

    fig.tight_layout()

    filename = "./plots/" + str(time.time()) + ".png"
    plt.savefig(filename) 

    print("Plot Saved  at {}".format(filename))


def plot_numtraces(title, hypothesis, traces):

    corr_numtraces = []
    x_ntraces = []

    for ntrace in range(3,traces.shape[1],10):
        temp_traces = []
        x_ntraces.append(ntrace)
        corr = np.empty((7,1))
        
        # take ntraces column from traces
        temp_traces = traces[:,:ntrace]
        temp_traces = np.asarray(temp_traces)

        # generate correct hypothesis size
        temp_hypothesis = hypothesis[:,:ntrace]
        temp_hypothesis = np.asarray(temp_hypothesis)
        
        coeff_matrix = calculate_corr(temp_hypothesis, temp_traces)

        # take the maximum value per each intermediate step
        corr = np.max(coeff_matrix, axis = 1)
        corr_numtraces.append(corr)
    
    # append correlation for each ntraces value
    # corr_numtraces.shape = [number of intermediate steps, number of iterations of ntraces] 
    corr_numtraces = (np.asarray(corr_numtraces)).T
    
    # plot the above matrix row wise i.e. per hypothesis
    fig = plt.figure(figsize = (12, 8))
    fig.suptitle(title)

    plot_num = 1
    for hypothesis_corr in corr_numtraces:            
        sub_plot = fig.add_subplot(2, 4, plot_num)
        sub_plot.plot(x_ntraces, hypothesis_corr)
        sub_plot.set_title("Operation #{}".format(plot_num))
        sub_plot.set_ylabel("Corr. Coeff.")
        sub_plot.set_xlabel("#traces")
        plot_num += 1

    fig.tight_layout()

    filename = "./plots/" + str(time.time()) + ".png"
    plt.savefig(filename) 

    print("Plot Saved  at {}".format(filename))

def intermediates_compress(bin_size, intermediates):
    
    if len(intermediates[0]) % bin_size != 0:
        raise Exception("Bin size {} does not divide the total number of samples {}".format(bin_size, len(traces[0])))

    compressed_intermediates = []

    for intermediate in intermediates:
        compressed_intermediate = []
        for v in range(0, len(intermediate), bin_size):
            compressed_value = 0
            for l in range(bin_size):
                compressed_value ^= intermediate[v+l]

            compressed_intermediate.append(compressed_value)
        compressed_intermediates.append(compressed_intermediate)

    return np.array(compressed_intermediates)   

def traces_compress(bin_size, traces):
    
    if len(traces[0]) % bin_size != 0:
        raise Exception("Bin size {} does not divide the total number of samples {}".format(bin_size, len(traces[0])))

    compressed_traces = []

    for trace in traces:   
        compressed_traces.append(np.mean(trace.reshape(-1, bin_size), axis=1))

    return np.array(compressed_traces)

def order_1_trace_compress_xor_avg(traces):

    xor_weights = {
        '00': 0.0, '01': 1.0, '02': 2.0, '03': 3.0, '04': 4.0, '05': 5.0, '06': 6.0, 
        '07': 7.0, '08': 8.0, '11': 1.75, '12': 2.5, '13': 3.25, '14': 4.0, '15': 4.75, 
        '16': 5.5, '17': 6.25, '18': 7.0, '22': 3.0, '23': 3.5, '24': 4.0, '25': 4.5, 
        '26': 5.0, '27': 5.5, '28': 6.0, '33': 3.75, '34': 4.0, '35': 4.25, '36': 4.5, 
        '37': 4.75, '38': 5.0, '44': 4.0, '45': 4.0, '46': 4.0, '47': 4.0, '48': 4.0, 
        '55': 3.75, '56': 3.5, '57': 3.25, '58': 3.0, '66': 3.0, '67': 2.5, '68': 2.0, 
        '77': 1.75, '78': 1.0, '88': 0.0
    }

    compressed_traces = []

    for trace in traces:
        compressed_trace = []
        for v in range(0, len(trace), 2):
            key = str(min(trace[v], trace[v+1])) + str(max(trace[v], trace[v+1]))
            compressed_value = xor_weights[key]
            compressed_trace.append(compressed_value)
        compressed_traces.append(compressed_trace)

    return np.array(compressed_traces)

def order_1_trace_compress_xor_prob(traces):

    xor_weights = {
        '00': 0, '01': 1, '02': 2, '03': 3, '04': 4, 
        '05': 5, '06': 6, '07': 7, '08': 8, '11': 2, 
        '12': 3, '13': 4, '14': 3, '15': 4, '16': 5, 
        '17': 6, '18': 7, '22': 4, '23': 3, '24': 4, 
        '25': 5, '26': 4, '27': 5, '28': 6, '33': 4, 
        '34': 3, '35': 4, '36': 5, '37': 4, '38': 5, 
        '44': 4, '45': 3, '46': 4, '47': 3, '48': 4, 
        '55': 4, '56': 3, '57': 4, '58': 3, '66': 4, 
        '67': 3, '68': 2, '77': 2, '78': 1, '88': 0
    }

    compressed_traces = []

    for trace in traces:
        compressed_trace = []
        for v in range(0, len(trace), 2):
            key = str(min(trace[v], trace[v+1])) + str(max(trace[v], trace[v+1]))
            compressed_value = xor_weights[key]
            compressed_trace.append(compressed_value)
        compressed_traces.append(compressed_trace)

    return np.array(compressed_traces)

def analyse(file, order=0):
    reader = Reader(file)

    trace_hypothesis, intermediate_hypothesis = gen_hypothesis(reader.get_inputs())
    traces = reader.get_traces()
    intermediates = reader.get_intermediates()
    
    if order > 0:
        for sd in traces.keys():
            traces[sd] = traces_compress(order+1, traces[sd])
        for sd in intermediates.keys():
            intermediates[sd] = intermediates_compress(order+1, intermediates[sd])

    title = "Dataset: " + file + "\nDataset Order: " + str(reader.get_d()) + "\nAnalysis Order: " + str(order) 

    # analyse traces for sd 0.40
    plot_corr(title + "\nSD: 0.40 \nType: Intermediate Traces", trace_hypothesis.T, traces[0.40].T)

    # analyse intermediates for sd 10.00
    plot_corr(title + "\nSD: 10.00 \nType: Intermediate Values", intermediate_hypothesis.T, intermediates[10.00].T)

    # analyse traces for sd 0.2 wrt ntraces
    plot_numtraces(title + "\nSD: 0.40 \nType: Intermediate Traces", trace_hypothesis.T, traces[0.40].T)

    # analyse traces for sd 0.2 wrt ntraces
    plot_numtraces(title + "\nSD: 0.00 \nType: Intermediate Traces", trace_hypothesis.T, traces[0.00].T)

    # analyse intermediates for sd 10 wrt ntraces
    plot_numtraces(title + "\nSD: 10.00 \nType: Intermediate Values", intermediate_hypothesis.T, intermediates[10.00].T)

     # analyse intermediates for sd 10 wrt ntraces
    plot_numtraces(title + "\nSD: 0.00 \nType: Intermediate Values", intermediate_hypothesis.T, intermediates[0.00].T)
    
    # plot noise versus correlation coeff graph
    plot_noise(title + "\nType: Intermediate Traces", trace_hypothesis, traces)

    # plot noise versus correlation coeff graph
    plot_noise(title + "\nType: Intermediate Values", intermediate_hypothesis, intermediates)

# note: here traces can also be intermediate values but the hypothesis should match the type
def plot_noise(title, hypothesis, traces):

    # plot the above matrix row wise i.e. per hypothesis
    fig = plt.figure(figsize = (12, 8))
    fig.suptitle("Correlation vs Noise" + title)

    x, y = hypothesis.shape

    # analyze per hypothesis or per operation
    for plot_num in range(y):
        vector = hypothesis[:,plot_num]
        sd_indexes = []
        corr_sd = []

        for sd in sorted(traces.keys()):
            sd_indexes.append(sd)
            coeff_matrix = np.corrcoef(vector.T, traces[sd].T)
            coeff_matrix = coeff_matrix[:1,1:]
            corr_sd.append(max(coeff_matrix[0]))

        #print(sd_indexes)

        sub_plot = fig.add_subplot(2, 4, plot_num+1)
        sub_plot.plot(sd_indexes, corr_sd)
        sub_plot.set_xlabel("sd of err")
        sub_plot.set_ylabel("corr. coeff.")
        sub_plot.set_ylim(-1,1)
        sub_plot.set_title("Operation #{}".format(plot_num+1))

    fig.tight_layout()

    filename = "./plots/" + str(time.time()) + ".png"
    plt.savefig(filename) 
    print("Plot Saved  at {}".format(filename))

def analyse_numtraces(d = 0, order = 0):

    title = "\nDataset Order: " + str(d) + "\nAnalysis Order: " + str(order) 

    # analyse traces for sd 0.2 and 2.8
    get_corr_numtraces(title + "\nSD: 0.2 \nType: Intermediate Traces", d, 0.2, order, False)
    get_corr_numtraces(title + "\nSD: 2.8 \nType: Intermediate Traces", d, 2.8, order, False)

    # analyse intermediates for sd 0.2 and 2.8
    get_corr_numtraces(title + "\nSD: 0.2 \nType: Intermediate Values", d, 0.2, order, True)
    get_corr_numtraces(title + "\nSD: 2.8 \nType: Intermediate Values", d, 2.8, order, True)


# generates the correct size for the hypothesis
def gen_hypothesis(inputs):
    recorder = Recorder()

    for p in inputs:
        s = np.empty(1, dtype=int)
        s[0] = p #p stands for plaintext

        y = sec_sbox_aes(s, recorder)
            
        recorder.save_trace()

    trace_hypothesis = recorder.get_trace_hypothesis()
    intermediate_hypothesis = recorder.get_intermediate_hypothesis()
    return trace_hypothesis, intermediate_hypothesis

def analyse_order(file):
    reader = Reader(file)

    trace_hypothesis, intermediate_hypothesis = gen_hypothesis(reader.get_inputs())
    traces = reader.get_traces()
    intermediates = reader.get_intermediates()
    
    title = "Dataset: " + file + "\nDataset Order: " + str(reader.get_d()) 

    # analyse traces for sd 0.40
    plot_order(title + "\nSD: 0.40 \nType: Intermediate Traces", trace_hypothesis.T, traces[0.40], False)

    # analyse intermediates for sd 10.00
    plot_order(title + "\nSD: 10.00 \nType: Intermediate Values", intermediate_hypothesis.T, intermediates[10.00], True)


def plot_order(title, hypothesis, traces, intermediate_values_on):
    corr_order = []
    order_range = [0,1,3,4,9,19]

    for order in order_range:
        temp_traces_order = []
        corr = []
        if (intermediate_values_on):
            temp_traces_order = intermediates_compress(order+1, traces)
        else:
            temp_traces_order = traces_compress(order+1, traces)

        coeff_matrix = calculate_corr(hypothesis, temp_traces_order.T)

        # take the maximum value per each intermediate step
        corr = np.max(coeff_matrix, axis = 1)
        corr_order.append(corr)
    
    # append correlation for each ntraces value
    # corr_numtraces.shape = [number of intermediate steps, number of iterations of ntraces] 
    corr_order = (np.asarray(corr_order)).T
    
    # plot the above matrix row wise i.e. per hypothesis
    fig = plt.figure(figsize = (12, 8))
    fig.suptitle(title)

    plot_num = 1
    for hypothesis_corr in corr_order:            
        sub_plot = fig.add_subplot(2, 4, plot_num)
        sub_plot.plot(order_range, hypothesis_corr)
        sub_plot.set_title("Operation #{}".format(plot_num))
        sub_plot.set_ylabel("Corr. Coeff.")
        sub_plot.set_xlabel("order")
        plot_num += 1

    fig.tight_layout()

    filename = "./plots/" + str(time.time()) + ".png"
    plt.savefig(filename) 

    print("Plot Saved  at {}".format(filename))
        
def plot_order_d(sd, intermediate_values_on): 
    recorder = Recorder()
    r = Reader("no_masks")
    hypothesis, intermediate_hypothesis = gen_hypothesis(r.get_inputs())
    corr_d = []
    x_d = []

    for d in range(0,20,1):
        x_d.append(d)
        temp_traces_d = []
        corr = []
        record.record(str(d), d)
        reader = Reader(str(d))
        traces = reader.get_traces()
        intermediates = reader.get_intermediates()

        
        if(intermediate_values_on):
            if(d > 0):
                intermediates [sd] = intermediates_compress(d+1, intermediates[sd])
            traces[sd] = intermediates[sd]
            hypothesis = intermediate_hypothesis
        else:
            if(d > 0):
                traces[sd] = traces_compress(d+1, traces[sd])

        coeff_matrix = calculate_corr(hypothesis.T, traces[sd].T)
        # take the maximum value per each intermediate step
        corr = np.max(coeff_matrix, axis = 1)
        corr_d.append(corr)
    
    # append correlation for each ntraces value
    # corr_numtraces.shape = [number of intermediate steps, number of iterations of ntraces] 
    corr_d = (np.asarray(corr_d)).T
    
    # plot the above matrix row wise i.e. per hypothesis
    fig = plt.figure(figsize = (12, 8))
    if(intermediate_values_on):
        title = "\nSD:" + str(sd) + "\nType: Intermediate Values" 
    else:
        title = "\nSD:" + str(sd) + "\nType: Intermediate Traces" 
    
    fig.suptitle(title)

    plot_num = 1
    for hypothesis_corr in corr_d:            
        sub_plot = fig.add_subplot(2, 4, plot_num)
        sub_plot.plot(x_d, hypothesis_corr)
        sub_plot.set_title("Operation #{}".format(plot_num))
        sub_plot.set_ylabel("Corr. Coeff.")
        sub_plot.set_xlabel("d")
        plot_num += 1

    fig.tight_layout()

    filename = "./plots/" + str(time.time()) + ".png"
    plt.savefig(filename) 

    print("Plot Saved  at {}".format(filename))

def analyse_different_methods_order_1(file):
    reader = Reader(file)

    trace_hypothesis, intermediate_hypothesis = gen_hypothesis(reader.get_inputs())
    traces = reader.get_traces()
    intermediates = reader.get_intermediates()

    title = "Dataset: " + file + "\nDataset Order: " + str(reader.get_d()) + "\nAnalysis Order: " + str(1)

    # analyse traces for sd 0.00
    traces_avereaged_xored_method = order_1_trace_compress_xor_avg(traces[0.00])
    plot_corr(title + "\nMethod: Average XORed weights" + "\nSD: 0.00 \nType: Intermediate Traces", trace_hypothesis.T, traces_avereaged_xored_method.T)

    # analyse traces for sd 0.00
    traces_prob_xored_method = order_1_trace_compress_xor_prob(traces[0.00])
    plot_corr(title + "\nMethod: Most probable XOR weights" + "\nSD: 0.00 \nType: Intermediate Traces", trace_hypothesis.T, traces_prob_xored_method.T)

    # analyse traces for sd 0.00
    traces_mean_method = traces_compress(2, traces[0.00])
    plot_corr(title + "\nMethod: Mean weights" + "\nSD: 0.00 \nType: Intermediate Tarces", trace_hypothesis.T, traces_mean_method.T)


#analyse("no_masks")
#analyse("with_masks_3")
analyse_different_methods_order_1("with_masks_1")
#analyse_order("with_masks_19")
#plot_order_d(0.40, False)
#plot_order_d(10.00, True)
# plot_order_d(0.00, False)
# plot_order_d(0.00, True)