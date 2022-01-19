#!/usr/bin/env python3

s = input()

parseDate = ""
parseDay = ""
parseMonth = ""
parseYear = ""

i = 0
while i < len(s) and (s[i] != " "):
    i += 1

a = i
i = i + 1
b = i

while i < len(s) and (s[i] != " "):
    i += 1
c = i
i = i + 1
d = i
while i < len(s) and (s[i] != ","):
    i += 1
e = i
i = i
f = i
while i < len(s):
    i += 1
g = i
parseData = s[d:e] + " " + s[b:c] + s[f:g] + " (" + s[:a] + ")"
print(parseData)
