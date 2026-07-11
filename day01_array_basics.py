#11-07-26
#NumPy Array Basics

import numpy as np

# Problem 1 - Create a 1D array of numbers 1 to 10
arr = np.arange(1, 11)
print("1D Array:", arr)

# Problem 2 - Create a 3x3 matrix of zeros
zeros = np.zeros((3, 3))
print("Zeros Matrix:\n", zeros)

# Problem 3 - Create a 3x3 identity matrix
identity = np.eye(3)
print("Identity Matrix:\n", identity)

# Problem 4 - Create array of 5 evenly spaced numbers between 0 and 1
spaced = np.linspace(0, 1, 5)
print("Evenly Spaced:", spaced)

# Problem 5 - Check shape and datatype of an array
arr2 = np.array([1.5, 2.5, 3.5])
print("Shape:", arr2.shape, "Dtype:", arr2.dtype)
