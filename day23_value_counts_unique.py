#02-08-26
#Pandas Value Counts and Unique

import pandas as pd

data = {'City': ['Surat', 'Mumbai', 'Surat', 'Delhi', 'Mumbai', 'Surat'],
        'Grade': ['A', 'B', 'A', 'C', 'B', 'A']}
df = pd.DataFrame(data)

# Problem 1 - Value counts of city
print(df['City'].value_counts())

# Problem 2 - Unique cities
print("Unique Cities:", df['City'].unique())

# Problem 3 - Number of unique cities
print("Count:", df['City'].nunique())

# Problem 4 - Value counts as percentage
print(df['City'].value_counts(normalize=True) * 100)

# Problem 5 - Value counts of grade
print(df['Grade'].value_counts())
