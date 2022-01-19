#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

n = 13
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

src = lower + upper
dst = lower[n:] + lower[:n] + upper[n:] + upper[:n]

caesar = {}
i = 0
while i < len(src):
    caesar[src[i]] = dst[i]
    i += 1

j = 0
while j < len(lines):
    line = lines[j].rstrip()
    encrytpted = ""
    i = 0
    while i < len(line):
        if line[i] in caesar:
            encrytpted += caesar[line[i]]
        else:
            encrytpted += line[i]
        i += 1
    lines[j] = encrytpted
    j += 1

answer = "\n".join(lines)
print(answer)
