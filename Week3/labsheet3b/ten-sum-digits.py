#!/usr/bin/env python3

n = 10
total = 0
i = 0
while i < n:
    numIn = int(input())
    if numIn < 0:
        lastDigit = (numIn * -1) % 10
        total = total + lastDigit
    else:
        lastDigit = numIn % 10
        total = total + lastDigit
    i += 1
print(total)
