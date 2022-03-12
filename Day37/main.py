

import requests
from datetime import  datetime
import os
USERNAME = "deepaksingh"
TOKEN = os.environ.get("PIXELA_TOKEN")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Reading graph",
    "unit": "pages",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)
today = datetime.now()
postpixel_endpoint = f"{graph_endpoint}/graph1"

postpixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5"
}

formatted_graph = today.strftime("%Y%m%d")

#response = requests.post(url=postpixel_endpoint, json=postpixel_config, headers=headers)
#print(response.text)

putpixel_endpoint = f"{graph_endpoint}/graph1/{formatted_graph}"

putpixel_config = {
     "quantity": "2"
}


#response = requests.put(url=putpixel_endpoint, json=putpixel_config, headers=headers)
#print(response.text)

delete_endpoint = f"{graph_endpoint}/graph1/{formatted_graph}"
response = requests.delete(url=putpixel_endpoint, json=putpixel_config, headers=headers)
print(response.text)