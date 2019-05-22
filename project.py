#!/usr/bin/python3
import numpy as np
from scipy.fftpack import dstn, idstn
import time
import sys


def f(i, j, step):
    x = i * step
    y = j * step
    return -(2 - np.pi ** 2 * (x - 1) * x) * np.sin(np.pi * y)
    #return 8 * np.pi ** 2 * np.sin(2 * np.pi * x) * np.sin(2 * np.pi * y)


def get_exact(i, j, step):
    x = i * step
    y = j * step
    #return np.sin(2 * np.pi * x) * np.sin(2 * np.pi * y)
    return x * (x - 1) * np.sin(np.pi * y)


def solve_poisson(n):
    step = 1 / n
    N = (n - 1) ** 2

    eigenvalues = np.zeros((n - 1, n - 1))
    g = np.zeros((n - 1, n - 1))
    for k in range(1, n):
        for m in range(1, n):
            eigenvalues[k - 1, m - 1] = 4 / (step**2) * \
                                ((np.sin(np.pi * k * step / 2))**2 + (np.sin(np.pi * m * step / 2)) ** 2)
            g[k - 1, m - 1] = f(k, m, step)

    return dstn(idstn(g, norm='ortho', type=1) / eigenvalues, norm='ortho', type=1)


def test(n):
    exact = np.empty((n - 1, n - 1))
    for k in range(1, n):
        for m in range(1, n):
            exact[k - 1, m - 1] = get_exact(k, m, 1 / n)

    sol = solve_poisson(n)
    return np.max(np.abs(exact - sol))


if __name__ == '__main__':
    n = int(sys.argv[1])
    start = time.time()
    error = test(n)
    end = time.time()
    print(n, error, end - start, sep='\t')
