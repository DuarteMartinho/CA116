#!/usr/bin/env python3

NumList = []
i = 0
k = 0

while k < 2:
    s = input()
    while s != "end":
        NumList.append(int(s))
        i = 0
        while i < len(NumList):
            j = i + 1
            while j < len(NumList):
                if NumList[i] > NumList[j]:
                    tmp = NumList[i]
                    NumList[i] = NumList[j]
                    NumList[j] = tmp
                j = j + 1
            i += 1
        s = input()
    k += 1
i = 0

while i < len(NumList):
    print(NumList[i])
    i += 1
