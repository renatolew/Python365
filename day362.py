#  You have a string that consist only of digits. You need to find how many zero digits ("0") are at the beginning of the given string.
#
# Input: A string, that consist of digits.
#
# Output: An Int.


def beginning_zeros(string1):
    string_list = list(string1)
    count_zeroes = 0
    for i in string_list:
        if i == "0":
            count_zeroes += 1
        else:
            break
    return count_zeroes

print(beginning_zeros('100'))
print(beginning_zeros('100100'))
print(beginning_zeros('001001'))
print(beginning_zeros('012345679'))
print(beginning_zeros('0000'))
