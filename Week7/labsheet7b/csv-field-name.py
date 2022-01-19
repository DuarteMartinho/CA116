#!/usr/bin/env python3

import sys
args = int(sys.argv[1])

line = input()
j = 0
k = 0
while k < (args + 1):
    l = j
    j += 1
    while j < len(line) and line[j] != ",":
        j += 1
    k += 1

if args == 0:
    print(line[:j])
else:
    print(line[l + 1:j])
