#13-07-26
#NumPy Math Operations

import numpy as np

a = np.array([10, 20, 30, 40, 50])

# Problem 1 - Add 5 to every element
print("Add 5:", a + 5)

# Problem 2 - Multiply every element by 2
print("Multiply 2:", a * 2)

# Problem 3 - Square every element
print("Squared:", a ** 2)

# Problem 4 - Square root of every element
print("Sqrt:", np.sqrt(a))

# Problem 5 - Element wise addition of two arrays
b = np.array([1, 2, 3, 4, 5])
print("Element-wise Add:", a + b)
