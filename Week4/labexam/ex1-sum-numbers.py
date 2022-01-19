#!/usr/bin/env python3

n = int(input())
answer = 0
i = 0

while i < n:
    words = input()

    if words == "one":
        numberWord = 1
    elif words == "two":
        numberWord = 2
    elif words == "three":
        numberWord = 3
    elif words == "four":
        numberWord = 4
    else:
        numberWord = 5
    answer = answer + numberWord
    i = i + 1

print(answer)
