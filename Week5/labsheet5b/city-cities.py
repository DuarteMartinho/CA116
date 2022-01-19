#!/usr/bin/env python3

n = 10
i = 0
total = 0
lineIn = "start"
while lineIn != "end":
    lineIn = input()
    i = 0
    while i < len(lineIn):
        i += 1
        if i < len(lineIn) - 4:
            if ((lineIn[i + 1]) == "C") and ((lineIn[i + 2]) == "i"):
                if ((lineIn[i + 3]) == "t") and ((lineIn[i + 4]) == "y"):
                    print(lineIn[:i + 5])
