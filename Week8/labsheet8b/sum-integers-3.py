#!/usr/bin/env python3

import sys
file_names = sys.argv[1:]
total = 0
x = []

i = 0
while i < len(file_names):
    file_name = file_names[i]
    with open(file_name) as f_in:
        x += f_in.readlines()
    i += 1

i = 0
while i < len(x):
    num = x[i].rstrip()
    total += int(num)
    i += 1

print(total)
