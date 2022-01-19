#!/usr/bin/env python3

numIn = int(input())

if(numIn % 3 == 0) and (numIn % 5 == 0):
    print("fizz-buzz")
elif numIn % 3 == 0:
    print("fizz")
elif numIn % 5 == 0:
    print("buzz")
else:
    print(numIn)
