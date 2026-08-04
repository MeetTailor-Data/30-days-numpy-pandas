#01-08-26
#Pandas Duplicates and Cleaning

import pandas as pd

data = {'Name': ['Meet', 'Raj', 'Meet', 'Priya', 'Raj'],
        'Age': [21, 22, 21, 20, 22],
        'Marks': [85, 78, 85, 92, 78]}
df = pd.DataFrame(data)

# Problem 1 - Check duplicates
print("Duplicates:\n", df.duplicated())

# Problem 2 - Count duplicates
print("Total duplicates:", df.duplicated().sum())

# Problem 3 - Drop duplicates
print(df.drop_duplicates())

# Problem 4 - Drop duplicates based on one column
print(df.drop_duplicates(subset='Name'))

# Problem 5 - Reset index after dropping
cleaned = df.drop_duplicates().reset_index(drop=True)
print(cleaned)
