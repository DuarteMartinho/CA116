#!/usr/bin/env python3

s = input()
lastletter = 0
i = 0

while i < len(s):
    print(s[lastletter:len(s)])
    lastletter = lastletter + 1
    i += 1
