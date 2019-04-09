#!usr/bin/env python3
"""
Prints out the number of words on each line.
"""

import sys

if __name__ == "__main__":
    file_name = sys.argv[1]
else:
    print("Error")

with open(file_name) as f:
    lines = f.readlines()

for i in range(len(lines)):
    print(f"{i+1}: {len(lines[i].split())}")

