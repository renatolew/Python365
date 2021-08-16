# Write a function that takes a credit card number and only displays the last four characters.
# The rest of the card number must be replaced by ************.


card_number = input('Type the number of the credit card to be hidden: \n')
card_list = list(card_number)

def card_hide(list):
    counter = 0
    max_counter = len(list) - 4
    while counter < max_counter:
        list[counter] = '*'
        counter += 1
    list = ''.join(list)
    return list

print('The partially hidden card number is {}.'.format(card_hide(card_list)))