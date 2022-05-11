# Read line number 4 from the following file


with open("file.txt", "r") as file:
    lines = file.readlines()
    print(lines[3])