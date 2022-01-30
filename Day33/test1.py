
import requests
import datetime as dt

parameters = {
    "lat":"40.2192",
    "lng": "66.9792",
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
print(response.json())
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise)
print(sunset)
print(dt.datetime.now())