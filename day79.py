# Write a NumPy program to split a given text into lines and split the single line into array values.

import numpy as np


original_text = """01	V	Pikachu
02	V	Bulbasaur
03	V	Squirtle
04	V	Charmander
05	V	Ratata
06	V	Pidgey
07	V	Growlithe
08	V	Vulpix
09	V	Snorlax
10	V	Dratini"""

print("Original text:")
print(original_text)


text_lines = original_text.splitlines()
text_lines = [r.split('\t') for r in text_lines]
result = np.array(text_lines, dtype=np.str)


print("\nArray from the said text:")
print(result)