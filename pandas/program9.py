import pandas as pd
class_data= {
    'name':["Sundar", "Pankaj", "Ramu", "Sonu","Monu"],
    'roll':[1,5,6,7,8],
    'branch':["CSE", "ECE", "ME", "CE", "EE"],
    'age':[19, 18,18,20,17]
}

new_data= pd.DataFrame(class_data)

re_index= new_data.reindex(index=['a','b','c','d','e'])
print(re_index)