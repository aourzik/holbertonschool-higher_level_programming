#!/usr/bin/pyhton3

def no_c(my_string):
    remove_letter = "cC"
    new_string = "".join([c for c in my_string if c not in remove_letter])

    print(new_string)
