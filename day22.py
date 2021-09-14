# Write a Python function to check whether a string is a pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"

import string, sys

string_input = input('Type the string to be pangram tested: ')


def is_pangram(string_tested, alphabet = string.ascii_lowercase):
    pangram_test = set(alphabet)
    return pangram_test <= set(string_tested.lower())


print(is_pangram(string_input))