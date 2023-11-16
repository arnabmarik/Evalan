# APP_ID = "cf8d6bff"
# API_KEY = "5367be6670adf7e70cdcaa4cee118239"
#
#
import requests
import json
#
# GENDER = "MALE"
# WEIGHT_KG = "60"
# HEIGHT = "160.5" #entered random height in cm
# AGE = "50"
#
#
# exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
#
# exercise_input ="I swam for minutes and then walked for 10 minutes" #input("Tell which exercise you did today?: ")
#
# header = {
#     "x-app-id": APP_ID,
#     'x-app-key': API_KEY
# }
#
# parameters = {
#     'query': exercise_input,
#     "gender": GENDER,
#     "weight_kg": WEIGHT_KG,
#     "height_cm": HEIGHT,
#     "age": AGE,
# }
#
# response = requests.post(url=exercise_endpoint, json=parameters, headers=header)
# response.raise_for_status()
# result = response.json()
# print(json.dumps(result, indent=4))


workout = {
    "workout":
                {
                    "date": "sdfsad",
                    "time": "sdasd",
                    "exercise": "swimming",
                    "duration": 50,
                    "calories": 150
                }
}

response = requests.post(url="https://api.sheety.co/42c41085ecf8f2ca7fe2509252fe1f9f/arnabWorkout/workouts", json=workout)

