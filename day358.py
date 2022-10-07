# Slice a list to get a smaller list with two strings, and then slice the second string to get only the second word of it.


persons = [ "John", "Marissa", "Pete", "Joao Maria", "Dayton" ]

slice_list = persons[2:4]
print(slice_list)

sec_str = slice_list[1]
print(sec_str)

final_word = sec_str[5:]
print(final_word)