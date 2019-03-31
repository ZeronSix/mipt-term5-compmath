#!/usr/bin/python3
import math
import numpy as np

L = 0
R = 1


def g(x):
    return -1


def dg(x):
    return 0


def p(x):
    return 1


def f(x):
    return 0#-3*np.cos(2 * x)#-3 * np.math.exp(2 * x)


def solve(l, r, n):
    h = (R - L) / n
    y = np.zeros(n+1)
    A = np.zeros(n+1)
    B = np.zeros(n+1)

    b = p(0) + g(0) * 2 / h**2
    c = -g(0) * 2 / h**2 
    d = f(0) + dg(0)*l - 2*g(0)*l / h 
    A[0] = -c / b
    B[0] = d / b

    for i in range(1, n):
        a = -g((i-0.5)*h) / h**2
        b = g((i-0.5)*h) / h**2 + g((i+0.5)*h) / h**2 + p(i*h)
        c = -g((i+0.5)*h) / h**2
        d = f(h*i)
        e = a*A[i-1] + b

        A[i] = -c / e
        B[i] = (d - a*B[i-1]) / e

    b = 1 + h**2 * p(h*n) / g(h*n)
    a = -1
    d = -r*(-h - h**2*dg(h*n) / g(h*n)) + h**2*f(h*n) / g(h*n)

    a = -g(1)*2 / h**2
    b = p(1) + g(1)*2 / h**2
    d = f(1) + dg(1)*r + 2*g(1)*r / h

    y[n] = (d - a*B[n-1]) / (b + a*A[n-1])
    for i in range(n-1, -1, -1):
        y[i] = A[i]*y[i+1] + B[i]

    return y

if __name__ == '__main__':
    print("equation: -y''+y=-3*e^(2x), y'(0)=2, y'(1)=2*e^2")
    print('exact solution: y=e^(2x)')
    n = 20
    y = solve(0, -1 * np.sin(1), n)#2, 2*np.math.exp(2), n)
    exact = np.cos(np.linspace(0, 1, n + 1))
    err = np.max(np.abs(y - exact))

    for i in range(n + 1):
        print('x={}; y_exact={}; y_approx={}'.format(i / n, exact[i], y[i]))

    print('\nerror: {}'.format(err))
