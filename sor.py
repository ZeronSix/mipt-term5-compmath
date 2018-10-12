#!/usr/bin/python3
import sys
import numpy as np

W = 1.5
EPS = 1E-4


def check_convergence(matrix, x, b, k):
    n = matrix.shape[0]
    residual = np.zeros(n)

    for i in range(n):
        residual[i] = b[i]
        for j in range(n):
            residual[i] -= matrix[i, j] * x[j]

    l = np.linalg.norm(residual)
    print('k={}'.format(k), l)
    return l < EPS


def sor(matrix):
    n = matrix.shape[0]
    matrix = matrix.transpose().dot(matrix)
    x = np.zeros(n)
    b = np.zeros(n)
    for i in range(n):
        for j in range(n):
            b[i] += matrix[i, j] * (j + 1)

    k = 0
    while not check_convergence(matrix, x, b, k):
        for i in range(n):
            s = b[i]
            for j in range(n):
                if i == j:
                    continue
                s -= matrix[i, j] * x[j]
            x[i] = (1 - W) * x[i] + W / matrix[i, i] * s
        k += 1

    return x


def main():
    if len(sys.argv) != 2:
        print('Wrong arguments!')
        return

    filename = sys.argv[1]
    with open(filename) as f:
        n = int(f.readline())
        matrix = np.empty((n, n))

        i = 0
        for line in f:
            j = 0
            for a in [s for s in line.rstrip('\n').split(' ') if s]:
                matrix[i, j] = float(a)
                j += 1
            i += 1
        print('Solution: ', sor(matrix))


if __name__ == '__main__':
    main()
