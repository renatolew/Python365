# Write a Python program to compute the summation of the absolute difference of all distinct pairs in a given array (non-decreasing order).

def sum_distinct_pairs(array):
    result = 0
    counter = 0
    while counter < len(array):
        result += counter * array[counter] - (len(array)-counter-1) * array[counter]
        counter += 1
    return result


print(sum_distinct_pairs([1,2,3]))

print(sum_distinct_pairs([1,4,5]))

print(sum_distinct_pairs([1,4,5,8,9]))