# Find the words with exactly 8 letters using regex.

import re

str = '''Au pays parfume que le soleil caresse,
J'ai connu, sous un dais d'arbres tout empourpres
Et de palmiers d'ou pleut sur les yeux la paresse,
Une dame creole aux charmes ignores.'''


regex = r'\w{8}'
eight_letters = re.findall(regex, str)


print(eight_letters)