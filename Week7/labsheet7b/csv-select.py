#!/usr/bin/env python3

import sys
args = sys.argv[1]

i = 0
while i < len(args) and args[i] != "=":
    i += 1

header = args[:i]
parameter = args[i + 1:]

a = []
s = input()
while s != "end":
    a.append(s)
    s = input()

i = 0
j = 0
countHeader = 0
x = True
while i < len(a[0]) and x:
    if a[0][i] == ",":
        if a[0][j + 1:i] == header or a[0][:i] == header:
            x = False
        j = i
        if x:
            countHeader += 1
    i += 1

x = 1
while x < len(a):
    line = a[x]
    if countHeader == 0:
        i = 0
        while i < len(line) and line[i] != ",":
            i += 1
        if parameter == line[:i]:
            print(line)
    else:
        i = 0
        loop_n_times = 0
        while loop_n_times < countHeader:
            i += 1
            while i < len(line) and line[i] != ",":
                i += 1
            loop_n_times += 1
        if parameter == line[i + 1:((i + 1) + len(parameter))]:
            print(line)
    x += 1
