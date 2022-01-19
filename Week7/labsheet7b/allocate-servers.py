#!/usr/bin/env python3

s = input()
a = []

while s != "end":
    a.append(int(s))
    s = input()

tasks = []

i = 0
j = 1
while i < len(a):

    task = 0
    while j < len(a) and a[i] + 1000 >= a[j]:
        task += 1
        j += 1

    if task > 0:
        tasks.append(task)
    i = j

server_req = 0
i = 0
j = 1
while i < len(tasks):
    if server_req < tasks[i]:
        server_req = tasks[i]
    i += 1
if server_req == 8:
    server_req = 10

print(server_req)
