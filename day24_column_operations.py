#03-08-26
#Pandas Column Operations

import pandas as pd

data = {'Name': ['Meet', 'Raj', 'Priya'],
        'Math': [85, 78, 92],
        'Science': [90, 82, 88],
        'English': [76, 85, 80]}
df = pd.DataFrame(data)

# Problem 1 - Add total column
df['Total'] = df['Math'] + df['Science'] + df['English']
print(df)

# Problem 2 - Add average column
df['Average'] = df['Total'] / 3
print(df)

# Problem 3 - Rename column
df = df.rename(columns={'English': 'Eng'})
print(df.columns.tolist())

# Problem 4 - Drop a column
df = df.drop(columns=['Total'])
print(df)

# Problem 5 - Reorder columns
df = df[['Name', 'Average', 'Math', 'Science', 'Eng']]
print(df)
