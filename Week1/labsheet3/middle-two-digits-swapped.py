#!/usr/bin/env python3

numIn = int(input())

numSplit = numIn % 10000
numSplit = numSplit // 100

num1digit = numSplit // 10
num2digit = numSplit % 10

numSwapped = (num2digit * 10) + num1digit

print(numSwapped)
