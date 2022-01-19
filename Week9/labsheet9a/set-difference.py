#!/usr/bin/env python3

seen = {}
with open("a.txt", "r") as f_in:
    words = f_in.readlines()
    i = 0
    while i < len(words):
        word = words[i].rstrip()
        seen[word] = True
        i += 1
    with open("b.txt", "r") as f_in2:
        words2 = f_in2.readlines()
        j = 0
        while j < len(words2):
            word2 = words2[j].rstrip()
            if word2 in seen:
                seen[word2] = False
            j += 1

for word in seen:
    if seen[word]:
        print(word.rstrip())
