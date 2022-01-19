#!/usr/bin/env python3

n = 10
i = 0

while i < n:
    numIn = int(input())
    if i == 0:
        printNumber = numIn
    if numIn > 0:
        if numIn <= printNumber:
            printNumber = numIn
    i += 1
print(printNumber)
