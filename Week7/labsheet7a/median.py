#!/usr/bin/env python3

s = input()
a = []

while s != "end":
    a.append(int(s))
    s = input()

i = 0
while i < len(a):
    j = i + 1
    while j < len(a):
        if a[i] > a[j]:
            tmp = a[i]
            a[i] = a[j]
            a[j] = tmp
        j = j + 1
    i += 1


if len(a) % 2 == 0:
    print(a[(len(a) // 2)])
else:
    print(a[((len(a) - 1) // 2)])
