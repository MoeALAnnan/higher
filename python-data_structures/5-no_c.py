#!/usr/bin/python3
def no_c(my_string):
    a = ""
    for x in range(0, len(my_string)):
        if (my_string[x] != "c") and (my_string[x] != "C"):
            a = a + my_string[x]
    return (a)
