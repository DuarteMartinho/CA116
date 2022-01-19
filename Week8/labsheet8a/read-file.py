#!/usr/bin/env python3

with open("input.txt") as f:
    lines = f.readlines()

i = 0
while i < len(lines):
    if i != 7:
        print(lines[i].rstrip())
    else:
        print(lines[i][:len(lines[i]) - 1])
    i += 1
