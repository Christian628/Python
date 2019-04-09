#!usr/bin/env python3
"""
Justify text to max number of chars.
"""

import sys

def just(file_name,width,output):
    with open(file_name) as f:
        text = f.readlines()
    for i in range(len(text)):
        if output == "None":
            print(text[i].ljust(int(width)))
        else:
            file = open(output,"a")
            file.write(text[i].ljust(int(width)))
            file.close()

if __name__ == "__main__":
    if(len(sys.argv) < 4):
        just(sys.argv[1],sys.argv[2],"None")
    else:
        just(sys.argv[1],sys.argv[2],sys.argv[3])

else:
    print("Error")
