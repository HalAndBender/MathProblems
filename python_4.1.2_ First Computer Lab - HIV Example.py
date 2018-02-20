# first computer lab - HIV example

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Mon Feb 19 08:20:08 2018

@author: stephangoldberg
"""

import numpy as np
import matplotlib.pyplot as plt

# importing the data (2 columns)
hiv_data = np.loadtxt('HIVseries.csv', delimiter=',')

# slicing the data (separating the columns):
time_in_days = hiv_data[:, 0]
viral_load = hiv_data[:, 1]


# creating a mathematical model, which represents the data 

# Define parameters:
A = 160000
B = 13000
alpha = 0.5
beta = 2

# Defining the range of x-values
time_model = np.linspace (0,10,101)

# Defining the y-values
viral_load_model = A *np.exp(-alpha * time_model) + B * np.exp(-beta *time_model)


# plotting the actual data and the model:
plt.scatter(time_in_days, viral_load, label = "Actual Data")
plt.plot(time_model, viral_load_model, label = "Mathematical model")

ax = plt.gca()      # getting control of the axis

ax.set_xlabel("Time in days")
ax.set_ylabel ("Viral load", size=10)
ax.set_title( " Viral load development in blood", size=16, weight="bold")

plt.legend()        # showing the labels of the plotted curves
plt.tight_layout()  # ensures that labels of x- or y-axis are not cut off

plt.savefig("Viral load development in blood.pdf")


plt.show()

