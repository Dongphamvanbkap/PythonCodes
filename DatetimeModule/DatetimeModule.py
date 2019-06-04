import datetime
import random
# print(dir(datetime.date))
today = datetime.date.today()
print(today.strftime("%d-%m-%Y"))
print(today.year)
print(today.month)
print(today.day)
print(today.weekday())
print(today.isoweekday())
timedelta = datetime.timedelta(days = )
print((today + timedelta).strftime("%d-%m-%Y"))
my_birth_day = datetime.date(2020,3,2)
till_bday = my_birth_day - today
print(till_bday.days)
time = datetime.datetime.now()
print(time.date())