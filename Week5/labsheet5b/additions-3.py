#!/usr/bin/env python3

n = 10
i = 0
total = 0
while total != 1000:
    addition = input()
    j = 0
    while j < len(addition) and addition[j] != "+":
        j += 1
    firstNum = j
    secondNum = j + 1
    total = int(addition[:firstNum]) + int(addition[secondNum:])
    print(total)
    i += 1
