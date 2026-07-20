#19-07-26
#NumPy Broadcasting

import numpy as np

# Problem 1 - Add scalar to matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Add 10:\n", matrix + 10)

# Problem 2 - Add 1D array to each row
row = np.array([1, 0, -1])
print("Add row:\n", matrix + row)

# Problem 3 - Multiply each column by different value
col = np.array([[2], [3], [4]])
print("Multiply col:\n", matrix * col)

# Problem 4 - Normalize array between 0 and 1
arr = np.array([10, 20, 30, 40, 50])
normalized = (arr - arr.min()) / (arr.max() - arr.min())
print("Normalized:", normalized)

# Problem 5 - Subtract column mean from each column
print("Column mean subtracted:\n", matrix - matrix.mean(axis=0))
