#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 08:40:18 2018

@author: stephangoldberg
"""

import numpy as np
import matplotlib.pyplot as plt

# creating a mathematical model, which represents the data 

# Define parameters:
A = 1
tau = 1


# Defining the range of x-values
time = np.linspace (0,2,101)

# Defining two functions:
V = 1 - np.exp(-time/tau)
W = A * ( np.exp(-time/tau) - 1 + (time / tau))

# Plotting the graph
plt.plot(time, W, label=r"$W(t)= A (e^{-t/ \tau} -1 + \frac{t}{\tau}) $")  # ensure to include 'r' preceeding the quotations.

ax = plt.gca() # getting control of the axis



ax.set_xlabel('time ')               # Label x-axis
ax.set_ylabel('W(t)', size=10)       # Label y-axis
ax.set_title( " Bacterial Example", size=16, weight="bold")

# method 1 declaring the lines:
#lines[0].set_label("$W(t)= A(e^{-t/ \\tau} -1 + \frac{t}{\\tau}}} }$")

# method 2 labelling the data:

# plt.scatter(time_in_days, viral_load, label = "$V(t)=1-e^{-t/ \\tau}$")
# plt.plot(time_model, viral_load_model, label = "$W(t)=text$")




plt.legend()        # showing the labels of the plotted curves
plt.tight_layout()  # ensures that labels of x- or y-axis are not cut off

plt.savefig("Bacterial Example.pdf")


plt.show()