#20-07-26
#NumPy Mixed Practice

import numpy as np

# Problem 1 - Create array and find cumulative sum
arr = np.array([1, 2, 3, 4, 5])
print("Cumulative Sum:", np.cumsum(arr))

# Problem 2 - Find unique values in array
arr2 = np.array([1, 2, 2, 3, 3, 3, 4])
print("Unique:", np.unique(arr2))

# Problem 3 - Sort array in descending order
arr3 = np.array([40, 10, 30, 20, 50])
print("Descending:", np.sort(arr3)[::-1])

# Problem 4 - Clip values between 20 and 40
arr4 = np.array([10, 20, 30, 40, 50])
print("Clipped:", np.clip(arr4, 20, 40))

# Problem 5 - Check where values are greater than 30
print("Where > 30:", np.where(arr4 > 30, "High", "Low"))
