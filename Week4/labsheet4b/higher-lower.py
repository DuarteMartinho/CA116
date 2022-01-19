#!/usr/bin/env python3

numIn = int(input())

i = 0
while i < 5:
    numIn2 = int(input())
    if numIn > numIn2:
        print("lower")
        numIn = numIn2
    elif numIn < numIn2:
        print("higher")
        numIn = numIn2
    elif numIn == numIn2:
        print("equal")
        numIn = numIn2
    i += 1
