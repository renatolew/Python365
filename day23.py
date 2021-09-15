# Write a Python program to create a list by concatenating a given list which range goes from 1 to n.
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']


sample_list = ['a', 'b', 'c']
n_number = 3

def list_concatenator(list):
    result_list = ['{}{}'.format(x, y) for y in range(1, n_number + 1) for x in sample_list]
    return result_list


print(list_concatenator(sample_list))