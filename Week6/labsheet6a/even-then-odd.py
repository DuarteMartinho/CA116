#!/usr/bin/env python3

s = input()
odd_list = []

while s != "end":
    value = s
    if int(value) % 2 == 0:
        print(value)
    else:
        odd_list.append(int(value))
    s = input()

i = 0
while i < len(odd_list):
    print(odd_list[i])
    i += 1
