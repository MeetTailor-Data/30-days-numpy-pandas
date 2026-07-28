#26-07-26
#Pandas Missing Values

import pandas as pd
import numpy as np

data = {'Name': ['Meet', 'Raj', None, 'Ankit', 'Sara'],
        'Age': [21, np.nan, 20, 23, np.nan],
        'Marks': [85, 78, 92, np.nan, 74]}
df = pd.DataFrame(data)

# Problem 1 - Check missing values
print(df.isnull().sum())

# Problem 2 - Drop rows with any missing value
print(df.dropna())

# Problem 3 - Fill missing age with mean
df['Age'] = df['Age'].fillna(df['Age'].mean())
print(df)

# Problem 4 - Fill missing marks with median
df['Marks'] = df['Marks'].fillna(df['Marks'].median())
print(df)

# Problem 5 - Fill missing name with unknown
df['Name'] = df['Name'].fillna('Unknown')
print(df)
