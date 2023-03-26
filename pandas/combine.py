import pandas as pd
import pandas as pd

# creating two dataframes
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [4, 5, 6], 'B': [7, 8, 9]})

# concatenating vertically
df = pd.concat([df1, df2])
print(df)