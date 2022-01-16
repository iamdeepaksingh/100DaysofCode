# Author: Deepak Kumar Singh
# Description: Working with csv files using pandas
# Date Created: 15/01/2022
# Date Modified: 15/01/2022

import pandas as pd
data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
print(data.columns)


print(data['Primary Fur Color'].value_counts())
count_file = data['Primary Fur Color'].value_counts()
count_file.to_csv("Squirrel_counts.csv")