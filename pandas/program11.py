import pandas as pd
class_data= {
    'name':["Sundar", "Pankaj", "Ramu", "Sonu","Monu"],
    'roll':[1,5,6,7,8],
    'branch':["CSE", "ECE", "ME", "CE", "EE"],
    'age':[19, 18,16,20,17]
}

new_data= pd.DataFrame(class_data)

new_sort= new_data.sort_values('branch')
print(new_sort)