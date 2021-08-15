# Create a function that takes a string and returns the number (count) of vowels contained within it.


print('This is a program that counts how many vowels there are in a string!')
str_given = input('What is the string you want to have vowels counted? \n')
lower_str = str_given.lower()

def vowel_counter(string):
    counter = 0
    vowels = set('aeiou')
    for element in string:
        if element in vowels:
            counter += 1
    return counter

print('In this string there are {} vowels!'.format(vowel_counter(lower_str)))