import requests
import json

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.json())
# response.raise_for_status()
