# Calculate the date 4 months from the current date

from datetime import datetime
from dateutil.relativedelta import relativedelta

current_date = datetime(2021, 10, 15).date()

months_to_add = 4
new_date = current_date + relativedelta(months =+ months_to_add)
print(new_date)