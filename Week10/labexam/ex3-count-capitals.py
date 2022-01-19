#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

total = 0
i = 0
while i < len(lines):
    line = lines[i].rstrip()
    j = 0
    while j < len(line):
        if (line[j] >= "A" and "Z" >= line[j]):
            total = total + 1
        j += 1
    i += 1

print(total)
