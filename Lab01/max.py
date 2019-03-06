#!/usr/bin/env python3
"""
Function that returns the greater of two numbers.
"""

import sys

def maximum(a, b):
    if a > b:
        return a
    return b

if __name__ == "__main__":
    if len(sys.argv) == 3:
        print(maximum(int(sys.argv[1]),int(sys.argv[2])))
    else:
        print("Error")

