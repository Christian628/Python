#!/usr/bin/env python3

def selectionSort(numList):
    for i in range(len(numList)):
        maxnum = max(numList[i:])
        indexnum = numList[i:].index(maxnum) + i 
        numList[indexnum], numList[i] = numList[i] , numList[indexnum]
    return numList

print(selectionSort([1, 5, -5, 10, 0]))
