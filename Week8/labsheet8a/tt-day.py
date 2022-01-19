#!/usr/bin/env python3

s = input()
all_list = []

while s != "end":
    line = s.rstrip()
    all_list.append(line)
    s = input()

n = input()
i = 0
while i < len(all_list):
    line = all_list[i]
    line_list = line.split()
    day = line_list[0]
    if day == n:
        name_joint = " ".join(line_list)
        print(name_joint)
    i += 1
