#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list.sort()
    y = 0
    for x in range(len(my_list)):
        if my_list[x] != my_list[-1]:
            if my_list[x] != my_list[x+1]:
                print("{}".format(my_list[x]))
                y = y + my_list[x]
    return (y + my_list[-1])
