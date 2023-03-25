import pandas as pd
class_data= {
    'name':["Sundar", "Pankaj", "Ramu", "Sonu"]   
}
new_data= pd.DataFrame(class_data)

print(new_data['name'].str.upper())