#!/usr/bin/env python3

import sys

translation = {
    "one": "eins",
    "two": "zwei",
    "three": "drei",
    "four": "vier",
    "five": "funf",
    "six": "sechs",
    "seven": "sieben",
    "eight": "acht",
    "nine": "neun",
    "ten": "zehn",
}

inputs = sys.stdin.readlines()

i = 0
while i < len(inputs):
    word = inputs[i].rstrip()
    if word in translation:
        print(translation[word])
    i += 1
