import requests
from pprint import pprint

SHEETY_ENDPOINT = "https://api.sheety.co/fc661f3ce0c5ec167d4515250345f798/flightDeals/prices"

new_data = {'prices': [{'city': 'Paris', 'iataCode': '', 'id': 2, 'lowestPrice': 200},
            {'city': 'Berlin', 'iataCode': '', 'id': 3, 'lowestPrice': 42},
            {'city': 'Tokyo', 'iataCode': '', 'id': 4, 'lowestPrice': 485},
            {'city': 'Sydney', 'iataCode': '', 'id': 5, 'lowestPrice': 551},
            {'city': 'Istanbul', 'iataCode': '', 'id': 6, 'lowestPrice': 95},
            {'city': 'Kuala Lumpur',
             'iataCode': '',
             'id': 7,
             'lowestPrice': 414},
            {'city': 'New York', 'iataCode': '', 'id': 8, 'lowestPrice': 500},
            {'city': 'San Francisco',
             'iataCode': '',
             'id': 9,
             'lowestPrice': 260},
            {'city': 'Cape Town',
             'iataCode': '',
             'id': 10,
             'lowestPrice': 378}]}

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        #response = requests.get(url=SHEETY_ENDPOINT, auth=("DeepakSingh", "DeepakSingh"))
        #data = response.json()
        data = new_data # Saved into dictionary in order to reduce SHETTY usage as it is limited to 200 per month.
        #pprint(data)
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            data1 = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"https://api.sheety.co/fc661f3ce0c5ec167d4515250345f798/flightDeals/prices/{city['id']}", json=data1, auth=("DeepakSingh", "DeepakSingh"))
            #print(response.text)
