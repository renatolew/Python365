# Create a function that takes a number num and returns its length.
# Even tho the input is a string, the function needs to check the length of an int variable.


num_input = input ('Type the number that you want to measure the length of: \n')
num_int = int(num_input)


def number_length(number):
    num_list = [int(num) for num in str(number)]
    length_num = len(num_list)
    return length_num

print('The length of {} is {}.'.format(num_int, number_length(num_int)))