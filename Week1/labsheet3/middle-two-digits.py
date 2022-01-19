#!/usr/bin/env python3

numIn = int(input())

numSplit = numIn % 10000
numSplit = numSplit // 100

print(numSplit)
