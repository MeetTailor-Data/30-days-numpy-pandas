#23-07-26
#Pandas Filtering

import pandas as pd

data = {'Name': ['Meet', 'Raj', 'Priya', 'Ankit', 'Sara'],
        'Age': [21, 22, 20, 23, 21],
        'Marks': [85, 78, 92, 88, 74]}
df = pd.DataFrame(data)

# Problem 1 - Filter marks greater than 80
print(df[df['Marks'] > 80])

# Problem 2 - Filter age equal to 21
print(df[df['Age'] == 21])

# Problem 3 - Filter using multiple conditions
print(df[(df['Marks'] > 80) & (df['Age'] == 21)])

# Problem 4 - Filter using isin
print(df[df['Name'].isin(['Meet', 'Priya'])])

# Problem 5 - Filter using string contains
print(df[df['Name'].str.contains('a')])
