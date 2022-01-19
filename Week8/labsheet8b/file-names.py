#!/usr/bin/env python3

import sys

x = sys.stdin.readline()
y = x.rstrip()
total = 0
while y != "":
    line = y.split("/")
    print(line[len(line) - 1])
    x = sys.stdin.readline()
    y = x.rstrip()
