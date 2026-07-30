#28-07-26
#Pandas Apply and Map

import pandas as pd

data = {'Name': ['Meet', 'Raj', 'Priya', 'Ankit', 'Sara'],
        'Marks': [85, 78, 92, 88, 74]}
df = pd.DataFrame(data)

# Problem 1 - Add grade column using apply
def get_grade(mark):
    if mark >= 90: return 'A'
    elif mark >= 80: return 'B'
    else: return 'C'

df['Grade'] = df['Marks'].apply(get_grade)
print(df)

# Problem 2 - Add 5 bonus marks using apply
df['Bonus'] = df['Marks'].apply(lambda x: x + 5)
print(df)

# Problem 3 - Map grades to points
grade_points = {'A': 10, 'B': 8, 'C': 6}
df['Points'] = df['Grade'].map(grade_points)
print(df)
