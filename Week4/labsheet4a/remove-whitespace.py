#!/usr/bin/env python3

s = input()
answer = ""
digits = 0

i = 0
while i < len(s):
    letter = s[digits]
    if letter != " ":
        answer = answer + letter
    digits = digits + 1
    i += 1

print(answer)
