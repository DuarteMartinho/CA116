#!/usr/bin/env python3

import sys

first_arg = int(sys.argv[1])

spaces = " "
char = "*"
half = first_arg // 2

numChar = 1
i = half
while i > 0:
    line = ((i) * spaces) + (char * numChar)
    print(line)
    numChar += 2
    i -= 1

print(char * first_arg)

numChar = first_arg - 2
i = 0
while i < half:
    line = ((i + 1) * spaces) + (char * numChar)
    print(line)
    numChar -= 2
    i += 1
