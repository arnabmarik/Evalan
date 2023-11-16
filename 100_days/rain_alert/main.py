# api_key = "fb8cde3b17fe019bf3b5b664f346138e"
import os

a = os.environ.get("api_key")
print(a)

import requests
import json
from datetime import datetime
# parameters = {"lat": 23,
#               "lon": 23,
#               "appid":api_key,
#               "exclude": "current, minutely, daily"
#               }

# response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)

# response.raise_for_status()
# sunrise = response.json()['results']
# sunset = response.json()['results']['sunset']
#
# sunrise  = sunrise.split("T")[1].split(":")[0]
# sunset = sunset.split("T")[1].split(":")[0]


# print(response.json())