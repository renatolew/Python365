# Write a Python program to convert a date of yyyy-mm-dd format to dd-mm-yyyy format.

import re


def change_date_format(orig_date):
        return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', orig_date)

original_date = "2021-10-08"

print("Original date in YYYY-MM-DD Format: ",original_date)

print("New date in DD-MM-YYYY Format: ",change_date_format(original_date))