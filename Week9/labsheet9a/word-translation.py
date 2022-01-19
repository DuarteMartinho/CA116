#!/usr/bin/env python3

import sys

translation = {}

with open("translation.txt", "r") as f_in:
    lines = f_in.readlines()
    i = 0
    while i < len(lines):
        words = lines[i].split()
        original_word = words[0].rstrip()
        translation_word = words[1].rstrip()
        translation[original_word] = translation_word
        i += 1

inputs = sys.stdin.readlines()
i = 0
while i < len(inputs):
    word = inputs[i].rstrip()
    if word in translation:
        print(translation[word])
    i += 1
