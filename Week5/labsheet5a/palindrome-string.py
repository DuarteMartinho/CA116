#!/usr/bin/env python3

s = input()
x = True

i = 0
while i < len(s):

    if x and s[i] == s[len(s) - 1 - i]:
        x = True
    else:
        x = False
    i += 1

if x:
    print("palindrome")
