#!/usr/bin/env python3

s = input()

i = 0
j = 1
while i < len(s) - 1 and (s[i] != s[j]):
    j += 1
    i += 1

if i < len(s) - 1:
    print(s[i:j + 1])
