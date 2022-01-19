#!/usr/bin/env python3

import sys

inputs = sys.stdin.readlines()

seen = {}

i = 0
while i < len(inputs):
    word = inputs[i].rstrip()
    if word not in seen:
        seen[word] = True
    elif word in seen:
        print("snap:", word)
        i = len(inputs)
    i += 1
