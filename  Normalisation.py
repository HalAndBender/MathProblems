# Find a unit vector, whose direction is perpendicular to the directions of both vectors a and c

import numpy as np
from sklearn import preprocessing
from fractions import Fraction


a = np.array([2,2,1])
b = np.array([4,4,-7])

# c is the cross product of a and b:
c = np.cross(a,b)

print (c)
# normalize the resultant vector c.
d = preprocessing.normalize(c)
#print (preprocessing.normalize(c))
print (d)

# Fraction(d).limit_denominator(1000)

