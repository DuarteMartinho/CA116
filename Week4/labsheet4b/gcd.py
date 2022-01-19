#!/usr/bin/env python3

a = int(input())
b = int(input())

i = 0
while b != 0:
    temp = a % b
    a = b
    b = temp
    i += 1

print(a)
