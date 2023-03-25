import pandas as pd
# Create a DataFrame
class_data = {'section': ['A', 'B', 'A', 'B'],
                   'roll': [1, 2, 3, 4]}
new_data= pd.DataFrame(class_data)

# Group by the 'section' column and calculate the mean
grouped = new_data.groupby('section')
print(grouped.mean())