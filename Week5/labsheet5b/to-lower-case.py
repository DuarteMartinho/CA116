#!/usr/bin/env python3

upper = "ABCDEFGHIFKLMNOPQRSTUVWXYZ"
lower = "abcdefghifklmnopqrstuvwxyz"
phrase = ""
lineIn = "start"
while lineIn != "end":
    lineIn = input()
    if lineIn != "end":
        x = lineIn
        i = 0
        while i < len(lineIn):
            j = 0
            while j < 26:
                if lineIn[i] == upper[j]:
                    if i == 0:
                        x = lower[j] + x[i + 1:]
                    else:
                        x = x[:i] + lower[j] + x[i + 1:]
                j += 1
            i += 1
        print(x)
