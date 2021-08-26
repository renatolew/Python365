# October 22nd is CAPS LOCK DAY. Apart from that day, every word should be lowercase, so write a function to normalize a word.
# Create a function that takes a string. If the string is all uppercase characters, convert it to lowercase and add an exclamation mark at the end of the word.

str_input = input('Type the word to be tested: \n')

input_list = list(str_input)

def caps_lock_day(string):
    count = 0
    for element in string:
        if element.isupper() == True:
            count += 1

    if count == len(string):
        count_it = 0
        while count_it < len(string):
            string[count_it] = string[count_it].lower()
            count_it += 1

        string[0] = string[0].upper()

        string.append('!')
        string_back = ''.join(string)
        return string_back

    else:
        string_back = ''.join(string)
        return string_back


print(caps_lock_day(input_list))
