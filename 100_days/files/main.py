import pandas
import pandas as pd
import csv

# with open("file.txt", mode = "w") as file:
#     file.write("arnab")
#     file.close()
#
#
# with open("file.txt", mode = "a") as file:
#     file.write("arnab\n")
#     file.write("arnab")
#     file.close()


#
# with open("weather_data.csv") as file:
#
#     data =  file.readlines()
#     temperatures = []
#     for row in data[1:]:
#         for i in row:
#             if i == ",":
#                 temperatures.append(int(row[row.index(i) + 1 : row.index(i) + 3]))
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures =[]
#
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#
#     print(temperatures)


data = pd.read_csv("weather_data.csv")
# print(len(data['temp'].to_list()))
#
# data_dict = data.to_dict()
# print(data_dict)
#
# print(data['temp'].mean())

# print(data[data['day'] == 'Monday'])
#
# data_dict = {
#     "students":["amy", "james","Angela"],
#     "scores":[76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
#
# json = data.to_json('output.json', orient='records')


data =  pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

a = data["Primary Fur Color"].to_list()
data_dict = {
    "FurColor": ["Grey", "Black", "Cinnamon"],
    "count": [a.count("Grey"), a.count("Black"), a.count("Cinnamon")]
}
data = pd.DataFrame(data_dict).to_csv("data.csv")















