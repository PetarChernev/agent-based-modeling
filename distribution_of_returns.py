from scipy.special import erf
import numpy as np
import matplotlib.pyplot as plt

sqrt_2 = np.sqrt(2)


def _cum_product(j):
    product = np.cumprod([-erf(-sqrt_2 * 0.8 ** k) for k in range(1, j)])
    if product.size > 0:
        return product[-1]
    else:
        return 1


def p_i_plus_c_lt_x(n, x):
    return sum((1 + erf(x / sqrt_2)) * (1 + erf(-sqrt_2 * 0.8 ** j)) * _cum_product(j)/2
               for j in range(1, n + 1))


cdf = []
start = -5
stop = 5
num = 50
dx = abs(stop - start) / num
x_space = np.linspace(start, stop, num)
for x in x_space:
    cdf.append(p_i_plus_c_lt_x(20, x))


plt.plot(x_space[:-1], np.diff(cdf) / dx)

plt.show()