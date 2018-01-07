# example from: https://sites.math.washington.edu/~wcasper/math307_win16/review/euler_method/euler_method.pdf

# importing external libriaries
import numpy as np
from matplotlib import pyplot as plt

# defining basic data
x0 = 0                  # initial condition value of x
y0 = 1                  # initial condition value of y
xf = 10                 # maximum value of x (interval maximum)
n = 101                 # number of steps
deltax = (xf-x0)/(n-1)  # step size

# defining x-values
x = np.linspace(x0, xf, n)

# initializing array for y-values
y = np.zeros ([n])

# for loop for Euler's method
# initial value problem ODE: dx/dx = -y + sin(x)
# initial condition: y(0)= 1
y[0] = y0
for i in range(1,n):
    y[i] = deltax * (-y[i-1] + np.sin(x[i])) + y[i-1]

# printing the data
for i in range(n):
    print (x[i], y[i])

# plotting the solution
plt.plot (x,y,'o')
plt.xlabel("Value of x")
plt.ylabel("Value or y")
plt.title ("approximate solution with forward Euler's method")
plt.show()