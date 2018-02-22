#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 14:38:45 2018
Open University, MST210, TMA05 Question 4 (a),
Sketching a perdiodic function
@author: stephangoldberg
"""

import numpy as np
import matplotlib.pyplot as plt

# define the period of f(t)
tau = 2*np.pi

# define the range of each periodic function (f_1 + f_2 + f_3):
for i in np.arange(-10,10,1):
    start_a = -np.pi + i * tau #start range of function f_1
    end_a = -0.5*np.pi + i * tau #end range of function f_1
    a = np.linspace(start_a, end_a, 50) # t-values of f_1
    f_1 = -0.5*np.pi*a**0 # y-values of f_3
    
    start_b = -0.5*np.pi +i * tau #start range of function f_2
    end_b = 0.5*np.pi +i * tau #end range of function f_2
    b = np.linspace(start_b, end_b, 50) # t-values of f_1
    f_2 = b-tau*i # y-values of f_2
    
    start_c = 0.5*np.pi +i * tau # start range of function f_3
    end_c = np.pi +i * tau #end range of function f_3
    c = np.linspace(start_c, end_c, 50) # t-values of f_1
    f_3 = 0.5*np.pi*c**0 # y-values of  f_3
    
    plt.plot(a,f_1,b,f_2,c,f_3)  #plotting f_1, f_2, f_3

# labeling the functions
ax = plt.gca()
lines = ax.get_lines()
lines[0].set_label(r"$-1/2 \ \pi$")
lines[1].set_label(r"$t$")
lines[2].set_label(r"$1/2\pi$")
ax.legend()

ax.set_xlabel('t ') # Labeling the x-axis

plt.xlim(-3*np.pi,3*np.pi) # Limiting the visible plot area on x-axis

# draw x and y axis and grid
plt.axhline(0, color='black')
plt.axvline(0, color='black')

arrow_length = 15 # In points

# X-axis arrow
ax.annotate('', xy=(0.97, 0), xycoords=('axes fraction', 'data'), 
            xytext=(arrow_length, 0), textcoords='offset points',
            arrowprops=dict(arrowstyle='<|-', fc='black'))

# Y-axis arrow
ax.annotate('', xy=(0, 0.96), xycoords=('data', 'axes fraction'), 
            xytext=(0, arrow_length), textcoords='offset points',
            arrowprops=dict(arrowstyle='<|-', fc='black'))

ax.grid() # plotting a background grid

ax.set_title( "The periodic function f(t)", size=16, weight="bold")

plt.savefig('MST210_TMA05_q4a.png')  #saving picture of plot

plt.show()

