#! /usr/bin/env python3
"""
Counts the number of prime numbers in an interval
"""

import sys
import math

def prim(a,b):
    if a > b:
        a, b = b, a
    count = 0
    for i in range(a, b + 1):
        if i > 1:
            p = 1
            for j in range(2,int(math.sqrt(i)) + 1):
                if i % j == 0:
                    p = 0
                    break
            if p == 1:
                count += 1
    print(count)


if __name__ == "__main__":
    if len(sys.argv) == 3:
        prim(int(sys.argv[1]),int(sys.argv[2]))
else:
    print("Error")


