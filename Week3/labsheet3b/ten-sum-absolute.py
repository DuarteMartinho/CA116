#!/usr/bin/env python3

n = 10
total = 0
i = 0

while i < n:
    numIn = int(input())
    if numIn > 0:
        total = total + numIn
    else:
        numIn = numIn * -1
        total = total + numIn
    i += 1

print(total)
