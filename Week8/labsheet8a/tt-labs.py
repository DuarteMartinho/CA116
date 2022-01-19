#!/usr/bin/env python3

s = input()

while s != "end":
    line = s.rstrip()
    line_list = line.split()
    hour = line_list[2]
    if int(hour) > 1:
        name_joint = " ".join(line_list)
        print(name_joint)
    s = input()
