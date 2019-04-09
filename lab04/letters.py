#!/usr/bin/env python3

text = "mississippi"

for i in {c for c in text}:
    print(f"{i}:{text.count(i)}")

