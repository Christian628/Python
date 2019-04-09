#!usr/bin/env python3
"""
Counts the number of individual words in a file.
"""

import sys

with open(sys.argv[1]) as f:
    text = f.read().split()

dictionary = {w:0 for w in set(text)}
for w in text:
    dictionary[w] += 1
print(dictionary)
