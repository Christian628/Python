#!usr/bin/env python3

import sys

with open(sys.argv[2]) as f:
    lines = f.readlines()

for line in lines:
    if (sys.argv[1] == "-U"):
        print(line.upper(),end='')
    elif (sys.argv[1] == "-L"):
        print(line.lower(),end='')

