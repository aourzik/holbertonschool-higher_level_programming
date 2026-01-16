#!/usr/bin/python3
import sys

args = sys.argv[1:]

if __name__ == "__main__":
    if not args:
        print(f"{len(args)} arguments.")
    else:
        if len(args) == 1:
            print(f"{len(args)} argument:")
        else:
            print(f"{len(args)} arguments:")
    for i in range(len(args)):
        print(f"{i + 1}: {args[i]}")
