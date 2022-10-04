# Implement the same exercise as Exercise 1 (Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old), except use f-strings instead of the + operator to print the resulting output message.


name = input("What is your name? ")
age = int(input("How old are you? "))
year = 2022 - age + 100
print(f"{name}, you will be 100 years old in the year {year}!")