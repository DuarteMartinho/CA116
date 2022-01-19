#!/usr/bin/env python3

n = 10
i = 0
while i < n:
    addition = input()
    j = 0
    while j < len(addition) and addition[j] != "+":
        j += 1
    firstNum = j
    secondNum = j + 1
    print(int(addition[:firstNum]) + int(addition[secondNum:]))
    i += 1
