#https://sites.math.washington.edu/~wcasper/math307_win16/review/euler_method/euler_method.pdf
# Excercise 15, Book A, page 32

# importing external libriaries
import numpy as np
from matplotlib import pyplot as plt

# differential equation: dy/dx = f(x,y) = x**2 + y
# defining basic data:
x0 = -1                  # initial condition value of x
y0 = -0.2                  # initial condition value of y
xf = 2                 # maximum value of x (interval maximum)
n = 21                 # number of steps
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
    y[i] = deltax * (  (x[i])**2 +  y[i-1]  )  +   y[i-1]     # ( deltax * f(x,y) )  +  y

# printing the data
for i in range(n):
    print (x[i], y[i])

# plotting the solution
plt.plot (x,y,'o')
plt.xlabel("Value of x")
plt.ylabel("Value or y")
plt.title ("approximate solution with forward Euler's method")
plt.show()