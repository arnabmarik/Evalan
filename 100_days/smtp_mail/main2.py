##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas as pd
import datetime as dt

birthdays = pd.read_csv("birthdays.csv")
birthdays = birthdays.set_index(['name'])
birthdays = birthdays[:-1]
birthdays.loc['arnab'] = ['arnavmarik@gmail.com', 1962, 10, 22]
birthdays.loc['arnab2'] = ['arnav2marik@gmail.com', 1962, 12,22]



year = birthdays['year'].tolist()
month = birthdays['month'].tolist()
day = birthdays['day'].tolist()
names = birthdays.index.tolist()
print(names)

a = {key:value for (key,value) in birthdays.iterrows()}

print(a['arnab']['year'])


date = dt.datetime.now()

for i in range(len(year)):
    if date.month == month[i] and date.day == day[i]:
        with open("letter_3.txt") as file:
            contents = file.read()
            contents = contents.replace("[NAME]", names[i])
            file.close()
        with open("letter_3.txt", 'w') as file:
            file.write(contents)
            file.close()














