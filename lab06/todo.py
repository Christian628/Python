#!usr/bin/env python3 

:w
#vcxsrv server display ant

import sys

if (sys.argv[1] == "-a"):
    with open("todo.txt","a") as f:
        f.write(f"{sys.argv[2]} {sys.argv[3]}\n")

record = []
if (sys.argv[1] == "-l"):
    with open("todo.txt") as f:
        lines = f.readlines()
    for line in lines:
        record.append(line.split())
    print(sorted(record,key=lambda x: x[0]))
