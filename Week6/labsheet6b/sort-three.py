#!/usr/bin/env python3

NumList = []
i = 0
while i < 3:
    numIn = int(input())
    NumList.append(numIn)
    j = 0
    while j < len(NumList) - 1:
        if NumList[j] > NumList[j + 1]:
            tmp = NumList[j]
            NumList[j] = NumList[j + 1]
            NumList[j + 1] = tmp
            j = 0
        else:
            j += 1
    i += 1

i = 0
while i < len(NumList):
    print(NumList[i])
    i += 1
