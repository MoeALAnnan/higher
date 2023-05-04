#!/usr/bin/python3
def no_c(my_string):
    if my_string is not None:
        my_list = list(my_string)
        for x in my_list:
            if x == 'c' or x == 'C':
                my_list.remove(x)
        new_string = ''.join(my_list)
        return (new_string)
