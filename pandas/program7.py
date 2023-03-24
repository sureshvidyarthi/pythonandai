import pandas as pd
class_data= {
    'name':["Sundar", "Pankaj", "Ramu", "Sonu"],
    'roll':[1,5,6,7]
}

new_data= pd.DataFrame(class_data)

del new_data['roll']
print(new_data)
