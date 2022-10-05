# Modify the word guessing game to have one level of user feedback: if the user does not enter a number between 1 and 9, tell them.
# Don’t count this guess against the user when counting the number of guesses they used.

import random

number = random.randint(1, 9)
number_of_guesses = 0
while True:
	while True:
		try:
			guess = int(input("Guess a number between 1 and 9: "))
			if guess >= 1 and guess <= 9:
				break
			else:
				print("Your input must be a number between 1 and 9 inclusive")
		except ValueError:
			print("You must enter a number")
	number_of_guesses += 1
	if guess == number:
		break
print(f"You needed {number_of_guesses} guesses to guess the number {number}")