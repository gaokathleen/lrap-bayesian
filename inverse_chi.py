from scipy.stats import chi2
import matplotlib.pyplot as plt
import numpy as np

def mean_n(mean_0, k_0, samples, sample_mean):
    return (k_0 / (k_0 + sample_mean)) * mean_0 + (samples.len() / (k_0 + samples.len())) * y

def k_n(k_0, samples, sample_mean):
    return k_0 + sample_mean

def v_n(v_0, samples, sample_mean):
    return v_0 + sample_mean

def sum_of_squares(mean_0, var_0, k_0, v_0, samples, sample_mean):
    sum = 0
    for elem in samples:
        sum += (elem - sample_mean)**2
    sample_var = sum / (samples.len() - 1)
    return v_0 * var_0 + (samples.len() - 1) * sample_var + ((k_0 * samples.len()) / k_0 + samples.len()) * ((sample_mean - mean_0) ** 2)

def inv_chi_square(mean_0, var_0, samples, k_0, v_0):
    y = 0
    for elem in samples:
        y += elem
    y = y / samples.len()
    mean_n = mean_n(mean_0, k_0, samples, y)
    k_n = k_n(k_0, samples, y)
    v_n = v_n(v_0, samples, y)
    var_sum = sum_of_squares(mean_0, var_0, samples, k_0, v_0, y)
    return [mean, var_sum, k_n, v_n]

s = np.random.normal(4.5, 3.74, 1000)
plt.plot(s)
plt.show()

# def inv_chi_square2(list_of_data):
#     mean_0 = list_of_data[0]
#     var_0 = list_of_data[1]
#     samples = list_of_data[2]
#     k_0 = list_of_data[3]
#     v_0 = list_of_data[4]
#     y = 0
#     for elem in samples:
#         y += elem
#     y = y / samples.len()
#     mean_n = mean_n(mean_0, k_0, samples, y)
#     k_n = k_n(k_0, samples, y)
#     v_n = v_n(v_0, samples, y)
#     var_sum = sum_of_squares(mean_0, var_0, samples, k_0, v_0, y)
#     return [mean, var_sum, samples, k_n, v_n]
