# Create a function that reverses a boolean value and returns the string "boolean expected" if another variable type is given.

def reverse_boolean(var):
    if var == True:
        var = False
        return print(var)
    elif var == False:
        var = True
        return print(var)
    else:
        return print('Boolean expected.')


true_var = True
false_var = False
string_var = 'Hello!'

reverse_boolean(true_var)
reverse_boolean(false_var)
reverse_boolean(string_var)