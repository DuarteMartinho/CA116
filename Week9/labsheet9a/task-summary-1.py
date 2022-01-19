#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
tasks = {}

i = 0
while i < len(lines):
    separated = lines[i].rstrip().split(".")
    task_name = ".".join(separated[0:2])
    if separated[2] == "incorrect":
        tasks[task_name] = False
    else:
        tasks[task_name] = True
    i += 1

for task_name in tasks:
    if tasks[task_name]:
        print(task_name)
