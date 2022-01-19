#!/usr/bin/env python3

s = input()
a_list = []

while s != "end":
    a_list.append(s)
    s = input()

i = 0
while i < len(a_list):
    print(i, len(a_list), a_list[i])
    i += 1
