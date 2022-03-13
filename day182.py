# Create a list by picking an odd-index items from the first list and even index items from the second

list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]
final_list = list()

odd_elements = list1[1::2]
print("Selecting odd index elements from first list: ")
print(odd_elements)

even_elements = list2[0::2]
print("Selecting even index elements from second list:")
print(even_elements)

print("Printing final list: ")
final_list.extend(odd_elements)
final_list.extend(even_elements)
print(final_list)