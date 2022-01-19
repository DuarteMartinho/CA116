#!/usr/bin/env python3

total = 0
with open("numbers.txt", "r") as num_in:
    a = num_in.readlines()
    i = 0
    while i < len(a):
        num = a[i].rstrip()
        total += int(num)
        i += 1

print(total)
