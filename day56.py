# Write a Python program to list all files in a directory in Python.

from os import listdir
from os.path import isfile, join

files_list = [f for f in listdir('C:/Users/Renato/Documents/Aulas/Projetos/Python365') if isfile(join('C:/Users/Renato/Documents/Aulas/Projetos/Python365', f))]

print(files_list);