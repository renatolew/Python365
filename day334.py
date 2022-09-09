# Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list.

def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

list1 = [23, 65, 19, 90]
pos1, pos2  = 1, 3

print(swapPositions(list1, pos1-1, pos2-1))