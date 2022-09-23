# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number.
# The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.
# Extras:
#
#     Use binary search.

def find(ordered_list, element_to_find):
    for element in ordered_list:
        if element == element_to_find:
            return True
    return False


if __name__ == "__main__":
    l = [2, 4, 6, 8, 10]
    print(find(l, 5))
    print(find(l, 10))
    print(find(l, -1))
    print(find(l, 2))

