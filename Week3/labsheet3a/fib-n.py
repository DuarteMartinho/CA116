#!/usr/bin/env python3

n = int(input())

term1 = 0
term2 = 1
i = 0
while i < n:
    print(term1)
    term3 = term1 + term2
    term1 = term2
    term2 = term3
    i += 1
