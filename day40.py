# Write a Python program to insert spaces between words starting with capital letters.

import re


def capital_words_spaces(combined_string):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", combined_string)

print(capital_words_spaces("Python"))

print(capital_words_spaces("PythonExercises"))

print(capital_words_spaces("PythonExercisesEveryday"))