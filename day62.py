# Write a Python class to reverse a string word by word.

class string_reverse:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))


print(string_reverse().reverse_words('My name is Renato'))