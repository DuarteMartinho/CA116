#!/usr/bin/env python3

s = input()

i = 0
while s != "end":
    line = s.rstrip()
    line_list = line.split()
    code = line_list[3]
    print(code)
    s = input()
    i += 1
