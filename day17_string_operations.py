#27-07-26
#Pandas String Operations

import pandas as pd

data = {'Name': ['meet tailor', 'raj shah', 'priya patel', 'ankit joshi'],
        'Email': ['meet@gmail.com', 'raj@yahoo.com', 'priya@gmail.com', 'ankit@outlook.com']}
df = pd.DataFrame(data)

# Problem 1 - Convert names to uppercase
print(df['Name'].str.upper())

# Problem 2 - Capitalize each word
print(df['Name'].str.title())

# Problem 3 - Extract first name only
print(df['Name'].str.split().str[0])

# Problem 4 - Check who uses gmail
print(df[df['Email'].str.contains('gmail')])

# Problem 5 - Get length of each name
print(df['Name'].str.len())
