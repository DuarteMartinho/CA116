#!/usr/bin/env python3

s = input()
total = 0

while s != "end":
    line = s.rstrip()
    line_list = line.split()
    hour = line_list[2]
    total += int(hour)
    s = input()

print(total)
