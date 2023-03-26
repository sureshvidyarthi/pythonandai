import pandas as pd

# create a DataFrame with hierarchical index
data = {'Year': [2019, 2019, 2020, 2020],
        'Quarter': ['Q1', 'Q2', 'Q1', 'Q2'],
        'Sales': [100, 200, 300, 400]}
df = pd.DataFrame(data)
df = df.set_index(['Year', 'Quarter'])

# print the DataFrame
print(df)