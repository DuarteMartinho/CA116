#!/usr/bin/env python3

s = input()
answer = ""
i = 0

while i < len(s):
    lastletter = s[0]
    middle = s[1:(len(s) - 1)]
    firstletter = s[len(s) - 1]
    answer = firstletter + middle + lastletter
    i += 1

print(answer)
