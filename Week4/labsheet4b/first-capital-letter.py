#!/usr/bin/env python3

s = input()

capitalletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
missing = True

i = 0
while missing:
    j = 0
    while j < 26 and missing:
        if s[i] == capitalletters[j]:
            print(i)
            missing = False
        j += 1
    i += 1
