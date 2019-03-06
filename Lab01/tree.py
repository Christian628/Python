#!/usr/bin/env python3
"""
Prints out a tree.
"""

import sys

def tree(height):
    stars = 1
    spaces = height - 1

    for i in range(height - 1):
        for i in range(spaces):
            print(' ',end='')
        for i in range(stars):
            print('*',end='')
        print()
        stars += 2
        spaces -= 1

    for i in range((stars - 1 ) // 2):
        print(' ',end='')
    print('*')



if __name__ == "__main__":
    if(len(sys.argv) == 2 ):
        tree(int(sys.argv[1]))
    else:
        print("Error")
