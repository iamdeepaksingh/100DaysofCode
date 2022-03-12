#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
# Author: Deepak Kumar Singh
# Description: Flight Search using Tequilla Kiwi and Sheety.
# Date Created: 06/02/2022
# Date Modified: 06/02/2022

import requests
from datetime import datetime
from datetime import timedelta
from data_manager import DataManager
from pprint import pprint
from notification_manager import NotificationManager


date_from = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
print(date_from)
date_to = (datetime.now() + timedelta(days=180)).strftime("%d/%m/%Y")
print(date_to)

# https://tequila.kiwi.com/portal/docs/tequila_api
# Search API https://tequila-api.kiwi.com/v2/search?fly_from=LGA&fly_to=MIA&dateFrom=01/04/2021&dateTo=02/04/2021



#response = requests.get(url=flight_search_endpoint, params=flight_search_params, headers=header_flight_search)
#data = response.json()
#print(data)

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
print("\n")
#print(sheet_data)

#print(sheet_data[0]["city"])
#print(sheet_data[0]["iataCode"])

for eachrow in sheet_data:
    if eachrow["iataCode"] == "":
        from flight_search import FlightSearch
        flight_search = FlightSearch()
        for row in sheet_data:
            row["iataCode"] = flight_search.get_destination_code(row["city"])
            #pprint(sheet_data)

        data_manager.destination_data = sheet_data
       #data_manager.update_destination_codes()

print(sheet_data)
for destination in sheet_data:
    flight = flight_search.search_flights("LON", destination["iataCode"], date_from, date_to)
    #print(f"Journey Start date: {flight.out_date}")
    #print(f"Return Date : {flight.return_date}")
    #print(destination["lowestPrice"])
    if flight is not None and float(flight.price) < destination["lowestPrice"]:
        notification_manager = NotificationManager()
        msg = f"Low price alert! Only €{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}",
        notification_manager.notify_by_sms(msg)
        print(f"sms should be sent for {flight.destination_city}")



