# child_swing.py
# Stephan Goldberg -- 2018 Jan 26

""""
Problem statement:
Children jumping or falling of a swing on a playground may be injured or injure bystanders.

Objective of this program:
Calculate the minimum diameter of a (soft) safe-zone around a swing on a playground

Assumptions:
- The child on the swing is modeled as a point mass
- The chain of the swing is modelled as a string
- Motion with constant g is considered and equations of classical Newtonian mechanics are used
- No air resistance
- No friction on hinge of swing


"""""
import numpy as np
import matplotlib.pyplot as plt

# Initializing variables.
mass = 80               # Mass of a heavy child [kg]
theta = np.pi/2         # Angle between swing rope and horizontal [rad]
initial_speed_x = 0.0   # Speed of child in x-direction [m/s]


# Initializing parameters.
g = 9.81                # Gravitational acceleration [m/s^2]
length_swing = 2        # Length of swing chain (from attachment to seat) [m]
height_seat = 0.5       # Height of swing seat above ground level [m]


theta = np.arctan (1/ np.sqrt( ))


R_max = 2 * np.sqrt(( length_swing - length_swing * np.cos (theta) *(2*length_swing - 2* length_swing* np.cos(theta)+height_seat)))

