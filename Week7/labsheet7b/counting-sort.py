#!/usr/bin/env python3

s = input()
a = []

i = -1
while s != "end":
    a.append(int(s))
    s = input()
    i += 1

if len(a) > 0:
    ans = a[0]

i = 0
j = 0
x = True
while x and i < len(a):
    if a[i] <= ans:
        ans = a[i]
        j = i
    i += 1
    if i == len(a):
        print(a[j])
        a.pop(j)
        if i == 0:
            x = False
        if 1 < i:
            ans = a[0]
        i = 0
        j = 0
