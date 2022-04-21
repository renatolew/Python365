# Calculate number of days between two given dates

from datetime import datetime


date_1 = datetime(2021, 5, 12).date()
date_2 = datetime(2017, 10, 19).date()

delta = None

if date_1 > date_2:
    delta = date_1 - date_2
else:
    delta = date_2 - date_1

print("Difference is", delta.days, "days")