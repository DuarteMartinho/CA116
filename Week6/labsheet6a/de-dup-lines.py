#!/usr/bin/env python3

a_list = []

s = input()
while s != "end":
    sentence = s

    if len(a_list) == 0:
        a_list.append(sentence)
    else:
        i = 0
        while i < len(a_list):
            if a_list[i] == sentence:
                i = len(a_list)
            elif i == len(a_list) - 1:
                a_list.append(sentence)
                i = len(a_list)
            i += 1
    s = input()

i = 0
while i < len(a_list):
    print(a_list[i])
    i += 1
