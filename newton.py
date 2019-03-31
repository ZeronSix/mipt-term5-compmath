#!/usr/bin/python3
import sys
import numpy as np


def set_f(f, x):
    f[0] = 4 * x[0] - x[1] + x[2] - x[0] * x[3]
    f[1] = x[0] - 2 * x[1] + 3 * x[2] - x[2] * x[3]
    f[2] = -1 * x[0] + 3 * x[1] - 2 * x[2] - x[1] * x[3]

    f[3] = x[0] ** 2 + x[1] ** 2 + x[2] ** 2 - 1


def set_j(j, x):
    j[0, 0] = 4 - x[3]
    j[0, 1] = -1
    j[0, 2] = 1
    j[0, 3] = -x[0]

    j[1, 0] = 1
    j[1, 1] = -2
    j[1, 2] = 3 - x[3]
    j[1, 3] = -x[2]

    j[2, 0] = -1
    j[2, 1] = 3 - x[3]
    j[2, 2] = -2
    j[2, 3] = -x[1]

    j[3, 0] = 2 * x[0]
    j[3, 1] = 2 * x[1]
    j[3, 2] = 2 * x[2]
    j[3, 3] = 0


def main():
    x = np.array([0.1, 0.1, 0.1, 0.1])
    f = np.array([0.0, 0.0, 0.0, 0.0])
    j = np.empty((4, 4))
    set_f(f, x)
    set_j(j, x)

    i = 1
    while np.linalg.norm(f) > 1e-4:
        try:
            x = x - np.linalg.solve(j, f)
        except np.linalg.LinAlgError as e:
            print(e)
            print("Try different x0")
            break
        set_j(j, x)
        set_f(f, x)
        print('x{} ='.format(i), x)
        print('F{} ='.format(i), f, ' ||F{}|| ='.format(i), np.linalg.norm(f))

        i += 1

    print('\nResult: ', x)


if __name__ == '__main__':
    main()
