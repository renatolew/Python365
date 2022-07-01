# Python program to print all the items in a dictionary

phone_book = {
'John' : [ '8592970000', 'john@xyzmail.com' ],
'Bob': [ '7994880000', 'bob@xyzmail.com' ],
'Tom' : [ '9749552647' , 'tom@xyzmail.com' ]
}
for k,v in phone_book.items():
    print(k, ":", v)