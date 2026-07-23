#22-07-26
#Pandas DataFrame Basics

import pandas as pd

data = {'Name': ['Meet', 'Raj', 'Priya', 'Ankit'],
        'Age': [21, 22, 20, 23],
        'Marks': [85, 78, 92, 88]}
df = pd.DataFrame(data)

# Problem 1 - Print first 2 rows
print(df.head(2))

# Problem 2 - Check shape
print("Shape:", df.shape)

# Problem 3 - Select one column
print("Names:\n", df['Name'])

# Problem 4 - Select multiple columns
print(df[['Name', 'Marks']])

# Problem 5 - Basic info
print(df.info())
