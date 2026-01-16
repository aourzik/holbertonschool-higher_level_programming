#!/usr/bin/python3
import sys

args = sys.argv[1:]

if __name__ == "__main__":
    if not args:
        print(0)
    else:
        total = sum(int(arg) for arg in args)
        print(total)
