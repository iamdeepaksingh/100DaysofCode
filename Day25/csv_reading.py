# Author: Deepak Kumar Singh
# Description: Working with csv files
# Date Created: 15/01/2022
# Date Modified: 15/01/2022

import csv
with open("./weather_data.csv", "r") as f:
    data = f.readlines()

print(data)

with open("./weather_data.csv") as c:
    data2 = csv.reader(c)  # data2 is a csv reader object
    print(data2)
    temperature = []
    for row in data2:
        print(row)
        if row[1] != "temp":
            temperature.append(int(row[1]))
print(temperature)

# The above code is cumbersome, so pandas library is used.
