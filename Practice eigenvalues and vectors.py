import numpy as np

w, v = np.linalg.eig(np.array([[4, 0, 0],[-2, -4, 2],
       [1, -3, 3]]))

print(w) # these are the eigenvalues
print()
print(v) # these are the eigenvectors corresponding to the eigenectors