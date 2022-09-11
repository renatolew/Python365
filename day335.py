# Given a list of words in Python, the task is to remove the Nth occurrence of the given word in that list.

def RemoveIthWord(list1, word, N):
    newList = []
    count = 0

    for i in list1:
        if (i == word):
            count = count + 1
            if (count != N):
                newList.append(i)
        else:
            newList.append(i)

    list1 = newList

    if count == 0:
        print("Item not found")
    else:
        print("Updated list is: ", list1)

    return newList


list_1 = ["geeks", "for", "geeks"]
word_1 = "geeks"
N_1 = 2

RemoveIthWord(list_1, word_1, N_1)


list_2 = ["me", "many", "I", "me", "more", "my", "me", "aye", "me"]
word_2 = "me"
N_2 = 3

RemoveIthWord(list_2, word_2, N_2)