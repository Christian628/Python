#!/usr/bin/env python3
"""
Even and odd multiplicaiton table.
"""

odd = [(i, j, i*j) for i in range(1, 11, 2) for j in range(1, 11)]
even = [(i, j, i*j) for i in range(2, 11, 2) for j in range(1,11)]
print(even)
print(odd)

