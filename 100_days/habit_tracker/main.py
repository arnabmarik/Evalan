import requests

pixela_endpoint = "https://pixe.la/v1/users"
token = "sadsadasdasdasdgdhfghgth"
username = "marik"


users_params= {
    "token": token,
    "username": username,
    "agreeTermsOfService":"yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=users_params)
# print(response.text)


graph_endpoint  = f"{pixela_endpoint}/{username}/graphs"

headers= {"X-USER-TOKEN": token}

graph_config = {
    "id"   : "graph1",
    "name" : "cycling graph",
    "unit" : "Km",
    "type" : "float",
    "color": "ajisai"
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{username}/graphs"