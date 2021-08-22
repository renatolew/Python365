# Create a function that takes a string and returns a new string with all vowels removed.

full_str = input('Type the string to have its vowels removed: \n')

def vowel_remover(string):
    str_list = list(string.lower())
    vowels = 'aeiou'
    for element in str_list:
        if element in vowels:
            str_list.remove(element)
    str_final = ''.join(str_list)
    return str_final

print(vowel_remover(full_str))