#reference: https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.linalg.solve.html

#find solution of
# x-4*y+2*z=9
# 3*x-2*y+3*z=7
# 8*x-2*y+9*z=34

import numpy as np

#augmented matrix left side:
a = np.array([[1,-4,2], [3,-2,3],[8,-2,9]])
# augmented matrix right side:
b = np.array([9,7,34])

#solving:
x = np.linalg.solve(a, b)

#check that the solution is correct:
print(np.allclose(np.dot(a, x), b))

#show result:
print(x)

# x = -7.8
# y = 1.2
# z = 11