#!/usr/bin/python3
import math
# from matplotlib import pyplot

L = 10
LAMBDA = 2.0
G = 9.8
B = 1.0
OMEGA = 1.0


def func(u, v, t):
    return (B * math.sin(OMEGA * t) - G * math.sin(u) - 2 * LAMBDA * v) / L


def euler_step(u, v, t, step):
    return u + step * v, v + step * func(u, v, t)


def runge_kutta_step(u, v, t, step):
    k1 = func(u, v, t)
    l1 = v
    k2 = func(u + step * l1 / 2, v + step * k1 / 2, t + step / 2)
    l2 = v + step * k1 / 2
    k3 = func(u + step * l2 / 2, v + step * k2 / 2, t + step / 2)
    l3 = v + step * k2 / 2
    k4 = func(u + step * l3, v + step * k3, t + step)
    l4 = v + step * k3

    return (u + step / 6 * (l1 + 2 * l2 + 2 * l3 + l4),
            v + step / 6 * (k1 + 2 * k2 + 2 * k3 + k4))


def main():
    period = 2 * math.pi * math.sqrt(L / G)
    step = period / 20
    t = 0.0
    u_ee = 1.0
    v_ee = 1.0
    u_rk = 1.0
    v_rk = 1.0
    n = 0

    ts = [0]
    u_ees = [u_ee]
    u_rks = [u_rk]

    print("t_{} = {}; u_ee = {}; u_rk = {}".format(n, t, u_ee, u_rk))
    while t <= period * 3:
        u_ee, v_ee = euler_step(u_ee, v_ee, t, step)
        u_rk, v_rk = runge_kutta_step(u_rk, v_rk, t, step)
        t += step
        n += 1

        ts.append(t)
        u_ees.append(u_ee)
        u_rks.append(u_rk)

        print("t_{} = {}; u_ee = {}; u_rk = {}".format(n, t, u_ee, u_rk))

    # pyplot.plot(ts, u_ees, 'bs', ts, u_rks, 'r--')
    # pyplot.legend(('Euler', 'Runge-Kutta'))
    # pyplot.show()


if __name__ == '__main__':
    main()
