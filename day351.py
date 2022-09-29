# Let’s continue building Hangman. In the game of Hangman, a clue word is given by the program that the player has to guess, letter by letter.
# The player guesses one letter at a time until the entire word has been guessed. (In the actual game, the player can only guess 6 letters incorrectly before losing).
#
# Let’s say the word the player has to guess is “EVAPORATE”.
# For this exercise, write the logic that asks a player to guess a letter and displays letters in the clue word that were guessed correctly.
# For now, let the player guess an infinite number of times until they get the entire word.
# As a bonus, keep track of the letters the player guessed and display a different message if the player tries to guess that letter again.
# Remember to stop the game when all the letters have been guessed correctly!
# Don’t worry about choosing a word randomly or keeping track of the number of guesses the player has remaining - we will deal with those in a future exercise.




if __name__ == '__main__':
	print("Welcome to hangman!!")
	word = "EVAPORATE"
	guessed = "_" * len(word)
	word = list(word)
	guessed = list(guessed)
	lstGuessed = []
	letter = input("guess letter: ")
	while True:
		if letter.upper() in lstGuessed:
			letter = ''
			print("Already guessed!!")
		elif letter.upper() in word:
			index = word.index(letter.upper())
			guessed[index] = letter.upper()
			word[index] = '_'
		else:
			print(''.join(guessed))
			if letter != '':
				lstGuessed.append(letter.upper())
			letter = input("guess letter: ")

		if '_' not in guessed:
			print("You won!!")
			break