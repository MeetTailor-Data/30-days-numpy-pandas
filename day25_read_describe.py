#04-08-26
#Pandas Read and Describe

import pandas as pd
import numpy as np

# Simulating a dataset without needing a CSV file
np.random.seed(42)
df = pd.DataFrame({
    'Age': np.random.randint(18, 60, 100),
    'Salary': np.random.randint(20000, 100000, 100),
    'Experience': np.random.randint(0, 20, 100)
})

# Problem 1 - Shape
print("Shape:", df.shape)

# Problem 2 - Describe
print(df.describe())

# Problem 3 - Column wise mean
print(df.mean())

# Problem 4 - Correlation
print(df.corr())

# Problem 5 - Check null values
print(df.isnull().sum())
