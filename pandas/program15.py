import pandas as pd
class_data= {
    'name':["Sundar", "Pankaj", "Pankaj", "Sonu","Monu"],
    'roll':[1,5,6,7,8],
    'branch':["CSE", "ECE", "CSE", "CE", "EE"],
    'age':[19, 18,16,20,17]
}

new_data= pd.DataFrame(class_data)
print(new_data.drop_duplicates(['name']))