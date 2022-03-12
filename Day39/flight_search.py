import requests
from pprint import pprint
from flight_data import FlightData


TEQUILLA_API = "your TEQUILLA API"
header_flight_search = {
    "apikey": TEQUILLA_API
}

flight_search_endpoint = "https://tequila-api.kiwi.com/v2/search"
flight_location_search_endpoint = "https://tequila-api.kiwi.com/locations/query"


flight_details = {
    "Brussels": {"BRU", "800"},
    "Mumbai": {"BOM", "700"}
}

# https://tequila-api.kiwi.com/locations/query?term=CCU&locale=en-US&location_types=airport&limit=10&active_only=true

#https://tequila-api.kiwi.com/v2/search?fly_from=LGA&fly_to=MIA&dateFrom=01/04/2021&dateTo=02/04/2021

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, cityname):
        flight_search_params = {
            "term": cityname,
            "locale": "en-US",
            "location_types": "airport",
            "limit": "1",
            "active_only": "true"
       }
        response = requests.get(url=flight_location_search_endpoint, params=flight_search_params, headers=header_flight_search)
        #code = "Testing"
        code = response.json()["locations"][0]["code"]
        #print(response.text)
        #print("\n")
        #print(code)
        return code

    def search_flights(self, dep_from, dep_to, date_from, date_to):
        flight_search_params = {
            "fly_from": dep_from,
            "fly_to": dep_to,
            "dateFrom": date_from,
            "dateTo": date_to,
            "nights_in_dst_from": "7",
            "nights_in_dst_to": "28",
            "one_for_city": "1",
            "max_stopovers": "0",
            "curr": "EUR"
        }
        try:
            response = requests.get(url=flight_search_endpoint, params=flight_search_params, headers=header_flight_search)
            data2 = response.json()["data"][0]
            #pprint(data2)
        except IndexError:
            print(f"No flights found for {dep_to}")
            return None

        flight_data = FlightData(
            price = data2["price"],
            origin_city = data2["route"][0]["cityFrom"],
            origin_airport = data2["route"][0]["flyFrom"],
            destination_city = data2["route"][0]["cityTo"],
            destination_airport = data2["route"][0]["flyTo"],
            out_date = data2["route"][0]["local_departure"].split("T")[0],
            return_date = data2["route"][1]["local_departure"].split("T")[0]
        )

        print(f"{flight_data.destination_city}: €{flight_data.price}")
        #print(f"{flight_data.out_date} : {flight_data.return_date}")
        return flight_data






