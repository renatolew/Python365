# Write a Python program to find the position of the second occurrence of a given string in another given string.
# If there is no such string return -1.


def find_string(text_input, target):
	return text_input.find(target, text_input.find(target)+1)


print(find_string("The man ran away with the lady's purse.", "the"))

print(find_string("the man ran away with the lady's purse.", "the"))