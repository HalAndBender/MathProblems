"""
Created: %(date)s
Author: %(username)s (Python 3.4)

Created: 2018
Author: Stephan Goldberg

Description:
Random walk with step_size number of steps in x- and y-direction with the numpy random-function.

"""
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import random as rng


num_steps  = 10000


x_step = rng((num_steps,))              # array with num_steps elements between 0 and 1
y_step = rng((num_steps,))


x_step[x_step >= 0.5] = 1              # assigning the value 1 for numbers between 0.5 and 1
x_step[x_step < 0.5] = -1              # assigning the value -1 for numbers between 0 and 0.5

y_step[y_step >= 0.5] = 1
y_step[y_step < 0.5] = -1

plt.plot(np.cumsum(x_step) ,np.cumsum(y_step))

ax = plt.gca()
ax.set_title( str(num_steps) + " random steps in x- and y-direction ", size=16)

plt.show()




