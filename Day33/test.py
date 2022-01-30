import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
response.raise_for_status()
print(response.json())
data = response.json()
latitude = data["iss_position"]["latitude"]
lomgitude = data["iss_position"]["longitude"]
print(latitude)
print(lomgitude)