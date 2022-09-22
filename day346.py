# Create a program that will play the “cows and bulls” game with the user. The game works like this:
#
# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.”
# Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over.
# Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

import random

num_len = 4
number_list = random.sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], num_len)
number = "".join(number_list)
cow = 0
while cow < num_len:
    cow = 0
    bull = 0
    validity = 0

    guess = input("Enter your number: ")

    for i in guess:
        if i in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] and len(guess) == num_len:
            validity = validity +1

    if validity == num_len:
        for i in range(num_len):
            if number[i] == guess[i]:
                cow = cow + 1
            elif number[i] in guess:
                bull = bull + 1

        if cow == num_len:
            win = "\nYou got it correct!! Congratulations!"
        else:
            win = "\nTry again!"
            tries += 1
        print("cows :", cow, ", bulls :", bull, win)

    else:
        print("\nPlease enter a valid number: ")