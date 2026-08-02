#30-07-26
#Pandas Pivot Table

import pandas as pd

data = {'Name': ['Meet', 'Meet', 'Raj', 'Raj', 'Priya', 'Priya'],
        'Subject': ['Math', 'Science', 'Math', 'Science', 'Math', 'Science'],
        'Marks': [85, 90, 78, 82, 92, 88]}
df = pd.DataFrame(data)

# Problem 1 - Basic pivot table
pivot = df.pivot_table(values='Marks', index='Name', columns='Subject')
print(pivot)

# Problem 2 - Pivot with mean aggregation
print(df.pivot_table(values='Marks', index='Name', aggfunc='mean'))

# Problem 3 - Pivot with sum
print(df.pivot_table(values='Marks', index='Name', aggfunc='sum'))

# Problem 4 - Crosstab
print(pd.crosstab(df['Name'], df['Subject']))

# Problem 5 - Add margins (totals)
print(df.pivot_table(values='Marks', index='Name', columns='Subject', margins=True))
