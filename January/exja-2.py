#!/usr/bin/env python3

import sys
args = sys.argv[1]
lines = sys.stdin.read().split()
lenght = len(args)

i = 0
while i < len(lines):
    num = int(lines[i].rstrip())
    if num % (10 ** lenght) != int(args):
        print(num)
    i += 1
