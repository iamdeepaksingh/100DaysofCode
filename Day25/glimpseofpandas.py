# Author: Deepak Kumar Singh
# Description: Working with csv files using pandas
# Date Created: 15/01/2022
# Date Modified: 15/01/2022

# Pandas references:
#  1. https://pandas.pydata.org/docs/
#  2. https://pandas.pydata.org/docs/reference/index.html
#  3. https://pandas.pydata.org/docs/user_guide/10min.html#min

# Pandas has 2 type of data structures, series(1 dimensional), dataframe(2 dimensional)
# Series are like columns
# Dataframe is like table

import pandas as pd
data = pd.read_csv("./weather_data.csv")
print(data)
print(type(data))
print(type(data['day']))
print(data.to_dict())
print(data['temp'])
temp_list = data['temp'].to_list()
print(temp_list)

print(f"Avg temperature is {sum(temp_list)/len(temp_list)}")

temp = data['temp'].to_list()
print(type(temp))
print(f"Average temperature is {sum(temp)/len(temp)}")

print(data['temp'].mean())
print(data['temp'].max())
print(data.temp.max())  # columns are converted into attributes by pandas

# Getting data of a row
print(data[data.day == "Monday"])

# Row of data where temp is max
print(data[data.temp == data.temp.max()])

val_f = (int(data[data.day == 'Monday'].temp) * 9/5) + 32

print(f"Monday's temperature in Fahrenheit is {val_f} ")

data_dict = {
    "ID": [1, 2, 3],
    "Name": ["Deepak", "Vinay", "Ramana"]
}

d = pd.DataFrame(data_dict)
d.to_csv("createdDate.csv")
