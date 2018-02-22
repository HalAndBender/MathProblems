#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 14:09:09 2018

Purpose: Assignment for MST201, TMA05, Question 4c

@author: stephangoldberg
"""

import numpy as np
import matplotlib.pyplot as plt




t_values = np.linspace(-3*np.pi, 3*np.pi, 100)

a = np.sin(t_values) + 2/np.pi*np.sin(t_values)
b = -np.sin(2*t_values)
c = (1/3 + 2/(3*np.pi))*np.sin(3*t_values)

d = a+b+c
plt.plot(t_values, d)


ax = plt.gca()

#ax.legend()

ax.set_xlabel('t ') # Labeling the x-axis
ax.set_ylabel('F(t) ')

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



ax.set_title( "F(t) for n=1,2,3", size=16)

plt.savefig('MST210_TMA05_q4c.png')



plt.show()

