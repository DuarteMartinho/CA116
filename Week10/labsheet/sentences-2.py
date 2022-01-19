#!/usr/bin/env python3

import sys

lineIn = sys.stdin.read().split()
lineIn[0] = lineIn[0].capitalize()

i = 0
while i < len(lineIn) - 1:
    word = lineIn[i].rstrip()
    lenghtWord = len(word)
    if word[lenghtWord - 1] == ".":
        lineIn[i] = word + "\n"
        if (lineIn[i + 1][0] <= "A" or lineIn[i + 1][0] >= "Z"):
            lineIn[i + 1] = lineIn[i + 1].capitalize()
    elif word[lenghtWord - 1] == "?":
        lineIn[i] = word + "\n"
        if (lineIn[i + 1][0] <= "A" or lineIn[i + 1][0] >= "Z"):
            lineIn[i + 1] = lineIn[i + 1].capitalize()
    elif word[lenghtWord - 1] == "!":
        lineIn[i] = word + "\n"
        if (lineIn[i + 1][0] <= "A" or lineIn[i + 1][0] >= "Z"):
            lineIn[i + 1] = lineIn[i + 1].capitalize()
    else:
        lineIn[i] = word + " "
    i += 1
print("".join(lineIn))
