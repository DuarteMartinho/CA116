#!/usr/bin/env python3

s = input()
a = []

while s != "end":
    a.append(s)
    s = input()

n = int(input())

i = 0
while i < len(a):
    j = 0
    k = 0
    term = a[i]
    while k < (n + 1):
        l = j
        j += 1
        while j < len(term) and term[j] != ",":
            j += 1
        k += 1

    i += 1
    if n == 0:
        print(term[:j])
    else:
        print(term[l + 1:j])
