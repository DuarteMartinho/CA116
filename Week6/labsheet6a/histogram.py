#!/usr/bin/env python3

numbers_list = []
apperances_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
frequency_sign = "*"
apperances = 0

s = input()
while s != "end":
    newNum = int(s)

    i = 0

    numbers_list.append(newNum)
    while i < len(numbers_list):
        if numbers_list[i] == newNum:
            apperances_list[newNum] = apperances_list[newNum] + 1
            i = len(numbers_list)
        elif i == len(numbers_list) - 1:
            apperances_list[newNum] = apperances_list[newNum] + 1
            i = len(numbers_list)
        i += 1
    s = input()

i = 0
while i < 10:
    print(i, apperances_list[i] * frequency_sign)
    i += 1
