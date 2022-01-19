#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

i = 0
while i < len(lines):
    num = int(lines[i])
    if num >= 100:
        print(num)
        i = len(lines) + 1
    i += 1

if i < len(lines) + 1:
    print("none")
