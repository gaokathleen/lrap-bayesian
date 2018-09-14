import matplotlib.pyplot as plt
import math
import numpy as np
def gauss(x, mean, variance):
    deviation = math.sqrt(variance)
    return np.exp(-np.power(x - mean, 2) / (2 * np.power(deviation, 2)))

# points is a list of coordinate pairs. The coordinate pairs are tuples containing (mean, variance)
def plot(points):
    for mean, variance in points:
        plt.plot(gauss(np.linspace(mean - 3 * math.sqrt(variance), mean + 3 * math.sqrt(variance), 100), mean, variance))


plot([(-100, 4), (1000, 2), (6, 6)])
plt.show()

#import scipy.stats as stats
#stats.norm.pdf(x, mean, deviation)
