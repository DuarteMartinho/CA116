#!/usr/bin/env python3

s = input()
a = []

while s != "end":
    a.append(int(s))
    s = input()

position = int(input())
i = position + 1
while i < len(a):
    if a[i] < a[position]:
        position = i
    i += 1

print(position)
