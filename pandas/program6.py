#value assign, membership
import pandas as pd
class_data= {
    'name':["Sundar", "Pankaj", "Ramu", "Sonu"],
    'roll':[1,5,6,7]
}
new_data= pd.DataFrame(class_data)
new_data.loc[1, 'roll']= 10

# print(new_data)
print('branch' in new_data)