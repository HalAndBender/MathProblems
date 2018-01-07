#https://sites.math.washington.edu/~wcasper/math307_win16/review/euler_method/euler_method.pdf
# Excercise 15, Book A, page 32

# importing external libriaries
import numpy as np
from matplotlib import pyplot as plt
from math import e

# differential equation: dy/dx = f(x,y) = e**x + y
# defining basic data:
x0 = 0                       # initial condition value of x
y0 = 1                       # initial condition value of y
xf = 1                       # maximum value of x (interval maximum)
n = 101                      # number of steps
deltax = (xf-x0)/(n-1)       # step size h (step size ~ accuracy)



# defining x-values
x = np.linspace(x0, xf, n)

# initializing array for y-values
y = np.zeros ([n])

#adding a comparision function for comparison
z = (x+1) * (e**x)

# for loop for Euler's method
# initial value problem ODE: dx/dx = -y + sin(x)
# initial condition: y(0)= 1
y[0] = y0
for i in range(1,n):
    y[i] = y[i-1] + deltax * ( ( e**(x[i])) +  y[i-1]  )         #  y + (h * f(x,y))

# printing the data
for i in range(n):
    print (x[i], y[i])
print (y[100])
# plotting the solution
plt.plot (x,y,'o')  #plotting the differential equation with circles, solved with Euler's method
plt.plot (x,z)      #plotting the comparision function
plt.xlabel("Value of x")
plt.ylabel("Value or y")
plt.title ("approximate solution with forward Euler's method")
plt.show()