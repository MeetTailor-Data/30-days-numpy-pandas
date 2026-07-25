#24-07-26
#Pandas Sorting and Ranking

import pandas as pd

data = {'Name': ['Meet', 'Raj', 'Priya', 'Ankit', 'Sara'],
        'Marks': [85, 78, 92, 88, 74],
        'Age': [21, 22, 20, 23, 21]}
df = pd.DataFrame(data)

# Problem 1 - Sort by marks descending
print(df.sort_values('Marks', ascending=False))

# Problem 2 - Sort by age ascending
print(df.sort_values('Age'))

# Problem 3 - Sort by multiple columns
print(df.sort_values(['Age', 'Marks'], ascending=[True, False]))

# Problem 4 - Rank marks
df['Rank'] = df['Marks'].rank(ascending=False).astype(int)
print(df[['Name', 'Marks', 'Rank']])

# Problem 5 - Get top 3 by marks
print(df.nlargest(3, 'Marks'))
