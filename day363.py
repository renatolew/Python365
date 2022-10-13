#  You have a number and you need to determine which digit in this number is the biggest.
#
# Input: A positive integer.
#
# Output: An integer (0-9).

def max_digit(num):
    num_str = str(num)
    num_list = list(num_str)
    max_dig = 0
    for i in num_list:
        if int(i) > max_dig:
            max_dig = int(i)
    return max_dig



print(max_digit(0))
print(max_digit(637))
print(max_digit(14482))
print(max_digit(92584))

