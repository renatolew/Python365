# Create a new list from a two list using the following condition
#
# Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.


def merge_list(list1, list2):
    result_list = []

    for num in list1:
        if num % 2 != 0:
            result_list.append(num)

    for num in list2:
        if num % 2 == 0:
            result_list.append(num)
    return result_list


list1 = [10, 12, 15, 17, 20, 24, 25, 28, 30, 35]
list2 = [40, 45, 60, 75, 90, 93, 96, 99, 100, 102]
print("First list: ", list1)
print("Second list: ", list2)
print("\nResult list:", merge_list(list1, list2))