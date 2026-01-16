#!/usr/bin/python3
import sys

args = sys.argv[1:]

if __name__ == "__main__":
    if not args:
        print(f"{len(args)} arguments.")
    else:
        for i in range(len(args)):
            if len(args) == 1:
                print(f"{len(args)} argument:")
                print(f"{i + 1}: {args[i]}")
            else:
                print(f"{len(args)} arguments:")
                print(f"{i + 1}: {args[i]}")
