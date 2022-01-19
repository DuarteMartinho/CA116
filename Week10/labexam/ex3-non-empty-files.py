#!/usr/bin/env python3

import sys
args = sys.argv[1:]

i = 0
while i < len(args):
    file_name = args[i]
    with open(file_name, "r") as f_in:
        lines = f_in.readline()
        if len(lines) > 0:
            print(file_name)
    i += 1
