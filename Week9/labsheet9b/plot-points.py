#!/usr/bin/env python3

import sys
inputs = sys.stdin.readlines()

graph = []
NumberOfTimes = 20
i = 0
while i < NumberOfTimes:
    line = [" "] * NumberOfTimes
    graph.append(line)
    i += 1

i = 0
while i < len(inputs):
    split = inputs[i].rstrip().split()
    x = int(split[0])
    y = int(split[1])
    graph[y][x] = "*"
    i += 1

lineSeparator = " " + "-" * NumberOfTimes
print(lineSeparator)
i = len(graph) - 1
while i >= 0:
    line = "|" + "".join(graph[i]) + "|"
    print(line)
    i -= 1
print(lineSeparator)
