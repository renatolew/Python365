# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.
# For example, say I type the string:
#
#   My name is Michele
#
# Then I would see the string:
#
#   Michele is name My


def reverseWord(x):
  y = x.split()
  return " ".join(y[::-1])

print(reverseWord("Eu me chamo Renato"))
