#!/usr/bin/env python3

s = input()
lastletter = len(s)
i = 0
while i < len(s):
    lastletter = lastletter - 1
    print(s[lastletter])
    i += 1
