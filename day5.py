#Hamming distance is the number of characters that differ between two strings.
#To illustrate:
#String1: "abcbba"
#String2: "abcbda"
#Hamming Distance: 1 - "b" vs. "d" is the only difference.
#Create a function that computes the hamming distance between two strings.

print('This is a program that tells you how many characters are different between two strings(hamming distance) of the same lenght!')
str_1 = input('Tell me the first string of the comparison: \n')
str_2 = input('Now tell me the second string of the comparison: \n')
print('Good! Lets calculate now... \n')

list_str_1 = list(str_1)
list_str_2 = list(str_2)

def hamming_distance(string_1, string_2):
    if len(string_1) == len(string_2):
        counter = 0
        hamming = 0
        while counter < len(string_1):
            if string_1[counter] == string_2[counter]:
                counter += 1
            else:
                hamming += 1
                counter += 1
        return print('The hamming distance between this two strings is {}.'.format(hamming))
    else:
        return print('The strings are not of same lenght.')


hamming_distance(list_str_1, list_str_2)
