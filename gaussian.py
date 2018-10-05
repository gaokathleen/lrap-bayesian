import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.stats import norm

def gauss(x, mean, variance):
    deviation = math.sqrt(variance)
    return np.exp(-np.power(x - mean, 2) / (2 * np.power(deviation, 2)))

# points is a list of coordinate pairs. The coordinate pairs are tuples containing (mean, variance)
def plot_gauss(points):

    means = [mean[0] for mean in points]
    variances = [point[0] for point in points]
    deviation = math.sqrt(max(variances))

    max_y, min_y = means[0], means [0]
    for m in means:
<<<<<<< HEAD
        if m > max:
            max = m
        if min > m:
            min = m
    print(min)

    for mean, variance in points:
        deviation = math.sqrt(variance)
        plt.plot(norm.pdf(np.linspace(norm.ppf(0.05, min, deviation), norm.ppf(0.95, max, deviation), 1000), loc = mean, scale = deviation))
        #plt.plot(gauss(np.linspace(norm.ppf(0.05, min, deviation), norm.ppf(0.95, max, deviation), 1000), mean, deviation))
=======
        if m > max_y:
            max_y = m
        if min_y > m:
            min_y = m
>>>>>>> 215f463cbb0a2fcff40cdad89fd5e3a924219193

    min_x = norm.ppf(0.05, min_y, deviation)
    max_x = norm.ppf(0.95, max_y, deviation)
    x_points = np.linspace(min_x, max_x, 1000)

    for mean, variance in points:
        y_points = gauss(x_points, mean, variance)
        plt.plot(x_points, y_points)
    plt.show()

<<<<<<< HEAD
plot([(100, 4)])
plt.show()
=======
plot_gauss([(200, 20), (6, 20), (-100,10)])
>>>>>>> 215f463cbb0a2fcff40cdad89fd5e3a924219193

