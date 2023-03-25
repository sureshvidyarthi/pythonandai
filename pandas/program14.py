import pandas as pd

class_data= {
    'name':["Sundar", "Pankaj", "Ramu", "Sonu","Monu"],
    'roll':[1,5,None,7,None],
    'branch':["CSE", "ECE",None, "CE", "EE"],
    'age':[19, 18,16,20,17]
}

new_data= pd.DataFrame(class_data)

#missing data
# print(new_data.isna())

#fill data
print(new_data.fillna(0))
