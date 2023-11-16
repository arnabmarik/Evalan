import requests
import json
from datetime import datetime
parameters = {"lat": 23,
              "lng": 23,
              "formatted":0
              }

response = requests.get("https://api.sunrise-sunset.org/json?", params=parameters)
response.raise_for_status()

sunrise = response.json()['results']['sunrise']
sunset = response.json()['results']['sunset']

sunrise  = sunrise.split("T")[1].split(":")[0]
sunset = sunset.split("T")[1].split(":")[0]

print(sunrise,sunset)

print(datetime.now().hour)