# Write a program to print the following start pattern using the for loop
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *



rows = 5

# printing until row number
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

# printing the reverse way until 1
for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")
