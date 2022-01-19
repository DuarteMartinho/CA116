#!/usr/bin/env python3

s = input()

i = 0
while s != "end":
    line = s.rstrip()
    line_list = line.split()
    week = line_list[0]
    if week == '3':
        name_joint = " ".join(line_list)
        print(name_joint)
    s = input()
    i += 1
