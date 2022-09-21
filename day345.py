# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

import random

rd = random.randint(1,9)
guess = 0
c = 0
while guess != rd and guess != "exit":
    guess = input("Enter a guess between 1 to 9 (type 'exit' to cancel): ")

    if guess == "exit":
        break

    guess = int(guess)
    c += 1

    if guess < rd:
        print("Too low!")
    elif guess > rd:
        print("Too high!")
    else:
        print("You guessed it right!")
        print("You took ", c, "tries!")
