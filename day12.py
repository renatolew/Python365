# Create a function that takes a list of integers and adds 1 to all even numbers on that list while mantaining the uneven numbers as they are.

number_list = [12, 14, 55, 102, 9, 64, 32, 91, 22, 84, 77]

def one_to_evens(list):
    count = 0
    while count < len(list):
        if list[count] % 2 == 0:
            list[count] += 1
            count += 1
        else:
            count += 1
    return list

print(one_to_evens(number_list))