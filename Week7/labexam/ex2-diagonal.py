#!/usr/bin/env python3

import sys

arguments = sys.argv[1]
numIn = int(arguments)

i = 0
while i < numIn:
    spaces = i * " "
    Line_Out = spaces + "+"
    print(Line_Out)
    i = i + 1
