#!/usr/bin/env python3
"""
Polish notation calculator. 
"""

import sys

stack = []

for i in sys.argv[1:]:
    if i.isnumeric():
        stack.append(i)
    else:
        a, b = int(stack.pop()), int(stack.pop())
        if i == '+':
            stack.append(a + b)
        elif i == '-':
            stack.append(a - b)
        elif i == '*':
            stack.append(a * b)
        elif i == '/':
            stack.append(a / b)

print(stack.pop())
