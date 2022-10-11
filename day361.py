#  For the input of your function, you will be given one sentence. You have to return a corrected version, that starts with a capital letter and ends with a period (dot).
#
# Pay attention to the fact that not all of the fixes are necessary. If a sentence already ends with a period (dot), then adding another one will be a mistake.


def correct_sentence(string1):
    list1 = list(string1)
    corrected_string = ""
    if list1[0].islower():
        list1[0] = list1[0].upper()
    if list1[-1] != ".":
        list1.append(".")
    for i in list1:
        corrected_string += i
    return corrected_string


print(correct_sentence("greetings, friends"))
print(correct_sentence("Greetings, friends..."))
print(correct_sentence("greetings, friends."))
print(correct_sentence("greetings, Friends"))
