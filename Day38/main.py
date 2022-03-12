# Author: Deepak Kumar Singh
# Description: Habit tracker app using Nutritionix API and Google spreadsheet.
# Date Created: 05/02/2022
# Date Modified: 05/02/2022

# Requests Authentication : https://docs.python-requests.org/en/master/user/authentication/#basic-authentication

import requests
from datetime import datetime
import os
from dotenv import load_dotenv

APP_ID = "f01db9f6"
API_KEY = "7e61a3cd30001c8ad820d4ab0337d30b"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

user_input = input("Tell me which exercises you did. ")

json_request = {
 "query": user_input,
 "gender": "male",
 "weight_kg": 72.5,
 "height_cm": 167.64,
 "age": 30
}

response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=json_request, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

print(sheet_inputs)
print("\n")
print(os.environ)

# No Authentication
#sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

# Basic Authentication
#sheet_response = requests.post(
#     sheet_endpoint,
#     json=sheet_inputs,
#     auth=(
#         YOUR USERNAME,
#     YOUR PASSWORD,
#     )
# )

# # Bearer Token Authentication
# bearer_headers = {
#     "Authorization": "Bearer YOUR_TOKEN"
# }
# sheet_response = requests.post(
#     sheet_endpoint,
#     json=sheet_inputs,
#     headers=bearer_headers
# )