import numpy as np


#enter the matrix here:
A = np.array([[5, -3],[2, -2]])


w, v = np.linalg.eig(A)


print('For this matrix:')
print (A)
print ()
print('These are the eigenvalues:')
print(w) # these are the eigenvalues
print()
print('And these are the corresponding eigenvectors, respectively:')
print('in order to obtain integer numbers, divide the larger number by the smaller number in each vector')
print(v) # these are the eigenvectors corresponding to the eigenectors
print()
print()

