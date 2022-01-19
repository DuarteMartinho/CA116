#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

i = 0
while i < len(lines):
    j = i + 1
    while j < len(lines):
        line = lines[i].rstrip().split(" ")
        line2 = lines[j].rstrip().split(" ")
        if line[1] > line2[1]:
            tmp = lines[i]
            lines[i] = lines[j]
            lines[j] = tmp
        elif line[1] == line2[1]:
            if line[0] > line2[0]:
                tmp = lines[i]
                lines[i] = lines[j]
                lines[j] = tmp
        j += 1
    i += 1

i = 0
while i < len(lines):
    print(lines[i].rstrip())
    i += 1
