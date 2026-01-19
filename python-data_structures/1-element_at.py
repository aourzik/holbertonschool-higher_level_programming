#!/usr/bin/python3

def element_at(my_list, idx):
    for i in my_list:
        if i > idx:
            print(None)
        elif i < 0:
            print(None)
        else:
            print("{:d}".format(i))
