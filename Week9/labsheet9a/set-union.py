#!/usr/bin/env python3

allwords = []
with open("a.txt", "r") as f_in:
    allwords = f_in.readlines()
    with open("b.txt", "r") as f_in2:
        allwords += f_in2.readlines()

seen = {}
i = 0
while i < len(allwords):
    word = allwords[i].rstrip()
    if word not in seen:
        seen[word] = word
    i += 1
for word in seen:
    print(word)
