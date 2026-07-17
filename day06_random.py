#16-07-26
#NumPy Random

import numpy as np

np.random.seed(42)

# Problem 1 - Generate 5 random numbers between 0 and 1
print("Random floats:", np.random.rand(5))

# Problem 2 - Generate 5 random integers between 1 and 100
print("Random ints:", np.random.randint(1, 100, 5))

# Problem 3 - Generate 3x3 random matrix
print("Random matrix:\n", np.random.rand(3, 3))

# Problem 4 - Pick random sample from array
arr = np.array([10, 20, 30, 40, 50])
print("Random sample:", np.random.choice(arr, 3))

# Problem 5 - Shuffle an array
np.random.shuffle(arr)
print("Shuffled:", arr)
