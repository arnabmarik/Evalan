import smtplib
import datetime as dt
import random

# my_email = "arnavmarik@gmail.com"
# connection = smtplib.SMTP("smtp.gmail.com", 587)
# connection.starttls()
# connection.login(user=my_email, password="brgkvtlllugprbey" )
# connection.sendmail(from_addr=my_email, to_addrs="webcritic92@gmail.com", msg="Hello" )
# connection.close()


now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()



date_of_birth = dt.datetime(year=1995 , month=12 , day=15, hour=4)
print(date_of_birth.weekday())


with open("quotes.txt") as file:
    a= [line for line in file]
    all_quotes = file.readlines()
    print(all_quotes)
    my_email = "arnavmarik@gmail.com"
    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=my_email, password="brgkvtlllugprbey" )
    connection.sendmail(from_addr=my_email, to_addrs="webcritic92@gmail.com", msg=f"Subject:Monday Motivation\n{random.choice(a)}")
    connection.close()

















