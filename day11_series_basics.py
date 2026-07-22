#21-07-26
#Pandas Series Basics

import pandas as pd

# Problem 1 - Create a Series
s = pd.Series([10, 20, 30, 40, 50])
print("Series:\n", s)

# Problem 2 - Create Series with custom index
s2 = pd.Series([85, 90, 78], index=['Math', 'Science', 'English'])
print("With Index:\n", s2)

# Problem 3 - Access element by label
print("Math score:", s2['Math'])

# Problem 4 - Basic stats
print("Mean:", s2.mean(), "Max:", s2.max())

# Problem 5 - Filter values greater than 80
print("Greater than 80:\n", s2[s2 > 80])
