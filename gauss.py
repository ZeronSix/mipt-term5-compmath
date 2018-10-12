#!/usr/bin/python3
import sys
import numpy as np


def update_main_el(matrix, step, n, var_order):
    row_order = [x for x in range(n)]
    col_order = [x for x in range(n)]

    # Find max
    m = float("-inf")
    index = (-1, -1)

    for i in range(step, n):
        for j in range(step, n):
            if abs(matrix[i, j]) > m:
                m = abs(matrix[i, j])
                index = (i, j)

    var_order[step], var_order[index[1]] = var_order[index[1]], var_order[step]
    col_order[step], col_order[index[1]] = col_order[index[1]], col_order[step]
    row_order[step], row_order[index[0]] = row_order[index[0]], row_order[step]

    matrix = matrix[row_order]
    matrix = matrix[:, col_order + [n]]
    return matrix, var_order


def gauss(matrix, n):
    x = np.vstack(np.array([i for i in range(1, n + 1)]))
    b = np.vstack(matrix.dot(x))
    ext_matrix = np.append(matrix, b, axis=1)
    var_order = [x for x in range(n)]

    for i in range(n - 1):
        ext_matrix, var_order = update_main_el(ext_matrix, i, n, var_order)

        for j in range(i + 1, n):
            a = -ext_matrix[j, i] / ext_matrix[i, i]
            for k in range(i, n + 1):
                ext_matrix[j, k] += ext_matrix[i, k] * a

    answer = np.empty((n, 1))
    for i in reversed(range(0, n)):
        answer[i, 0] = ext_matrix[i, n]
        for j in range(i + 1, n):
            print(i, j)
            answer[i, 0] -= ext_matrix[i, j] * answer[j, 0]
        answer[i, 0] /= ext_matrix[i, i]

    index = 0
    ordered_answer = np.empty((n, 1))
    for var in var_order:
        ordered_answer[var] = answer[index]
        index += 1

    return np.linalg.norm(ordered_answer - x, np.inf)


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
        print(gauss(matrix, n))


if __name__ == '__main__':
    main()

