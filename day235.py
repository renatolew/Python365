# Write a program to remove characters from a string starting from zero up to n and return a new string.

def remove_chars(word, n):
    print('\nOriginal string:', word)
    new_string = word[n:]
    return new_string

sample_str = input("Type the string to have its characters removed: ")

print(remove_chars(sample_str, 4))
print(remove_chars(sample_str, 2))