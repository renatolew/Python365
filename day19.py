# Write a Python function to multiply all the numbers in a list.

num_list = [12, 15, -3, 9, -11, 2]

def mult_list(list):
    result = 1
    for i in list:
        result = result * i
    return result


print(mult_list(num_list))
