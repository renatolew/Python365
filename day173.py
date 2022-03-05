# Reverse a given integer number

num = int(input("Type the desired number to be reversed: "))
reverse_number = 0
print("Given Number ", num)
while num > 0:
    slot = num % 10
    reverse_number = (reverse_number * 10) + slot
    num = num // 10
print("Reverse Number ", reverse_number)