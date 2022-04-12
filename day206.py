# Subtract a week (7 days)  from a given date in Python

from datetime import datetime, timedelta

initial_date = datetime(2021, 5, 18)
print("Choosen date:")
print(initial_date)

subtracted_days = 7
res_date = initial_date - timedelta(days = subtracted_days)
print("New Date:")
print(res_date)