#09-08-26
#Final Mixed Challenge

import pandas as pd
import numpy as np

np.random.seed(99)
df = pd.DataFrame({
    'Employee': [f'E{i}' for i in range(1, 11)],
    'Department': np.random.choice(['HR', 'Tech', 'Sales'], 10),
    'Salary': np.random.randint(30000, 100000, 10),
    'Experience': np.random.randint(1, 15, 10)
})

# Problem 1 - Average salary by department
print(df.groupby('Department')['Salary'].mean())

# Problem 2 - Highest paid employee
print("Top Earner:", df.loc[df['Salary'].idxmax(), 'Employee'])

# Problem 3 - Employees with more than 5 years experience
print(df[df['Experience'] > 5])

# Problem 4 - Salary to experience ratio
df['Ratio'] = (df['Salary'] / df['Experience']).round(2)
print(df[['Employee', 'Ratio']])

# Problem 5 - Department with most employees
print("Largest Dept:", df['Department'].value_counts().idxmax())
