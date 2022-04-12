import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "",
    "username": "",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_config = {
    "id": "graph1",
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": user_params["token"]
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

graph_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs"
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

today = datetime.now()

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "5.5",
}

add_pixel_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs/{graph_config['id']}"
response = requests.post(url=add_pixel_endpoint, json=pixel_params, headers=headers)
print(response.text)

pixel_mod = {
    "quantity": "8.4"
}

update_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs/{graph_config['id']}/{pixel_params['date']}"
response = requests.put(url=update_endpoint, json=pixel_mod, headers=headers)
print(response.text)

delete_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs/{graph_config['id']}/{pixel_params['date']}"
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)