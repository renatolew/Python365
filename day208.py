# Find the day of the week of a given date

from datetime import datetime

given_date = datetime(2021, 10, 19)

# as integer
print(given_date.today().weekday())

# as weekday
print(given_date.strftime('%A'))