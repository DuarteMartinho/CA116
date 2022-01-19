#!/usr/bin/env python3

seen = {}
intersecting = False

with open("a.txt", "r") as f_in:
    words = f_in.readlines()
    i = 0
    while i < len(words):
        word = words[i].rstrip()
        seen[word] = False
        i += 1
    with open("b.txt", "r") as f_in2:
        words = f_in2.readlines()
        j = 0
        while j < len(words):
            word = words[j].rstrip()
            if word in seen:
                intersecting = True
            j += 1


if intersecting:
    print("intersecting")
else:
    print("disjoint")
