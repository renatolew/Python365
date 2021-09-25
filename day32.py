# Write a Python program to check the validity of password input by users.
# Validation :
#
#     At least 1 letter between [a-z] and 1 letter between [A-Z].
#     At least 1 number between [0-9].
#     At least 1 character from [$#@].
#     Minimum length 6 characters.
#     Maximum length 16 characters.

import re

password_test = input("Input the password to be checked:\n")

cond = True

while cond:
    if (len(password_test)<6 or len(password_test)>12):
        break
    elif not re.search("[a-z]",password_test):
        break
    elif not re.search("[0-9]",password_test):
        break
    elif not re.search("[A-Z]",password_test):
        break
    elif not re.search("[$#@]",password_test):
        break
    elif re.search("\s",password_test):
        break
    else:
        print("Valid Password")
        cond = False
        break

if cond:
    print("Not a Valid Password")

