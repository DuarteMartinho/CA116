#!/usr/bin/env python3

s = input()
a = []

while s != "end":
    a.append(int(s))
    s = input()

position = 0
i = 1
while i < len(a):
    if a[i] < a[position]:
        position = i
    i += 1

print(position)
