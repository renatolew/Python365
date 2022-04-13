# Print a date in a the following format:
# Day_name  Day_number  Month_name  Year


from datetime import datetime

ex_date = datetime(2022, 3, 15)

print("Example date is: ")
print(ex_date.strftime('%A %d %B %Y'))