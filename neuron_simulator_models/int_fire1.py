# Implementation of IntFire1 in pure python

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

V0 = 10.0  # mV
t = np.linspace(0, 20, 100)  # ms
t0 = [0.0]


def v_ode_model(V, t, tau):
    dvdt = -1 / tau * V * np.exp(-(t - t0[0]) / tau)
    t0[0] = t
    return dvdt


def v_plain_model(V, t, t_prev, tau):
    V = V * np.exp(-(t - t_prev) / tau)
    return V


def solve_v_ode(t, V0, tau):
    return odeint(v_ode_model, V0, t, args=(tau,))


def solve_v_plain(t, V0, tau):
    v_plain = [V0]
    for i, t_i in enumerate(t):
        if i < 1:
            continue
        V = v_plain_model(v_plain[i - 1], t[i], t[i - 1], tau)
        v_plain.append(V)
    return v_plain


plt.figure()

plt.plot(t, solve_v_ode(t, V0, 2.), 'r', label='ODE, tau=2')
plt.plot(t, solve_v_plain(t, V0, 2.), 'b', label='plain, tau=2')
plt.plot(t, solve_v_ode(t, V0, 10.), 'r.', label='ODE, tau=10')
plt.plot(t, solve_v_plain(t, V0, 10.), 'b.', label='plain, tau=10')
plt.legend()
plt.xlabel('time')
plt.ylabel('V')

plt.show()


def milestone_index(v_list, t):
    v0 = v_list[0]
    for i, v_i in enumerate(v_list):
        if (0.37 - v_i / v0) <= 0.01:
            print('i=', i, ' t[i]=', t[i], ' v_i=', v_i)


milestone_index(solve_v_plain(t, V0, 2.), t)
milestone_index(solve_v_plain(t, V0, 10.), t)