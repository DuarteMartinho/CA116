#!/usr/bin/env python3

s = input()
a_list = []

while s != "end":
    a_list.append(int(s))
    s = input()

n = input()

i = 0
while i < len(a_list):
    print(int(n) + a_list[i])
    i += 1
