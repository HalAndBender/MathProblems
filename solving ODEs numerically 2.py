# First Order ODE:

# http://sam-dolan.staff.shef.ac.uk/mas212/notebooks/ODE_Example.html

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Define a function which calculates the derivative
def dy_dx(y, x):
    return x - y

xs = np.linspace(0,5,100)
y0 = 1.0  # the initial condition
ys = odeint(dy_dx, y0, xs)
ys = np.array(ys).flatten()

plt.rcParams.update({'font.size': 14})  # increase the font size
plt.xlabel("x")
plt.ylabel("y")
plt.plot(xs, ys)

#Compare the numerical solution with the analytical solution by showing both on the same plot
y_exact = xs - 1 + 2*np.exp(-xs)
y_difference = ys - y_exact
plt.plot(xs, ys, xs, y_exact, "+");

plt.show()