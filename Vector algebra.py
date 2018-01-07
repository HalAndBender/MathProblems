import numpy as np
import math

#Two vectors
x = np.array([-3, 2, 1])
y = np.array([0, 1, -1])
print ('vector x:', x)
print ('vector y:', y)
print('')

# The sum of two vectors:
print('The sum:')
print(x+y)
print(' ')

#The cross product of the two vectors:
print ('The cross product:')
print (np.cross(x, y))
print(' ')

#The magnitude of a vector:
print('The magnitude of x:')
print(np.linalg.norm(x))
print('')

# Dot product of x and y:
print('the dot product of x and y:')
print(np.dot(x,y))
print('')

#angle between two vectors with math package (in radians)
def dotproduct(v1, v2):
  return sum((a*b) for a, b in zip(v1, v2))

def magnitude(v):
  return math.sqrt(dotproduct(v, v))

def angle(v1, v2):
  return math.acos(dotproduct(v1, v2) / (magnitude(v1) * magnitude(v2)))
print (' The angle between in radians')
print(angle(x,y))
print('')


#angle between two vectors with numpy package (in radians):
def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'::"""
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))
print (' The angle between in radians')
print(angle_between(x,y))
print('')

#angle in degrees
print('The angle between in degrees')
print(180/np.pi*(angle_between(x,y)))
print('')