#!/usr/bin/env python3

totalPos = 0
totalNeg = 0

i = 0
while i < 5:
    n = int(input())
    if n < 0:
        totalNeg = totalNeg + n
    elif n > 0:
        totalPos = totalPos + n
    i += 1
print(totalNeg, totalPos)
