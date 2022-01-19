#!/usr/bin/env python3

n = 10
total = 0
i = 0
while i < n:
    numIn = int(input())
    if i == 0:
        printNumber = numIn
    if numIn >= printNumber:
        printNumber = numIn
    i += 1
print(printNumber)
