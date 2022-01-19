#!/usr/bin/env python3

numIn = int(input())

if numIn == 2 or numIn == 3:
    print("prime")
elif numIn % 2 == 0 or numIn % 3 == 0 or numIn == 1:
    print("not prime")
else:
    print("prime")
