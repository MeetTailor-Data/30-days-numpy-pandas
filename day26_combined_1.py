#05-08-26
#NumPy and Pandas Combined 1

import pandas as pd
import numpy as np

np.random.seed(0)
df = pd.DataFrame({
    'Score': np.random.randint(40, 100, 10),
    'Hours': np.random.randint(1, 10, 10)
})

# Problem 1 - Numpy mean on pandas column
print("Mean Score:", np.mean(df['Score']))

# Problem 2 - Normalize Score column using numpy
df['Score_norm'] = (df['Score'] - np.min(df['Score'])) / (np.max(df['Score']) - np.min(df['Score']))
print(df)

# Problem 3 - Create new column using numpy where
df['Result'] = np.where(df['Score'] >= 60, 'Pass', 'Fail')
print(df)

# Problem 4 - Correlation using numpy
print("Correlation:", np.corrcoef(df['Score'], df['Hours'])[0][1])

# Problem 5 - Convert column to numpy array
arr = df['Score'].to_numpy()
print("As numpy array:", arr)
