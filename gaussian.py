import matplotlib.pyplot as plt
import math
import numpy as np
def gauss(x, mean, variance):
    deviation = math.sqrt(variance)
    return math.exp(-(x - mean) ** 2 / (2 * (deviation ** 2)))

# points is a list of coordinate pairs. The coordinate pairs are composed (mean, variance)
def plot(points):
    for mean, variance in points:
        plt.plot(gauss(np.linspace(-10, 10, 100), mean, variance))

plt.show()
