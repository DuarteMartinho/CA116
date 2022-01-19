#!/usr/bin/env python3

n = 10
i = 0
total = 0
lineIn = "start"
while lineIn != "end":
    lineIn = input()
    if(lineIn != "end"):
        i = 0
        while i < len(lineIn) and (lineIn[i] != ":"):
            i += 1
        j = len(lineIn) - 1
        while j < len(lineIn) and (lineIn[j] != ":"):
            j -= 1
        path = lineIn[j + 1:]
        user = lineIn[:i]
        print(user, path)
