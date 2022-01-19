#!/usr/bin/env python3

lineIn = "start"
while lineIn != "end":
    lineIn = input()
    if lineIn != "end":
        i = len(lineIn) - 1
        while i < len(lineIn) and (lineIn[i] != "/"):
            i -= 1
        j = i
        while j < len(lineIn):
            j += 1
            if j + 3 < len(lineIn):
                if (lineIn[j] == "p") and (lineIn[j + 1] == "y"):
                    k = j + 2
                    print(lineIn[i + 1:j + 2])
                    j = len(lineIn)
