®#The area of a triangle with sides defined by vectors a and b is (1/2) |a x b|

import numpy as np

a = np.array([3,1])
b = np.array([0,4])

c = np.cross(a,b)


d = 1/2 * np.linalg.norm(c)

print (d)