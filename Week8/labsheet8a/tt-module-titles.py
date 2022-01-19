#!/usr/bin/env python3

s = input()

i = 0
while s != "end":
    line = s.rstrip()
    line_list = line.split()
    name = line_list[5:]
    name_joint = " ".join(name)
    print(name_joint)
    s = input()
    i += 1
