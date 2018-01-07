# The volume of a parallelepiped is the area of it's base times it's vertical height,
# or expressed in vectors: |(a) x (b)| * c

import numpy as np

a = np.array([3,1,0]) #base side a
b = np.array([2,4,0]) #base side b
c = np.array([2,0,4]) #height c

x = np.cross(a,b)
y = np.dot (x,c)
z = np.linalg.norm(y)

print (z)
