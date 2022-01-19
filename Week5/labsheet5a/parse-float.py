#!/usr/bin/env python3

s = input()
x = ""
y = ""

i = 0
while i < len(s) and (s[i] != "."):
    x = x + s[i]
    i += 1

i = i + 1
while i < len(s):
    y = y + s[i]
    i += 1
print(x)
print(y)
