#!/usr/bin/env python3

import sys

arguments = sys.argv[1:]

i = 0
while i < len(arguments):
    numInt = int(arguments[i])
    if numInt > 500:
        print(numInt)
    i = i + 1
