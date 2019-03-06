#! /usr/bin/env python3
"""
URL parser
"""

import sys

def parse(path):

    tokens = path.split("/")
    suffixes = tokens[-1].split(".")
    for token in tokens[:-1]:
        print(token)
    for suff in suffixes:
        print(suff)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        parse(sys.argv[1])
else:
    print("Error")
