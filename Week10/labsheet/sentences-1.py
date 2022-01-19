#!/usr/bin/env python3

import sys
lineIn = sys.stdin.read().split()

i = 0
while i < len(lineIn) - 1:
    word = lineIn[i].rstrip()
    lenghtWord = len(word)
    if word[lenghtWord - 1] == ".":
        lineIn[i] = word + "\n"
    elif word[lenghtWord - 1] == "?":
        lineIn[i] = word + "\n"
    elif word[lenghtWord - 1] == "!":
        lineIn[i] = word + "\n"
    else:
        lineIn[i] = word + " "
    i += 1

print("".join(lineIn))
