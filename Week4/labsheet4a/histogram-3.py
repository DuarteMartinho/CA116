#!/usr/bin/env python3

n = input()
digit = 0

i = 0
while i < len(n):
    numTimes = n[digit]
    digit = digit + 1
    print("*" * int(numTimes))
    i += 1
