#!/usr/bin/env python3

import sys
file_name = sys.argv[1]

total = 0
with open(file_name, "r") as num_in:
    a = num_in.readlines()
    i = 0
    while i < len(a):
        num = a[i].rstrip()
        total += int(num)
        i += 1

print(total)
