# Write a program to accept a string from the user and display characters that are present at an even index number.

str_sentence = input('Enter the sentence:')
print("Original string:", str_sentence)

size_sentence = len(str_sentence)

print("Printing only even index characters")
for i in range(0, size_sentence - 1, 2):
    print("index[", i, "]:", str_sentence[i])