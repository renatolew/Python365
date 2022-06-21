# Python program to implement binary search

def binary_search(numbers, low, high, x):
    if (high >= low):
        mid = low + (high - low)//2
        if (numbers[mid] == x):
            return mid
        elif (numbers[mid] > x):
            return binary_search(numbers, low, mid-1, x)
        else:
            return binary_search(numbers, mid+1, high, x)
    else:
        return -1

numbers = [1, 4, 6, 7, 12, 17, 25]
print(numbers)
x = int(input("Type the number to be searched in the array: "))

result = binary_search(numbers, 0, len(numbers)-1, x)
if (result != -1):
    print("Search successful, element found at position ", result)
else:
    print("The given element is not present in the array")