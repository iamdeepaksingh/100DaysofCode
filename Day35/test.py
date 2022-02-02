# Author: Deepak Kumar Singh
# Description: OpenWeathermap API calls with Python.
# Date Created: 31/01/2022
# Date Modified: 31/01/2022


import requests
import pandas as pd
import os
import json

api_key = os.environ.get("openweathermap_API_KEY")
print(api_key)
parameter ={
    "lat": 50.736660,
    "lon": 4.237160,
    "appid": api_key,
    "exclude": "current,minutely,daily,alerts"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameter)
response.raise_for_status()
weather_data = response.json()
#print(type(weather_data))
#print(weather_data)
df = pd.DataFrame.from_dict(weather_data, orient="index")
df.transpose()
#print(df)

#print(weather_data["hourly"][0:16]["weather"])

#rain = [id for (x,y) in weather_data["hourly"][0:16]["id"] if id > 700 ]

weather_id = []
for i in range(1, 12):
    weather_id.append(weather_data["hourly"][i]["weather"][0]["id"])
x = ""
for i in weather_id:
    if int(i) < 700:
        x = "rain"

if x == "rain":
    print("rain")





