#!/usr/bin/env python3

total = 0
n = int(input())

i = 0
while n != 0:
    if n < 0:
        n = n * -1
    total = total + n
    n = int(input())
    i += 1
print(total)
