#!/usr/bin/env python3

totalPos = 0
totalNeg = 0
numIn = int(input())

i = 0
while numIn != 0:
    if numIn < 0:
        totalNeg = totalNeg + numIn
    elif numIn > 0:
        totalPos = totalPos + numIn
    numIn = int(input())
    i += 1
print(totalNeg, totalPos)
