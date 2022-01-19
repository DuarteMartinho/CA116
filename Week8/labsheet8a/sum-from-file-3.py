#!/usr/bin/env python3

import sys
file_name = sys.argv[1]
total = 0
k = 0
with open(file_name, "r") as num_in:
    a = num_in.readlines()
    i = 0
    while i < len(a):
        line = a[i].strip()
        line_list = line.split()
        j = 0
        while j < len(line_list):
            num = int(line_list[j])
            total += num
            j += 1
        i += 1

print(total)
