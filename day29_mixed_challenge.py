#08-08-26
#Mixed Challenge Problems

import pandas as pd
import numpy as np

np.random.seed(10)
df = pd.DataFrame({
    'Product': ['A','B','C','D','E'],
    'Price': np.random.randint(100, 1000, 5),
    'Quantity': np.random.randint(1, 50, 5)
})

# Problem 1 - Add revenue column
df['Revenue'] = df['Price'] * df['Quantity']
print(df)

# Problem 2 - Most revenue product
print("Top Product:", df.loc[df['Revenue'].idxmax(), 'Product'])

# Problem 3 - Products above average revenue
avg_rev = df['Revenue'].mean()
print(df[df['Revenue'] > avg_rev])

# Problem 4 - Price per unit normalized
df['Price_norm'] = (df['Price'] - df['Price'].min()) / (df['Price'].max() - df['Price'].min())
print(df)

# Problem 5 - Rank by revenue
df['Rank'] = df['Revenue'].rank(ascending=False).astype(int)
print(df[['Product', 'Revenue', 'Rank']])
