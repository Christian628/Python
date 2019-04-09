#!usr/bin/env python3
"""
Prints each word on a separate line.
"""

import sys

with open(sys.argv[1]) as f:
    text = f.read().split()

for i in text:
    print(i)
