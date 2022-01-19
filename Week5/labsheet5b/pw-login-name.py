#!/usr/bin/env python3

n = 10
i = 0
total = 0
lineIn = "start"
while lineIn != "end":
    lineIn = input()
    i = 0
    while i < len(lineIn) and (lineIn[i] != ":"):
        i += 1
    if(lineIn != "end"):
        print(lineIn[:i])
