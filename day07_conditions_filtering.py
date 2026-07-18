#17-07-26
#NumPy Conditions and Filtering

import numpy as np

arr = np.array([5, 15, 25, 35, 45, 55, 65, 75, 85, 95])

# Problem 1 - Get all elements greater than 50
print("Greater than 50:", arr[arr > 50])

# Problem 2 - Get all even numbers
arr2 = np.arange(1, 21)
print("Even numbers:", arr2[arr2 % 2 == 0])

# Problem 3 - Replace all values less than 30 with 0
arr3 = arr.copy()
arr3[arr3 < 30] = 0
print("Less than 30 replaced:", arr3)

# Problem 4 - Count elements greater than 50
print("Count > 50:", np.sum(arr > 50))

# Problem 5 - Check if any element equals 45
print("Any == 45:", np.any(arr == 45))
