# Write a Python program to find whether a given array of integers contains any duplicate element.
# Return true if any value appears at least twice in the said array and return false if every element is distinct.

num_list = [1, 2, 3, 4, 5, 6]
num_list2 = [1, 2, 3, 3, 5, 6]

def verify_duplicate(list):
    set_list = set(list)
    len1 = len(list)
    len2 = len(set_list)

    if len1 == len2:
        return True
    else:
        return False

print(verify_duplicate(num_list))
print(verify_duplicate(num_list2))