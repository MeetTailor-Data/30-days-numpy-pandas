#29-07-26
#Pandas Merge and Join

import pandas as pd

students = pd.DataFrame({'ID': [1, 2, 3, 4],
                         'Name': ['Meet', 'Raj', 'Priya', 'Ankit']})
marks = pd.DataFrame({'ID': [1, 2, 3, 5],
                      'Marks': [85, 78, 92, 88]})

# Problem 1 - Inner merge
print(pd.merge(students, marks, on='ID', how='inner'))

# Problem 2 - Left merge
print(pd.merge(students, marks, on='ID', how='left'))

# Problem 3 - Right merge
print(pd.merge(students, marks, on='ID', how='right'))

# Problem 4 - Outer merge
print(pd.merge(students, marks, on='ID', how='outer'))

# Problem 5 - Concat two dataframes
df1 = pd.DataFrame({'Name': ['Meet', 'Raj']})
df2 = pd.DataFrame({'Name': ['Priya', 'Ankit']})
print(pd.concat([df1, df2], ignore_index=True))
