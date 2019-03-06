#!/usr/bin/env python3
"""
Returns the greatest of three arguments.
"""

import sys

def maxi(a,b,c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c


if __name__ == "__main__":
    if (len(sys.argv) == 4):
        print(maxi(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3])))
else:
    print("Error")
