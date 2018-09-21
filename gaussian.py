import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.stats import norm

def gauss(x, mean, variance):
    deviation = math.sqrt(variance)
    return np.exp(-np.power(x - mean, 2) / (2 * np.power(deviation, 2)))

# points is a list of coordinate pairs. The coordinate pairs are tuples containing (mean, variance)
def plot(points):

    means = [mean[0] for mean in points]
    max, min = means[0], means [0]
    for m in means:
        if m > max:
            max = m
        if min > m:
            min = m
    for mean, variance in points:
        deviation = math.sqrt(variance)
        plt.plot(gauss(np.linspace(norm.ppf(0.05, min, variance), norm.ppf(0.95, max, variance), 1000), mean, variance))


plot([(-100, 4), (1000, 2), (6, 6)])
plt.show()

#import scipy.stats as stats
#stats.norm.pdf(x, mean, deviation)
