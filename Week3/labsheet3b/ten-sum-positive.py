#!/usr/bin/env python3

n = 10
i = 0
total = 0
while i < n:
    numIn = int(input())
    if numIn > 0:
        total = total + numIn
    i += 1
print(total)
