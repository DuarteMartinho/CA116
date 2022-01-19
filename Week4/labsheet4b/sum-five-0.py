#!/usr/bin/env python3

numIn = int(input())
total = 0

i = 0
while numIn != 0:
    total = total + numIn
    numIn = int(input())
    i += 1
print(total)
