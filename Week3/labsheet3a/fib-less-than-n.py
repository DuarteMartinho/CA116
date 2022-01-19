#!/usr/bin/env python3

maxNum = int(input())

term1 = 0
term2 = 1

while term1 < maxNum:
    print(term1)
    term3 = term1 + term2
    term1 = term2
    term2 = term3
