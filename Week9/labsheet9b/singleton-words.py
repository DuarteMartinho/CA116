#!/usr/bin/env python3

import sys
words = sys.stdin.readlines()
dictionary = {}

i = 0
while i < len(words):
    word = words[i].rstrip()
    if word not in dictionary:
        dictionary[word] = True
    else:
        dictionary[word] = False
    i += 1

for word in dictionary:
    if dictionary[word]:
        print(word)
