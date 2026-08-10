#07-08-26
#NumPy and Pandas Combined 3

import pandas as pd
import numpy as np

np.random.seed(5)
df = pd.DataFrame({
    'Student': [f'S{i}' for i in range(1, 11)],
    'Math': np.random.randint(50, 100, 10),
    'Science': np.random.randint(50, 100, 10),
    'English': np.random.randint(50, 100, 10)
})

# Problem 1 - Row wise average using numpy
df['Average'] = np.mean(df[['Math','Science','English']].values, axis=1)
print(df)

# Problem 2 - Student with highest average
print("Top Student:", df.loc[df['Average'].idxmax(), 'Student'])

# Problem 3 - Subject with highest mean
subjects = ['Math', 'Science', 'English']
print("Best Subject:", subjects[np.argmax([df[s].mean() for s in subjects])])

# Problem 4 - Count students above 75 average
print("Above 75:", np.sum(df['Average'] > 75))

# Problem 5 - Standard deviation of each subject
print(df[subjects].std())
