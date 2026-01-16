#!/usr/bin/python 3
from calculator_1 import add, sub, mul, div

a = 10
b = 5

if __name__ == "__add__":
    print("{} + {} = {}".format(a, b, add(a, b)))
if __name__ == "__sub__":
    print("{} - {} = {}".format(a, b, sub(a, b)))
if __name__ == "__mul__":
    print("{} * {} = {}".format(a, b, mul(a, b)))
if __name__ == "__div__":
    print("{} / {} = {}".format(a, b, div(a, b)))
