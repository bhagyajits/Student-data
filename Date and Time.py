'''from datetime import date

# date object of today's date
today = date.today()

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)'''

from datetime import datetime

# Getting Datetime from timestamp
date_time = datetime.fromtimestamp(50)
print("Datetime from timestamp:", date_time)