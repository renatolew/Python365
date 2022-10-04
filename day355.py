# Implement the same exercise as Exercise 1 (Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old), except don’t explicitly write out the year.
# Use the built-in Python datetime library to make the code you write work during every year, not just the one we are currently in.


import datetime

current_year = datetime.datetime.now().year


name = input("What is your name? ")
age = int(input("How old are you? "))
print(f"{name}, you will be 100 years old in {current_year - age + 100}")