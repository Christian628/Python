#!/usr/bin/env python3
"""
Function computing factorial
"""

import sys

def fact(n):
    if (n==0 | n== 1):
        return 1
    else:
        a = n
        while n > 1:        
            n -= 1
            a *= n
        return a


if __name__ == "__main__":
    if len(sys.argv) == 2:
        print(fact(int (sys.argv[1])))
    else:
        print("Error")
