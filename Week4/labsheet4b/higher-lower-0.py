#!/usr/bin/env python3

numIn = int(input())


while numIn != 0:
    numIn2 = int(input())
    if numIn2 == 0:
        numIn = numIn2
    elif numIn > numIn2:
        print("lower")
        numIn = numIn2
    elif numIn < numIn2:
        print("higher")
        numIn = numIn2
    elif numIn == numIn2:
        print("equal")
        numIn = numIn2
