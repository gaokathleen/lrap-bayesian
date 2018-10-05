from scipy.stats import chi2
import matplotlib.pyplot as plt

def mean_n(mean_0, k_0, samples, sample_mean):
    return (k_0 / (k_0 + sample_mean)) * mean_0 + (samples.len() / (k_0 + samples.len())) * y

def k_n(k_0, samples, sample_mean):
    return k_0 + sample_mean

def v_n(v_0, samples, sample_mean):
    return v_0 + sample_mean

def sum_of_squares(mean_0, var_0, k_0, v_0, samples, sample_mean):
    return v_0 * var_0 + (samples.len() - 1) * s**2 + ((k_0 * samples.len()) / k_0 + samples.len()) * ((sample_mean - mean_0) ** 2)

def inv_chi_square(mean_0, var_0, samples, k_0, v_0):
    y = 0
    for elem in samples:
        y += elem
    y = y / samples.len()
    mean_n = mean_n(mean_0, k_0, samples, y)
    k_n = k_n(k_0, samples, y)
    v_n = v_n(v_0, samples, y)
    var_sum = sum_of_squares(mean_0, var_0, samples, k_0, v_0, y)
    return chi2.ppf(mean_n, var_sum / v_n) 
