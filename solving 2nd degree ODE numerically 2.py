# solving a 2nd degree ODE numerically


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def dU_dx(U, x):
    # Here U is a vector such that y=U[0] and z=U[1]. This function should return [y', z']
    return [U[1], -2*U[1] - 2*U[0] + np.cos(2*x)]
U0 = [0, 0]
xs = np.linspace(0, 10, 200)
Us = odeint(dU_dx, U0, xs) #odeint(function_which_returns_, list_of_initial_conditions, t, args=())
ys = Us[:,0]

plt.xlabel("x")
plt.ylabel("y")
plt.title("Damped harmonic oscillator")
plt.plot(xs,ys);

plt.show()