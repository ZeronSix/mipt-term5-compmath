#!/usr/bin/python3
import math

# f(x) = exp(x)
# a = 0, b = 1


def f(x):
    return math.exp(x) - 1


def integral_antiderivative(a, b):
    return math.exp(b) - math.exp(a) + a - b


def integral_simpson(a, b, n):
    h = (b - a) / n
    x = a

    i = 0
    for _ in range(n):
        i += (f(x) + 4 * f(x + h / 2) + f(x + h))
        x += h
    i *= h / 6

    return i


FIRST = -math.sqrt(3 / 5)
SECOND = 0
THIRD = math.sqrt(3 / 5)


def substitute_gauss3(a, h, x):
    return a + (x + 1) * h / 2


def integral_gauss3(a, b, n):
    h = (b - a) / n
    x = a

    i = 0
    for _ in range(n):
        x1 = substitute_gauss3(x, h, FIRST)
        x2 = substitute_gauss3(x, h, SECOND)
        x3 = substitute_gauss3(x, h, THIRD)
        i += 5 / 9 * f(x1) + 8 / 9 * f(x2) + 5 / 9 * f(x3)
        x += h
    i *= h / 2

    return i



def main():
    print('f(x) = e^x - 1')
    args = [10, 20, 40, 80]
    for arg in args:
        int1 = integral_antiderivative(0, 1)
        int2 = integral_simpson(0, 1, arg)
        int3 = integral_gauss3(0, 1, arg)
        print('n = {}:'.format(arg))
        print(' Int1 = {}'.format(int1))
        print(' Int2 = {}'.format(int2))
        print(' Int3 = {}'.format(int3))
        print(' |Int1 - Int2| = {}'.format(abs(int1 - int2)))
        print(' |Int1 - Int3| = {}'.format(abs(int1 - int3)))


if __name__ == '__main__':
    main()
