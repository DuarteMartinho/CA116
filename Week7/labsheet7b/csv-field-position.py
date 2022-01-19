#!/usr/bin/env python3

import sys
args = sys.argv[1]

line = input()
i = 0
j = 0
while j < len(line) and line[j] != ",":
    j += 1

if line[:j] == args:
    print(i)
    searching = False
else:
    i = 1
    searching = True

k = j + 1
while k < len(line) and searching:
    if line[k] == ",":
        if line[j + 1:k] == args:
            searching = False
        else:
            i += 1
            j = k
    k += 1

if i >= 1:
    print(i)
