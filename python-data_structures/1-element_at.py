#!/usr/bin/python3

def element_at(my_list, idx):
    for i in my_list:
        if i > idx:
            return None
        elif i < 0:
            return None
        else:
            print("{:d}".format(i))
