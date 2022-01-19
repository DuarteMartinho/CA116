#!/usr/bin/env python3

i = 0
j = 0
lineIn = input()
start = 0
while i < len(lineIn):
    if (lineIn[i] == ","):
        end = i
        print(lineIn[start:end])
        start = end + 1
    i += 1
print(lineIn[start:])
