#12-07-26
#NumPy Indexing and Slicing

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# Problem 1 - Get first 3 elements
print("First 3:", arr[:3])

# Problem 2 - Get last 3 elements
print("Last 3:", arr[-3:])

# Problem 3 - Get every alternate element
print("Alternate:", arr[::2])

# Problem 4 - Reverse the array
print("Reversed:", arr[::-1])

# Problem 5 - From a 3x3 matrix get second row
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print("Second Row:", matrix[1, :])
