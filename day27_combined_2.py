#06-08-26
#NumPy and Pandas Combined 2

import pandas as pd
import numpy as np

np.random.seed(1)
sales = np.random.randint(1000, 10000, 12)
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
df = pd.DataFrame({'Month': months, 'Sales': sales})

# Problem 1 - Total sales
print("Total:", np.sum(df['Sales']))

# Problem 2 - Month with highest sales
print("Best Month:", df.loc[df['Sales'].idxmax(), 'Month'])

# Problem 3 - Above average months
avg = np.mean(df['Sales'])
print(df[df['Sales'] > avg])

# Problem 4 - Cumulative sales
df['Cumulative'] = np.cumsum(df['Sales'])
print(df)

# Problem 5 - Percent contribution of each month
df['Percent'] = (df['Sales'] / df['Sales'].sum() * 100).round(2)
print(df[['Month', 'Percent']])
