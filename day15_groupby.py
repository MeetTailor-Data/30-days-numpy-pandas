#25-07-26
#Pandas GroupBy

import pandas as pd

data = {'City': ['Surat', 'Mumbai', 'Surat', 'Mumbai', 'Surat'],
        'Sales': [5000, 8000, 6000, 7000, 5500],
        'Category': ['A', 'B', 'A', 'A', 'B']}
df = pd.DataFrame(data)

# Problem 1 - Total sales by city
print(df.groupby('City')['Sales'].sum())

# Problem 2 - Average sales by city
print(df.groupby('City')['Sales'].mean())

# Problem 3 - Count by city
print(df.groupby('City')['Sales'].count())

# Problem 4 - Group by multiple columns
print(df.groupby(['City', 'Category'])['Sales'].sum())

# Problem 5 - Agg multiple functions
print(df.groupby('City')['Sales'].agg(['sum', 'mean', 'max']))
