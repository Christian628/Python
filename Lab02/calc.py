#! /usr/bin/env python3
"""
One liner
"""

import sys


def adder(n):
    print(int(n) + int(n + n) + int(n + n + n))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        adder(sys.argv[1])
else:
    print("Error")
