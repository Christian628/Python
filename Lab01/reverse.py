#!/usr/bin/env python3
"""
Print out arguments in reverse order.
"""

import sys

def reverse():
    """
    Printing arguments in reverse order.
    """

    for i in range(len(sys.argv)-1, 0, -1):
        print(sys.argv[i])


if __name__ == "__main__":
    reverse()
