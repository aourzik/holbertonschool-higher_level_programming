#!/usr/bin/python3

args = []

if not args:
    print(f"{len(args)} : arguments.")
else:
    for i in range(len(args)):
        if len(args) == 1:
            print(f"{len(args)} : argument :")
            print(f"{i} : {args[i]}")
        else:
            print(f"{len(args)} : arguments :")
            print(f"{i} : {args[i]}")
