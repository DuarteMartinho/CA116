#!/usr/bin/env python3

s = input()
digits = len(s) - 1

totalSum = 0

i = 0
while i < len(s):
    totalSum = totalSum + int(s[digits])
    digits = digits - 1
    i += 1

print(totalSum)
