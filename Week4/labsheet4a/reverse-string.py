#!/usr/bin/env python3

s = input()
answer = ""
digits = len(s) - 1

i = 0
while i < len(s):
    letter = s[digits]
    answer = answer + letter
    digits = digits - 1
    i += 1

print(answer)
