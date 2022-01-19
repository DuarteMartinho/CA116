#!/usr/bin/env python3

total = 0
lineIn = "start"
while lineIn != "end":
    lineIn = input()
    if(lineIn != "end"):
        j = len(lineIn) - 1
        x = lineIn[j - 6:]
        y = lineIn[j - 9:j - 7]
        if (x == "correct") and (y == "py"):
            total = total + 1
print(total)
