#18-07-26
#NumPy Linear Algebra

import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Problem 1 - Matrix multiplication
print("Matrix Multiply:\n", np.dot(a, b))

# Problem 2 - Determinant of a matrix
print("Determinant:", np.linalg.det(a))

# Problem 3 - Inverse of a matrix
print("Inverse:\n", np.linalg.inv(a))

# Problem 4 - Eigenvalues
eigenvalues, _ = np.linalg.eig(a)
print("Eigenvalues:", eigenvalues)

# Problem 5 - Transpose
print("Transpose:\n", a.T)
