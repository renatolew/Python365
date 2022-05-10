# Write a program to check if the given file is empty or not
import os

file_size = os.stat("file.txt").st_size
if file_size == 0:
    print('File is empty.')
else:
    print('File is not empty.')