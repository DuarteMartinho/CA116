#!/usr/bin/env python3

import sys

grepWord = sys.argv[1]
a_list = []

s = input()
while s != "end":
    a_list.append(s)
    s = input()

i = 0
while i < len(a_list):
    j = 0
    while j < len(a_list[i]):
        sentence = a_list[i]
        if sentence[j: (j + len(grepWord))] == grepWord:
            print(a_list[i])
            j = len(a_list[i])
        j += 1
    i += 1
