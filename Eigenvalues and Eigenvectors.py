import numpy as np

w, v = np.linalg.eig(np.array([[-3.65, 4.16, 14.56, 3.64],[-0.34, 2.79, 11.62, 0.68],
       [-0.20, -0.80, -3.33, 0.40], [-1.82, 4.16, 14.56, 1.81]]))

print(w) # these are the eigenvalues
print()
print(v) # these are the eigenvectors corresponding to the eigenectors



