#!/usr/bin/env python3

s = input()
n = int(input())

ncopies = (s + "-") * (n)

print(ncopies[0: len(ncopies) - 1])
