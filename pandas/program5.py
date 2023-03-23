#dataframe dec, selecting
import pandas as pd

class_data= {
    'name':["Sundar", "Pankaj", "Ramu", "Sonu"],
    'roll':[1,5,6,7]
}
class1= pd.DataFrame(class_data)
# print(class1)

print(class1.loc[1], class1.loc[0])
