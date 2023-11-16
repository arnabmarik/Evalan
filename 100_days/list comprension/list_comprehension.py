import pandas as pd
import random

# numbers = [1,2,3,4]
# new_list = []
# new_list = [n+1 for n in numbers]
#
# print(new_list)
#
# print([2*n for n in numbers])
#
# names = ["alex", "beth", "caroline", "Dave", "Eleanor", "Freddie"]
#
# print([n for n in names if len(n) == 4])
#
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
#
# print([n**2 for n in numbers])
#
# print([n for n in numbers if n%2 == 0])
#
#
# list = input().split(',')
# print(list)
#

#
# with open("file1.txt", 'r') as file:
#     file1 = [n[0] for n in file]
#
# with open("file2.txt", 'r') as file:
#     file2 = [n[0] for n in file]
#
#
# common = [n for n in file1 if n in file2]
#
# dict = { "a": 1, 'b':2, 'c':3, 'd':4}
#
# new_dict = {key:value for (key,value) in dict.items() if value !=3}
#
# print(new_dict)

# names = ["alex", "beth", "caroline", "Dave", "Eleanor", "Freddie"]
#
# student_scores = {key: random.randint(50,200) for key in names}
#
#
# passed_students = {key: value for (key,value) in student_scores.items() if value>100}
#
# print(passed_students)

# sentence = "what is the airspeed velocity of the unladen swallow?"
#
# sentence =sentence.split(" ")
#
# print({value:len(value) for value in sentence})
#
# input = {'Monday': 28, 'Tuesday': 18, 'Wednesday': 17, 'Thursday': 27, 'Friday': 16, 'Saturday': 10, 'Sunday': 17}
#
# print({key: 9/5*value + 32 for (key, value) in input.items()})
#
#
# print(input.items())

import pandas as pd

student_dict = {"student": ["angela", "James", "Lily"],
                "score": [56,76,98]
                }

# for (key,value) in student_dict.items():
#     print(value)

# student_dict  = pd.DataFrame(student_dict)
#
# #Loop through rows of a dataframe
#
# for (index, rows) in student_dict.iterrows():
#     print(rows['score'])
#     print(rows.score)


data = pd.read_csv("nato_phonetic_alphabet.csv")

letter = data['letter'].tolist()
code = data["code"].tolist()


# data = data.to_dict()
# for (index,row) in data.iterrows()


# dict = {i:j for (i,j) in (letter, code)}

#
# dictt = {}
#
# for i in letter:
#     dictt[i] = code[letter.index(i)]
# print(dictt)

data = pd.read_csv("nato_phonetic_alphabet.csv")

# letter = data['letter'].tolist()
# code   = data["code"].tolist()
#
# dict   = {i: code[letter.index(i)] for i in letter}



dict={ row['letter']:row['code']  for (index, row) in data.iterrows()}


name = input("enter a Name:").upper()


characters = [char.upper() for char in name]
print([(dict[key]) for key in characters])








