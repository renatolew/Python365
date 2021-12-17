# Write a Pandas program to calculate all Thursdays between two given days. 

import pandas as pd


thursdays  = pd.date_range('2021-10-01', 
                           '2021-12-31', freq="W-THU")


print("All Thursdays between 2021-10-01 and 2021-12-31:\n")
print(thursdays.values)