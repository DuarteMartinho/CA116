#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
users = {}
tasks = {}
i = 0
while i < len(lines):
    separated = lines[i].rstrip().split("/")
    if separated[0] not in users:
        users[separated[0]] = 0
    i += 1

i = 0
while i < len(lines):
    separated = lines[i].rstrip().split(".")
    task_name = ".".join(separated[0:2])
    if separated[2] == "incorrect":
        tasks[task_name] = False
    else:
        tasks[task_name] = True
    i += 1

for line in tasks:
    separated_users = line.rstrip().split("/")
    separated = line.rstrip().split(".")
    if tasks[line]:
        users[separated_users[0]] += 1

for word in users:
    print(word, users[word])
