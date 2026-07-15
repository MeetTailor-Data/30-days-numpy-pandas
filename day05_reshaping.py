#15-07-26
#NumPy Reshaping

import numpy as np

arr = np.arange(1, 13)

# Problem 1 - Reshape to 3x4
reshaped = arr.reshape(3, 4)
print("3x4 Matrix:\n", reshaped)

# Problem 2 - Reshape to 2x6
print("2x6 Matrix:\n", arr.reshape(2, 6))

# Problem 3 - Flatten a matrix back to 1D
print("Flattened:", reshaped.flatten())

# Problem 4 - Transpose a matrix
print("Transposed:\n", reshaped.T)

# Problem 5 - Stack two arrays vertically
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Vertical Stack:\n", np.vstack([a, b]))
