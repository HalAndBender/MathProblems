#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 17:16:45 2018

@author: stephangoldberg

From the book: A students guide to Python for physical modeling

"""

import numpy as np
import matplotlib.pyplot as plt

# creating a mathematical model, which represents the data 



# Defining the range of x-values
time = np.linspace (0,2,101)


# Define parameters:

A = 10
tau = 1
W0 = A * ( np.exp(-time/tau) - 1 + (time / tau))   
plt.plot(time, W0, label='W0') 
plt.text(0.6, 4, 'A='+str(A)+', tau='+str(tau))
    
A = 1
tau = 10
W1 = A * ( np.exp(-time/tau) - 1 + (time / tau))   
plt.plot(time, W1, label = 'W1') 
plt.text(1.25, 0.4, 'A='+str(A)+', tau='+str(tau))

A = 5
tau = 1
W1 = A * ( np.exp(-time/tau) - 1 + (time / tau))   
plt.plot(time, W1, label = 'W2') 
plt.text(1.75, 4, 'A='+str(A)+', tau='+str(tau))



# Defining two functions:
V = 1 - np.exp(-time/tau)


# Plotting the graph
#plt.plot(time, W, label=r"$W(t)= A (e^{-t/ \tau} -1 + \frac{t}{\tau}) $")

ax = plt.gca() # getting control of the axis



ax.set_xlabel('time ')               # Label x-axis
ax.set_ylabel(r"$W(t)= A (e^{-t/ \tau} -1 + \frac{t}{\tau}) $", size=10)       # Label y-axis
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