# The area of a parallelogram with sides defined by vectors (a) and (b) is |(a)x(b)|
import numpy as np

a = np.array([3,1])
b = np.array([0,4])

c = np.cross(a,b)



d = np.linalg.norm(c)

print ( d)