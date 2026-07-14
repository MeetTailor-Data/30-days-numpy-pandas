#14-07-26
#NumPy Aggregation

import numpy as np

arr = np.array([4, 7, 2, 9, 1, 5, 8, 3, 6, 10])

# Problem 1 - Find sum
print("Sum:", np.sum(arr))

# Problem 2 - Find mean
print("Mean:", np.mean(arr))

# Problem 3 - Find min and max
print("Min:", np.min(arr), "Max:", np.max(arr))

# Problem 4 - Find standard deviation
print("Std Dev:", np.std(arr))

# Problem 5 - Find index of max and min value
print("Index of Max:", np.argmax(arr))
print("Index of Min:", np.argmin(arr))
