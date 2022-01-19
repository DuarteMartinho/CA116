#!/usr/bin/env python3

numIn = int(input())

if numIn % 2 == 0:
    numIn = numIn // 2
    print(numIn)

else:
    numIn = (numIn * 3) + 1
    print(numIn)
