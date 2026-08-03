#31-07-26
#Pandas DateTime

import pandas as pd

data = {'Date': ['2024-01-15', '2024-03-22', '2024-07-10', '2024-11-05'],
        'Sales': [5000, 7000, 6000, 8000]}
df = pd.DataFrame(data)

# Problem 1 - Convert to datetime
df['Date'] = pd.to_datetime(df['Date'])
print(df.dtypes)

# Problem 2 - Extract month
df['Month'] = df['Date'].dt.month
print(df)

# Problem 3 - Extract day name
df['Day'] = df['Date'].dt.day_name()
print(df)

# Problem 4 - Filter dates after June
print(df[df['Date'] > '2024-06-01'])

# Problem 5 - Sort by date
print(df.sort_values('Date'))
