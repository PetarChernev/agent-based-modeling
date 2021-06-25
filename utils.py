import numpy as np
import timeit


def equally_spaced_points(n, scale=1):
    if n % 2:
        return scale * np.arange(-n//2 + 1, n//2 + 1)
    else:
        return scale * (np.arange(-n//2 + 0.5, n//2 + 0.5))


if __name__ == '__main__':
    # timer1 = timeit.Timer("equally_spaced_points(10000, 123.312)", "from __main__ import equally_spaced_points")
    # print(timer1.timeit(1000))

    print(equally_spaced_points(122, 1))