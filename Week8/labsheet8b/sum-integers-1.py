#!/usr/bin/env python3

import sys

x = sys.stdin.readline()
y = x.rstrip()
total = 0
while y != "":
    total += int(y)
    x = sys.stdin.readline()
    y = x.rstrip()

print(total)
