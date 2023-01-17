#!/usr/bin/python3
def uppercase(str):
    new_str =''
    for i in str:
        if ord(i) in range(97, 123):
            new_str = new_str+chr(ord(i)-32)
        else:
            new_str = new_str + i

    print(new_str.format())
