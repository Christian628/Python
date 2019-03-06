#! /usr/bin/env python3
"""
Formated multiplication table
"""


import sys

def multi(a):
    align = len(str(10 * a)) # used to format to variable places 
    for i in range(1,11):
        print(f"{i:>{align}d} * {a:d} = {a*i:>{align}d}")


if __name__ == "__main__":
    if(len(sys.argv) == 2):
        multi(int(sys.argv[1]))
else:
    print("Error")
