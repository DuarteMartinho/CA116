#!/usr/bin/env python3

import sys
file_name = sys.argv[1]
args = sys.argv[2:]

with open(file_name, "w") as f:
    i = 0
    while i < len(args):
        f.write(args[i] + "\n")
        i += 1
