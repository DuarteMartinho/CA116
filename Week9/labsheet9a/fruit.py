#!/usr/bin/env python3

import sys

fruit = {
    "apple": True,
    "pear": True,
    "orange": True,
    "banana": True,
    "cherry": True,
}

inputs = sys.stdin.readlines()

i = 0
while i < len(inputs):
    word = inputs[i].rstrip()
    if word in fruit:
        print(word)
    i += 1
