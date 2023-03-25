import pandas as pd

# Create two DataFrames
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [2, 3, 4], 'C': [7, 8, 9]})

# Merge the two DataFrames on column A
df3 = pd.merge(df1, df2, on='A')
print(df3)